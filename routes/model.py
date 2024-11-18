from fastapi import APIRouter
from house_data_request import HouseData
import pandas as pd
from xgboost import XGBRegressor
import numpy as np

router = APIRouter(prefix="/model")

model = XGBRegressor()
model.load_model("model.json")
test_data = pd.read_csv("test_data.csv")


def transform_feature(data, feature, transform="log"):
    if transform == "log":
        data[feature] = np.log(data[feature])
    elif transform == "sqrt":
        data[feature] = np.sqrt(data[feature])
    else:
        raise ValueError("Invalid transform")


def transform_data(data):
    columns = ['MedInc', 'AveOccup', 'Latitude', 'Longitude', 'point_location', 'bedrooms_per_room', 'HouseAge']
    high_skew_columns = ["AveRooms", "AveBedrms", "AveOccup"]
    moderate_skew_columns = ["MedInc"]

    for feature in high_skew_columns:
        transform_feature(data, feature)

    for feature in moderate_skew_columns:
        transform_feature(data, feature, "sqrt")

    data["bedrooms_per_room"] = data["AveBedrms"] / data["AveRooms"]
    data["point_location"] = data["Latitude"] + data["Longitude"]
    data = data[columns]
    return data


@router.post("/predict")
def predict(data: HouseData | list[HouseData]):

    if isinstance(data, list):
        data = [d.model_dump() for d in data]
        data = pd.DataFrame(data)
        data = transform_data(data)

        predictions = model.predict(data)
        return predictions.tolist()

    entry = data.model_dump()

    data = pd.DataFrame(entry, index=[0])
    data = transform_data(data)

    prediction = model.predict(data)[0]
    return float(prediction)


@router.get("/sample")
def random_data(num: int = 1):
    entry = test_data.sample(num)
    X = entry.drop("MedHouseVal", axis=1)
    y = entry["MedHouseVal"]
    preds = model.predict(X)
    data = X.to_dict(orient="records")

    for y_true, y_pred, row in zip(y, preds, data):
        row["y_true"] = float(y_true)
        row["y_pred"] = float(y_pred)

    return data

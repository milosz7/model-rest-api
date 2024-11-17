from fastapi import APIRouter
from house_data_request import HouseData
import pandas as pd
from xgboost import XGBRegressor

router = APIRouter(prefix="/model")

model = XGBRegressor()
model.load_model("model.json")
test_data = pd.read_csv("test_data.csv")


@router.post("/predict")
def predict(data: HouseData | list[HouseData]):
    columns = ['MedInc', 'AveOccup', 'Latitude', 'Longitude', 'point_location', 'bedrooms_per_room', 'HouseAge']

    if isinstance(data, list):
        data = [d.dict() for d in data]
        data = pd.DataFrame(data)
        data["bedrooms_per_room"] = data["AveBedrms"] / data["AveRooms"]
        data["point_location"] = data["Latitude"] + data["Longitude"]
        data = data[columns]
        predictions = model.predict(data)
        return predictions.tolist()

    entry = data.model_dump()
    entry["bedrooms_per_room"] = entry["AveBedrms"] / entry["AveRooms"]
    entry["point_location"] = entry["Latitude"] + entry["Longitude"]

    X = pd.DataFrame(entry, index=[0])
    X = X[columns]

    prediction = model.predict(X)[0]
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

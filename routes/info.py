from fastapi import APIRouter

router = APIRouter(prefix="/info")


@router.get("/")
def params_info():
    return {"AveBedrms": "Average number of bedrooms [float]",
            "AveRooms": "Average number of rooms [float]",
            "AveOccup": "Average house occupancy [int]",
            "MedInc": "Median income of the block [float]",
            "HouseAge": "Median house age [int]",
            "Latitude": "Latitude coordinate [float]",
            "Longitude": "Longitude coordinate [float]",
            "data_source": "https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html"}

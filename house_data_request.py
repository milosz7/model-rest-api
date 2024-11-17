from pydantic import BaseModel


class HouseData(BaseModel):
    AveBedrms: float
    AveRooms: float
    AveOccup: float
    MedInc: float
    HouseAge: int
    Latitude: float
    Longitude: float

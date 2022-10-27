from pydantic import BaseModel

class FAPerformance(BaseModel):
	age: int
	mrt: float
	pcr: float
	oer: float

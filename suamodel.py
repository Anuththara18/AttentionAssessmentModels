from pydantic import BaseModel

class SUAPerformance(BaseModel):
	age: int
	mrt: float
	pcr: float
	oer: float
	td: float

from pydantic import BaseModel

class Performance(BaseModel):
	age: int
	mrt: float
	pcr: float
	oer: float
	cer: float

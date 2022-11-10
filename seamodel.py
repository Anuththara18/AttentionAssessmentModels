from pydantic import BaseModel

class SEAPerformance(BaseModel):
	age: int
	td: float
	pcr: float
	oer: float
	cer: float

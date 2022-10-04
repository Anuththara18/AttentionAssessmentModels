from pydantic import BaseModel

class Performance(BaseModel):
	mrt: float
	pcr: float
	oer: float
	cer: float

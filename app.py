from fastapi import FastAPI
import uvicorn
import pickle
from models import Performance

app=FastAPI()

model=pickle.load(open("selectivemodel.sav", "rb"))

@app.get("/{name}")
async def hello(name):
	return {"Hello {} sss".format(name)}
	
@app.get("/")
async def greet():
	return {"Hello World!"}
	
@app.post("/predict")
async def predict(req:Performance):
	age=req.age
	mrt=req.meanReactionTime
	pcr=req.percentageOfCorrectResponses
	oer=req.omissionErrorRate
	cer=req.commissionErrorRate
	features=list([mrt,pcr,oer,cer])
	predict=model.predict([features])
	if(predict==1):
		return {"Ans 1 {}".format(predict)}
	elif (predict==2):
		return {"Ans 2 {}".format(predict)}
	elif (predict==3):
		return {"Ans 3 {}".format(predict)}
	else:
		return {"Ans 4 {}".format(predict)}
	
if __name__=="__main__":
	uvicorn.run(app, host="127.0.0.1", port=5049)
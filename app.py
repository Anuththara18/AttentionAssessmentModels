from fastapi import FastAPI
import uvicorn
import pickle
from models import Performance
from famodel import FAPerformance
from seamodel import SEAPerformance
from suamodel import SUAPerformance

app = FastAPI()

modelaa1 = pickle.load(open("modelaa1.sav", "rb"))
modelaa2 = pickle.load(open("modelaa2.sav", "rb"))
modelsea = pickle.load(open("modelsea.sav", "rb"))
modelsua = pickle.load(open("modelsua.sav", "rb"))
modelda = pickle.load(open("modelda.sav", "rb"))
modelfa1 = pickle.load(open("modelfa1.sav", "rb"))
modelfa2 = pickle.load(open("modelfa2.sav", "rb"))


@app.get("/{name}")
async def hello(name):
	return {"Hello {} sss".format(name)}
	
@app.get("/")
async def greet():
	return {"Hello World!"}

@app.post("/aa1predict")
async def predict(req:Performance):
	age=req.age
	mrt=req.mrt
	pcr=req.pcr
	oer=req.oer
	cer=req.cer
	features=list([age,mrt,pcr,oer,cer])
	predict=modelaa1.predict([features])
	if(predict==0):
		return {"{}".format(predict)}
	else:
		return {"{}".format(predict)}

@app.post("/aa2predict")
async def predict(req:Performance):
	age=req.age
	mrt=req.mrt
	pcr=req.pcr
	oer=req.oer
	cer=req.cer
	features=list([age,mrt,pcr,oer,cer])
	predict=modelaa2.predict([features])
	if(predict==0):
		return {"{}".format(predict)}
	elif (predict==1):
		return {"{}".format(predict)}
	else:
		return {"{}".format(predict)}
	
@app.post("/dapredict")
async def predict(req:Performance):
	age=req.age
	mrt=req.mrt
	pcr=req.pcr
	oer=req.oer
	cer=req.cer
	features=list([age,mrt,pcr,oer,cer])
	predict=modelda.predict([features])
	if(predict==0):
		return {"{}".format(predict)}
	else:
		return {"{}".format(predict)}
	
@app.post("/faonepredict")
async def predict(req:FAPerformance):
	age=req.age
	mrt=req.mrt
	pcr=req.pcr
	oer=req.oer
	features=list([age,mrt,pcr,oer])
	predict=modelfa1.predict([features])
	if(predict==0):
		return {"{}".format(predict)}
	else:
		return {"{}".format(predict)}
	
@app.post("/fatwopredict")
async def predict(req:FAPerformance):
	age=req.age
	mrt=req.mrt
	pcr=req.pcr
	oer=req.oer
	features=list([age,mrt,pcr,oer])
	predict=modelfa2.predict([features])
	if(predict==0):
		return {"{}".format(predict)}
	else:
		return {"{}".format(predict)}
	
@app.post("/seapredict")
async def predict(req:SEAPerformance):
	age=req.age
	td=req.td
	pcr=req.pcr
	oer=req.oer
	cer=req.cer
	features=list([age,td,pcr,oer,cer])
	predict=modelsea.predict([features])
	if(predict==0):
		return {"{}".format(predict)}
	elif (predict==1):
		return {"{}".format(predict)}
	elif (predict==2):
		return {"{}".format(predict)}
	else:
		return {"{}".format(predict)}
    
@app.post("/suapredict")
async def predict(req:SUAPerformance):
	age=req.age
	mrt=req.mrt
	pcr=req.pcr
	oer=req.oer
	td=req.td
	features=list([age,mrt,pcr,oer,td])
	predict=modelsua.predict([features])
	if(predict==0):
		return {"{}".format(predict)}
	elif (predict==1):
		return {"{}".format(predict)}
	else:
		return {"{}".format(predict)}

"""

if __name__=="__main__":
	uvicorn.run(app, host="127.0.0.1", port=5049)
	
"""
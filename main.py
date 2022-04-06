from fastapi import Request, FastAPI
from json import JSONDecodeError
# import JSONDecodeError

from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from vehicules import Voiture
from vehicules import Bateau
from vehicules import Moto
from vehicules import Avion
app = FastAPI()

@app.get('/start')
async def getInfo(request: Request):
    try:
        data = await request.json()
        for i in data:
            print(i)
    except JSONDecodeError:
        return JSONResponse({'Confirmation': "L'API est lancé"})



#Route total pour chaque type de Véhicule
@app.get('/vehicules/Voiture')
def getVoitures():
    return 'Nombre de voiture:',{Voiture.counter}

@app.get('/vehicules/Bateau')
def getBateau():
    return 'Nombre de Bateau:',{Bateau.counter}

@app.get('/vehicules/Moto')
def getMoto():
    return 'Nombre de Moto:',{Moto.counter}

@app.get('/vehicules/Avion')
def getAvion():
    return 'Nombre de Avion:',{Avion.counter}


#Route total Véhicules
@app.get('/vehicules')
def getNombre():
    return 'Nombre total de véhicules:',{Avion.counter+Moto.counter+Bateau.counter+Voiture.counter}




@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "Cette route n'existe pas" })


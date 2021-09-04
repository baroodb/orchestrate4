from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def getHome():
    return {'Response': 'Hello the world....'}
    
@app.get('/start')
def getHome2():
    return {'Response': 'Hello the world....'}

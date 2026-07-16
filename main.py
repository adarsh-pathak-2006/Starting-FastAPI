from fastapi import FastAPI

app=FastAPI()


@app.get("/calculate")
def calculator(a:int, b:int, symbol:str):
    if symbol=="add":
        return {'answer':a+b}
    elif symbol=="subtract":
        return {'answer':a-b}
    elif symbol=="multiply":
        return {'answer':a*b}
    elif symbol=="divide":
        return {'message':a/b}
    else:
        return {'message':'enter operation'}


@app.get("/search")
def search(query:str):
    return { 'Query':query }

@app.get("/square")
def square(number:int):
    return {'answer':number**2}
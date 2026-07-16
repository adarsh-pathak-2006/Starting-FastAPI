from fastapi import FastAPI

app=FastAPI()


@app.get("/calculate/{a}/{symbol}/{b}")
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
        return {'message':'enter +, -, *, /'}

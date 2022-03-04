from __future__ import division
import random
from fastapi import FastAPI
from enum import Enum


class operationTypes(str, Enum):
    addition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"
    division = "division"


app = FastAPI()


@app.get("/calculator/{operation}/{a}/{b}")
def perform(operation: operationTypes, a: float, b: float):
    if operation == operationTypes.addition:
        return {"operation": operation, "result": a+b}
    elif operation == operationTypes.subtraction:
        return {"operation": operation, "result": a-b}
    elif operation == operationTypes.multiplication:
        return {"operation": operation, "result": a*b}
    elif operation == operationTypes.division:
        return {"operation": operation, "result": a/b}


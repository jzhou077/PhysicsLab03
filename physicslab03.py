from vpython import *
import csv
from model import *

modelId = int(input("model? "))


model = Model(0.0009, 1.42, "physicslab03\physicslab03trial1data.csv")
model2 = Model(0.0018, 1.25, "physicslab03\physicslab03trial2data.csv")
model3 = Model(0.0027, 1.04, "physicslab03\physicslab03trial3data.csv")
model4 = Model(0.0036, 0.82, "physicslab03\physicslab03trial4data.csv")

models = {1: model, 2: model2, 3: model3, 4: model4}

models[modelId].runModel()
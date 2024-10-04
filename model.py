from vpython import *
import csv

class Model:
    def __init__(self, mass, time, data):
        self.mass = mass
        self.time = time
        self.data = data
    
    def runModel(self):
        f1 = gcurve()

        m = self.mass
        g = 9.8
        k = g/2207

        t = 0
        y = 0
        v = 0
        p = m*v

        dt = 0.001

        while t < self.time:
            F = (k*(p/m)**2) - (m*g)
            p += F*dt
            y += (p/m)*dt
            t += dt

            f1.plot(t, y)

        print("final position = ",y," m")
        print("fall time = ",t," s")

        f2 = gcurve(color=color.red)

        with open(self.data) as file:
            reader = csv.reader(file)
            for row in reader:
                f2.plot(float(row[0]), float(row[1]))

        input("stop?")
import numpy as np

class Derivative:
    def __init__(self, TimeArray, Function):
        self.time = TimeArray
        self.function = Function
    def fstDerivative(self, t):
        dt = 1e-3
        return (eval(self.function+"(t+dt)")-eval(self.function+"(t)"))/dt  
    def sndDerivative(self, t):
        dt = 1e-3
        return (eval(self.function+"(t+dt)")-2*eval(self.function+"(t)")+eval(self.function+"(t-dt)"))/dt  

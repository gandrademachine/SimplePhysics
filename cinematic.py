import numexpr as ne
import numpy as np
import matplotlib.pyplot as plt
from calculus import Derivative 

class position:
    def __init__(self, TimeArray, Function):
        self.time = TimeArray
        self.function = Function
    def Position(self):
        return eval(self.function+"(self.time)")
    def Velocity(self, t):
        der = Derivative(self.time,self.function)
        if t in self.time:
            return der.fstDerivative(t)
        else:
            return 0
    def Acceleration(self, t):
        der = Derivative(self.time,self.function)
        if t in self.time:
            return der.sndDerivative(t)
        else:
            return 0
    def Plot (self, t):
        s = self.Velocity(t)
        X, Y, U, V = np.array( ( t ) ), np.array( ( eval(self.function+"(t)") ) ), np.array( ( t+ np.cos( s ) ), dtype = float), np.array( ( eval(self.function+"(t)")+np.sin( s ) ), dtype = float)
        fig, ax = plt.subplots()
        ax.quiver(X ,Y, U, V,  angles='xy', scale_units='xy', scale=1)

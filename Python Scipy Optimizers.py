# optimizers in scipy: they are a set of procedures difined in scipy that either fine the minimum value of a function or a root of an equation
#optimizing function: all the algorithms which helps in minimizing the data.
#root of an equation: x + cos(x), we will solve it via optimize.root fuction
#this function take 2 arguments: "fun" and x0
#example: here we will find te root of the equation x + cos(x) :
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)


#here we want the info about not just x but the whole root:
def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot)


# minimizing the function or data:
#high point are called maxima and low point are called minima.
#finding the minima:
# we use scipy.optimize.minimize(). int uses 3 arguments: "fun", x0 and method: it also has some legal values: "CG", "BFGS","NEWTON-CG","L-BFGS","TNC","COBYLA","SLSQP".
#callback: functions called after iteration of optimizations.

#example of the above: in which we will minimize the function: x^2 + x + 2 with BFGS
from scipy.optimize import minimize
def eqn(x):
    return x**2 + x + 2
mymin = minimize(eqn,0,method="BFGS")
print(mymin)
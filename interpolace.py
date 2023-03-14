import pylab as lab
import scipy.interpolate as inp

x = [0, 0.3, 0.5, 0.8, 1, 2, 3]
y = [0, 0.1, 0.5, 1, 3, 10, 30]

x = list(map(float, x))
y = list(map(float, y))

lab.plot(x,y,'ro', label = "původní hodnoty")

funkce = inp.CubicSpline(x,y)
newX = lab.linspace(0, 3, 99)
newY = funkce(newX)
lab.plot(newX, newY, label = "Cubicspline")

lab.plot(newX, inp.Akima1DInterpolator(x,y)(newX), label = "AkimalDInterpolator")
lab.plot(newX, inp.PchipInterpolator(x,y)(newX), label = "PchipInterpolator")
lab.plot(newX, inp.UnivariateSpline(x,y)(newX), label = "UnivariateSpline")

lab.legend()
lab.grid()
lab.show()

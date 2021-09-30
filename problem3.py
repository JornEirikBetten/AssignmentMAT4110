import matplotlib
matplotlib.rcParams['text.usetex'] = True
import numpy as np
import matplotlib.pyplot as plt


def f(x): 
	return x**2*(x**2 - 5*x + 5)
	
def df(x): 
	return x**2*(2*x-5) + 2*x*(x**2-5*x+5)
	
def ddf(x): 
	return 12*x**2-30*x+10
	
x = np.linspace(-1, 4, 1001)
plt.plot(x, ddf(x), label=r'$\frac{d^2f(x)}{dx^2} = 12x^2-30x+10$')
plt.title(r'$f''(x)$ plotted on $x\in[-1,4]$', fontsize=20)
plt.axhline(0, color='r')
plt.xlabel(r'x')
plt.ylabel(r'y')
plt.legend()
plt.savefig("exampleP3ddf.pdf")
plt.show()

plt.plot(x, df(x), label=r'$\frac{df(x)}{dx}=4x^3-15x^2+10x$')
plt.title(r'$\frac{df}{dx}$ plotted on $x\in[-1,4]$', fontsize=20)
plt.axhline(0, color='r')
plt.xlabel(r'x')
plt.ylabel(r'y')
plt.legend()
plt.savefig("exampleP3df.pdf")
plt.show()

plt.plot(x, f(x), label=r'$f(x) = x^2(x^2-5x+5)$') 
plt.title(r'$f(x)=x^2(x^2-5x+5)$ plotted on $x\in[-1,4]$', fontsize=20)
plt.xlabel(r'x')
plt.ylabel(r'y')
plt.legend()
plt.savefig("exampleP3.pdf")
plt.show()

import matplotlib
matplotlib.rcParams['text.usetex'] = True
import numpy as np
import matplotlib.pyplot as plt


def f(x): 
	return x[0]**2*(8.0*x[0]**2+3.0) + x[1]**2*(x[1]**2 + 1.0)
	
def df(x): 
	return np.array([8.0*x[0]**3+6.0*x[0],4.0*x[1]**3 + 2.0*x[1]])
def ddf(x): 
	return np.array([[24.0*x[0]**2+6.0, 0], [0, 12.0*x[1]**2+2.0]])


x0N = np.array([1,1])
x0alpha = np.array([1,1])
alpha = 0.13
# Fixed point iteration
def iter_(x, alpha): 
	return x-alpha*df(x)

# Newton's method
def newton(x): 
	return x-np.linalg.inv(ddf(x))@ df(x)
	
newton_iters = []
alpha_iters = []
#newton_iters.append(x0N)
#alpha_iters.append(x0alpha)
for i in range(10): 
	x0N = newton(x0N) # Calculating next step using Newton's method
	x0alpha = iter_(x0alpha, alpha) # Calculating next step using fixed point iteration
	newton_iters.append(x0N) # Appends calculated value to list
	alpha_iters.append(x0alpha) 
xalpha = np.zeros(10)
yalpha = np.zeros(10)
# Plots the log10 of the values 
for i in range(len(alpha_iters)): 
	xalpha[i] = np.log10(alpha_iters[i][0]) 
	yalpha[i] = np.log10(alpha_iters[i][1])
 
plt.plot(xalpha[0], yalpha[0], 'or')
plt.plot(xalpha[1], yalpha[1], 'ob')
plt.plot(xalpha[2], yalpha[2], 'oy') 
plt.plot(xalpha[3], yalpha[3], 'og') 
plt.plot(xalpha[4], yalpha[4], 'ok') 
plt.plot(xalpha[5], yalpha[5], 'oc') 
plt.plot(xalpha[6], yalpha[6], 'oc') 
plt.plot(xalpha[7], yalpha[7], 'oc') 
plt.plot(xalpha[8], yalpha[8], 'oc') 
plt.plot(xalpha[9], yalpha[9], 'om')  
plt.title(r'$Log_{10}(x_1)$ vs $Log_{10}(x_2)$ for the ten first steps, $\alpha=0.13$.', fontsize=20)
plt.xlabel(r'$log_{10}(x_1)$', fontsize=16) 
plt.ylabel(r'$log_{10}(x_2)$', fontsize=16)
plt.legend([r'$(x_1^{(1)},x_2^{(1)})$', r'$(x_1^{(2)},x_2^{(2)})$', r'$(x_1^{(3)},x_2^{(3)})$', r'$(x_1^{(4)},x_2^{(4)})$', r'$(x_1^{(5)},x_2^{(5)})$', r'$(x_1^{(6)},x_2^{(6)})$', r'$(x_1^{(7)},x_2^{(7)})$', r'$(x_1^{(8)},x_2^{(8)})$', r'$(x_1^{(9)},x_2^{(9)})$', r'$(x_1^{(10)},x_2^{(10)})$']) 
plt.savefig("prob7alpha.pdf")
plt.show()	
	

print("The first five values of series, using the Newton's method, is:") 
print(newton_iters[0]) 
print(newton_iters[1]) 
print(newton_iters[2]) 
print(newton_iters[3]) 
print(newton_iters[4]) 
print(newton_iters[5]) 






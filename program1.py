import json
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

xpoints = [1, 2, 3, 4, 5]
ypoints = [1, 4, 9, 16, 25]
plt.title("My first graph!")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")


plt.grid(axis='both', color='gray', linestyle='--', linewidth=0.5)
plt.plot(xpoints, ypoints, marker = 'o', color = 'red', linestyle = 'dashed', linewidth = 5, markersize = 10)

plt.show()
x= [1, 2, 3, 4, 5]
plt.plot(x, [i**3 for i in x], marker = 'o', color = 'red', linestyle = 'dashed', linewidth = 5, markersize = 10)
plt.show()
plt.bar(xpoints, ypoints, color = 'blue', width = 0.5)
plt.show()

xpoints=np.array([1,9])
ypoints=np.array([1,9])

plt.plot(xpoints, ypoints, marker = 'o', color = 'red', linestyle = 'dashed', linewidth = 5, markersize = 10)
plt.show()

plt.plot(xpoints)
plt.plot(ypoints)
plt.show()
x= {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)
print(y)

speed=[60,50,40,30,20,10]
x= np.mean(speed)
a= np.median(speed)
print(x)
print(a)
b= sp.stats.mode(speed)
print(b)
x= np.std(speed)
print(x)
x= np.var(speed)
print(x)
x= np.percentile(speed, 70)
print(x)
x= plt.hist(speed, bins=5)
plt.show()
def myfunc(x):
    return x**2 + 2*x + 1
result = myfunc(3)
print(result)


import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def F1(x,y):
    result = np.sin(x/2) + np.cos(2*y)
    return result
def F2(x,y):
    result = -abs(x-2)-abs((.5*y)+1)+3
    return result
x = np.arange(0,10,.01)
y = np.arange(0,10,.01)
print(x,y)
value=F2(x,y)

step = .01
net_steps = []

for i in range(0,100):
    x_start = random.randint(0,len(x)-1)
    x_start = x[x_start]
    y_start = random.randint(0,len(y)-1)
    y_start = y[y_start]
    print(x_start,y_start)
    done=False
    number_steps = 0
    while done==False:
        
        x_only_higher = round(F2(x_start+step,y_start),2)
        x_only_lower = round(F2(x_start-step,y_start),2)
        y_only_higher = round(F2(x_start,y_start+step),2)
        y_only_lower = round(F2(x_start,y_start-step),2)
        both_higher = round(F2(x_start+step,y_start+step),2)
        both_lower = round(F2(x_start-step,y_start-step),2)
        stagger_1 = round(F2(x_start-step,y_start-step),2)
        stagger_2 = round(F2(x_start+step,y_start+step),2)
        value = max([x_only_higher,x_only_lower,y_only_higher,y_only_lower,
                     both_higher,both_lower,stagger_1,stagger_2])
        if round(F2(x_start,y_start),2)>=value:
            done = True
        else:
            number_steps += 1
        if value == x_only_higher:
            x_start = x_start+step
        elif value == x_only_lower:
            x_start = x_start-step
        elif value == y_only_higher:
            y_start = y_start+step
        elif value == y_only_lower:
            y_start = y_start-step
        elif value == both_higher:
            y_start = y_start+step
            x_start = x_start+step
        elif value == both_lower:
            y_start = y_start-step
            x_start = x_start-step
        elif value == stagger_1:
            y_start = y_start+step
            x_start = x_start-step
        elif value == stagger_2:
            y_start = y_start-step
            x_start = x_start+step
    net_steps.append(number_steps)
mean = np.mean(net_steps)
print("mean ", mean)
std = np.std(net_steps)
print("std ",std)
print(value)

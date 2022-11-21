#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:25:18 2022

@author: Joshuabalbi
"""

import matplotlib.pyplot as plt
import time
import numpy as np
import pandas as pd
mydata1 = pd.read_csv("/Users/Joshuabalbi/Desktop/shootings.csv")

#From SQL DATA-----------------------------------------------------------------
state = ['CL','TX','FL','AZ','CO','GA']
unarmed = [57,38,27,16,9,15]
mental = [162,78,89,42,23,33]
race = [480,251,168,113,77,84]
flee = [445,258,214,144,85,102]
body_cam = [598,387,307,198,150,144]
total = [701,426,324,222,168,161]

for i in range(len(total)):
    unarmed[i] = unarmed[i]/total[i] * 100
    mental[i] = mental[i]/total[i] * 100
    race[i] = race[i]/total[i] * 100
    flee[i] = flee[i]/total[i] * 100
    body_cam[i] = body_cam[i]/total[i] * 100

plt.bar(state,unarmed)
plt.xlabel("States")
plt.ylabel("percent total in state")
plt.title("Unarmed Rates in top 6 states")
plt.show()
plt.bar(state,race)
plt.xlabel("States")
plt.ylabel("percent total in state")
plt.title("Race Rates in top 6 states")
plt.show()
plt.bar(state,mental)
plt.xlabel("States")
plt.ylabel("percent total in state")
plt.title("Signs of mental illness rates in top 6 states")
plt.show()
plt.bar(state,flee)
plt.xlabel("States")
plt.ylabel("percent total in state")
plt.title("Feeling rates in top 6 states")
plt.show()
plt.bar(state,body_cam)
plt.xlabel("States")
plt.ylabel("percent total in state")
plt.title("Inactive Body Camera rates in top 6 states")
plt.show()


#error-------------------------------------------------------------------------
def laplaceMechanism(x, epsilon):
    x =  np.random.laplace(0, 1.0/epsilon, 1)[0]
    return x

epsilon = [.5, 1 ,1.5 ,2 ,2.5, 3]

for j in range(10):
    unarmedep = []
    for i in range(len(total)):
        unarmedep.append(laplaceMechanism(race[0], epsilon[i]))
    plt.plot(epsilon,unarmedep)
plt.xlabel("Epsilon")
plt.ylabel("Error (%)")
plt.title("Race in california error")
plt.show()
        
for j in range(10):
    unarmedep = []
    for i in range(len(total)):
        unarmedep.append(laplaceMechanism(flee[0], epsilon[i]))
    plt.plot(epsilon,unarmedep) 
plt.xlabel("Epsilon")
plt.ylabel("Error (%)")
plt.title("Fleeing rates in california error")
plt.show()     
  
for j in range(10):
    unarmedep = []
    for i in range(len(total)):
        unarmedep.append(laplaceMechanism(unarmed[0], epsilon[i]))
    plt.plot(epsilon,unarmedep) 
plt.xlabel("Epsilon")
plt.ylabel("Error (%)")
plt.title("Unarmed rates in california error")
plt.show()

for j in range(10):
    unarmedep = []
    for i in range(len(total)):
        unarmedep.append(laplaceMechanism(body_cam[0], epsilon[i]))
    plt.plot(epsilon,unarmedep) 
plt.xlabel("Epsilon")
plt.ylabel("Error (%)")
plt.title("Inactive Body Cameras rates in california error")
plt.show()

for j in range(10):
    unarmedep = []
    for i in range(len(total)):
        unarmedep.append(laplaceMechanism(mental[0], epsilon[i]))
    plt.plot(epsilon,unarmedep) 
plt.xlabel("Epsilon")
plt.ylabel("Error (%)")
plt.title("Signs of mental Illness rates in california error")
plt.show()

#runtime-----------------------------------------------------------------------

for j in range(10):
    unarmedep = []
    runtime = []
    for i in range(len(total)):
        start_time = time.time()
        unarmedep.append(laplaceMechanism(race[0], epsilon[i]))
        runtime.append(time.time() - start_time)
    plt.plot(epsilon,runtime)
plt.ylim(0,.00007)
plt.xlabel("Epsilon")
plt.ylabel("Runtime (S)")
plt.title("Race in california error")
plt.show()


for j in range(10):
    unarmedep = []
    runtime = []
    for i in range(len(total)):
        start_time = time.time()
        unarmedep.append(laplaceMechanism(flee[0], epsilon[i]))
        runtime.append(time.time() - start_time)
    plt.plot(epsilon,runtime)
plt.ylim(0,.00007)
plt.xlabel("Epsilon")
plt.ylabel("Runtime (S)")
plt.title("Fleeing rates in california error")
plt.show()    


for j in range(10):
    unarmedep = []
    runtime = []
    for i in range(len(total)):
        start_time = time.time()
        unarmedep.append(laplaceMechanism(unarmed[0], epsilon[i]))
        runtime.append(time.time() - start_time)
    plt.plot(epsilon,runtime)
plt.ylim(0,.00007)
plt.xlabel("Epsilon")
plt.ylabel("Runtime (S)")
plt.title("Unarmed rates in california error")
plt.show()



for j in range(10):
    unarmedep = []
    runtime = []
    for i in range(len(total)):
        start_time = time.time()
        unarmedep.append(laplaceMechanism(body_cam[0], epsilon[i]))
        runtime.append(time.time() - start_time)
    plt.plot(epsilon,runtime)
plt.ylim(0,.00007)
plt.xlabel("Epsilon")
plt.ylabel("Runtime (S)")
plt.title("Inactive Body Cameras rates in california error")
plt.show()




for j in range(10):
    unarmedep = []
    runtime = []
    for i in range(len(total)):
        start_time = time.time()
        unarmedep.append(laplaceMechanism(mental[0], epsilon[i]))
        runtime.append(time.time() - start_time)
    plt.plot(epsilon,runtime)
plt.ylim(0,.00007)
plt.xlabel("Epsilon")
plt.ylabel("Runtime (S)")
plt.title("Signs of mental Illness rates in california error")
plt.show()

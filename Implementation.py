#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:25:18 2022

@author: Joshuabalbi
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
mydata1 = pd.read_csv("/Users/Joshuabalbi/Desktop/shootings.csv")

#From SQL DATA
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
plt.show()
plt.bar(state,race)
plt.show()
plt.bar(state,mental)
plt.show()
plt.bar(state,flee)
plt.show()
plt.bar(state,body_cam)
plt.show()


def laplaceMechanism(x, epsilon):
    x +=  np.random.laplace(0, 1.0/epsilon, 1)[0]
    return x

epsilon = [.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
unarmedep = np.eye(6, 10).tolist()
mentalep = np.eye(6, 10).tolist()
raceep = np.eye(6, 10).tolist()
fleeep = np.eye(6, 10).tolist()
body_camep = np.eye(6, 10).tolist()
for i in range(len(total)):
    for j in range(10):
        unarmedep[i][j] = laplaceMechanism(unarmed[i], epsilon[j])
        mentalep[i][j] = laplaceMechanism(mental[i], epsilon[j])
        raceep[i][j] = laplaceMechanism(race[i], epsilon[j])
        fleeep[i][j] = laplaceMechanism(flee[i], epsilon[j])
        body_camep[i][j] = laplaceMechanism(body_cam[i], epsilon[j])

plt.bar(state,unarmedep[0])
plt.bar(state,unarmedep[1])
plt.bar(state,unarmedep[2])
plt.bar(state,unarmedep[3])
plt.bar(state,unarmedep[4])
plt.bar(state,unarmedep[5])
plt.show()
plt.bar(state,raceep[0])
plt.bar(state,raceep[1])
plt.bar(state,raceep[2])
plt.bar(state,raceep[3])
plt.bar(state,raceep[4])
plt.bar(state,raceep[5])
plt.show()
plt.bar(state,mentalep[0])
plt.bar(state,mentalep[1])
plt.bar(state,mentalep[2])
plt.bar(state,mentalep[3])
plt.bar(state,mentalep[4])
plt.bar(state,mentalep[5])
plt.show()
plt.bar(state,fleeep[0])
plt.bar(state,fleeep[1])
plt.bar(state,fleeep[2])
plt.bar(state,fleeep[3])
plt.bar(state,fleeep[4])
plt.bar(state,fleeep[5])
plt.show()
plt.bar(state,body_camep[0])
plt.bar(state,body_camep[1])
plt.bar(state,body_camep[2])
plt.bar(state,body_camep[3])
plt.bar(state,body_camep[4])
plt.bar(state,body_camep[5])
plt.show()

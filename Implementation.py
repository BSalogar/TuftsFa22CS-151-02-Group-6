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

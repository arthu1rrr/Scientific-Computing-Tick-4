import numpy as np
import matplotlib.pyplot as plt
def pairs(n):
    vector = np.arange(n)
    np.random.shuffle(vector)
    return (vector[:n//2],vector[n//2:])
def kinetic_exchange(v,w):
    r = np.random.random(len(v))
    return r*(v+w),(1-r)*(v+w)
def gini(w):
    sigmatop = 0
    sigmabottom = 0
    length = len(w)
    w2 = np.sort(w)
    sigmatop = np.sum(np.arange(1, length+1) * w2)
    sigmabottom = np.sum(w2)
    gini = 2*(sigmatop/(length*sigmabottom)) - (1+(1/length))
    return gini
def mobility(v,w):
    quintiles_v = np.percentile(v, [20, 40, 60, 80])
    quintiles_w = np.percentile(w, [20, 40, 60, 80])
    quintile_indices_v = np.digitize(v, quintiles_v, right=True)
    quintile_indices_w = np.digitize(w, quintiles_w, right=True)
    movement = np.abs(quintile_indices_v - quintile_indices_w)
    movers = np.sum(movement > 1)
    return movers / len(v)

#functions defined in previous ticks

def incomeSim(N,T):
    w = np.ones(N)
    gs = np.zeros(T)
    ms = np.zeros(T)
    income = np.random.rand(N)
    for i in range(T):
        prevw = w
        m1,m2 = pairs(N)
        v,w2 = kinetic_exchange(w[m1], w[m2])
        w[m1] = v 
        w[m2] = w2
        gs[i] = (gini(w))
        w = w + income
        w = w * 1.06
        w = w*N / np.sum(w)
        if i > 0:
            ms[i] = mobility(w,prevw)
    return (w,gs,ms)
def UBISim(N,T):
    w = np.ones(N)
    gs = np.zeros(T)
    ms = np.zeros(T)
    income = np.random.rand(N)
    for i in range(T):
        prevw = w
        m1,m2 = pairs(N)
        v,w2 = kinetic_exchange(w[m1], w[m2])
        w[m1] = v 
        w[m2] = w2
        gs[i] = (gini(w))
        w = w + income + 0.2
        w = w * 1.06
        w = w*N / np.sum(w)
        if i > 0:
            ms[i] = mobility(w,prevw)
        
    return (w,gs,ms)
N = 50000
T =1000
_, gs_income, ms_income = incomeSim(N, T)
_, gs_ubi, ms_ubi = UBISim(N, T)
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs[0, 0].plot(range(T), gs_income, color='blue',linewidth = 0.5)
axs[0, 0].set_title("Gini over Time")
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("Gini Coefficient")


axs[0, 1].plot(range(T), ms_income, color='green',linewidth = 0.5)
axs[0, 1].set_title("Mobility over Time")
axs[0, 1].set_xlabel("Time")
axs[0, 1].set_ylabel("Mobility")


axs[1, 0].plot(range(T), gs_ubi, color='red',linewidth = 0.5)
axs[1, 0].set_title("Universal Basic Income: Gini over Time")
axs[1, 0].set_xlabel("Time")
axs[1, 0].set_ylabel("Gini Coefficient")


axs[1, 1].plot(range(T), ms_ubi, color='purple',linewidth = 0.5)
axs[1, 1].set_title("Universal Basic Income: Mobility over Time")
axs[1, 1].set_xlabel("Time")
axs[1, 1].set_ylabel("Mobility")

plt.tight_layout()
plt.show()

from simplyData import catchRSSIByAP, completeRssi
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

def data2array():
    fname = 'RSSI.txt'
    table = np.genfromtxt(fname, delimiter=" ")
    # file = open('RSSIGOOD.txt', 'rb')
    # table = [row.split(' ') for row in file]
    return table

def plot_wireframe(Z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X = np.linspace(-15, 15, 9)
    Y = np.linspace(-15, 15, 10)
    xx, yy = np.meshgrid(X, Y)
    ax.plot_wireframe(xx, yy, Z)

    plt.show()

def plot_surface(Z):
    fig = plt.figure()
    ax2 = fig.add_subplot(111,projection='3d')
    X2 = np.linspace(-20, 20, 9)
    Y2 = np.linspace(-20, 20, 10)
    xx2, yy2 = np.meshgrid(X2, Y2)
    surf = ax2.plot_surface(xx2, yy2, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
    fig.colorbar(surf, shrink=0.5, aspect=10)

    plt.show()

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    ret = np.append(ret[:1], ret[n-1:]/n)
    ret = np.append(ret, ret[-1:])
    return ret
    # return ret[n-1:]/n

def moving_average_iter(Z):
    for i in range(np.shape(Z)[0]):
        Z[i] = moving_average(Z[i])
    for j in range(np.shape(Z)[1]):
        Z[:,j] = moving_average(Z[:,j])
    return Z



if __name__ == "__main__":
    # Z = data2array()
    # moving_average_iter(Z)
    # moving_average_iter(Z)
    # moving_average_iter(Z)
    # moving_average_iter(Z)
    # plot(Z)
    rssi = catchRSSIByAP("room504.txt", "HUST_WIRELESS")
    rssi = completeRssi(rssi)
    print(rssi)
    rssi = np.reshape(rssi, 90)
    rssi = np.reshape(rssi, (10, 9))
    # rssi = rssi[4:,]
    print(rssi)

    plot_wireframe(rssi)
    plot_surface(rssi)



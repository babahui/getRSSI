import numpy as np

def catchRSSIByAP(filename, APName):
    i = 0
    rssi = [[]]
    with open(filename) as f:
        for line in f:
            if not line.strip():
                rssi.append([])
                i += 1
            elif APName in line:
                rssiValue = line.strip().split(' ')[0]
                rssi[i].append(int(rssiValue))
    numpy_rssi = rssi[:-1]
    return numpy_rssi

def completeRssi(rssi):
    for i in range(len(rssi)):
        if rssi[i] == []:
            rssi[i].append(-90)
        else:
            rssi[i] = [ np.mean(rssi[i]) ]
    return rssi

if __name__ == "__main__":
    rssi = catchRSSIByAP("room504.txt", "anchor_2")
    rssi = completeRssi(rssi)
    print(rssi) 
    print(len(rssi))

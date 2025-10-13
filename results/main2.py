import matplotlib.pyplot as plt, numpy as np, mytools as mt

files = [
    'I02V73',
    'I04V713',
    'I06V705',
    'I08V695'
    ]

data = {}

for file in files:
    data[file] = np.loadtxt('res/'+file+'.csv', delimiter = ';', encoding='utf-8-sig')

data['I02V73'] = data['I02V73'][15000:]
data['I02V73'][0:,1] += 0.02

data['I04V713'] = data['I04V713'][12000:]
data['I04V713'][0:,1] -= 0

data['I06V705'] = data['I06V705'][11200:]
data['I06V705'][0:,1] += 0.0025

data['I08V695'] = data['I08V695'][1500:-3000]
data['I08V695'][0:,1] += 0.002

maximos = {}

for file in files:
    maximos[file] = np.array(mt.get_maxs(data[file]))

for file in files:
    maximos[file] = maximos[file][1:]

for file in files:
    plt.plot(data[file][0:,0], data[file][0:,1])
    plt.plot(maximos[file][0:,0],maximos[file][0:,1], '.')
    plt.xlabel("tiempo, s")
    plt.ylabel("Amplitud, cm")
    plt.savefig('res/'+file+'.png')
    plt.cla()

periodos = {}
print('periodos')
for file in files:
    periodos[file] = 2 * np.average(maximos[file][1:,0]-maximos[file][0:-1,0])
    print(file+': ', periodos[file])

omegas = {}
print('omegas')
for file in files:
    omegas[file] = 2 * np.pi / np.average(maximos[file][1:,0]-maximos[file][0:-1,0])
    print(file+': ', omegas[file])

vmaximos = {}
print('valor maximo')
for file in files:
    vmaximos[file] = np.average(maximos[file][0:,1])
    print(file+': ', vmaximos[file])

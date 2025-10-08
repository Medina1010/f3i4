import matplotlib.pyplot as plt, numpy as np, mytools as mt

todo = 'I04V03_04_05_06_065_07_075_08_085_09_010_011_012'

files = [
        todo
    ]

data = {}

for file in files:
    data[file] = np.loadtxt('res/'+file+'.csv', delimiter = ';', encoding='utf-8-sig')

data[todo] = data[todo][0:50000]

files.append('V03')
data['V03'] = data[todo][200:1400]
files.append('V04')
data['V04'] = data[todo][2400:4000]
files.append('V05')
data['V05'] = data[todo][5000:7000]
files.append('V06')
data['V06'] = data[todo][8000:9500]
files.append('V065')
data['V065'] = data[todo][11000:13000]
files.append('V07')
data['V07'] = data[todo][17000:19000]
files.append('V075')
data['V075'] = data[todo][24000:24500]
files.append('V08')
data['V08'] = data[todo][28000:30000]
files.append('V085')
data['V085'] = data[todo][34000:36000]
files.append('V09')
data['V09'] = data[todo][41000:42000]
files.append('V10')
data['V10'] = data[todo][44000:45000]
files.append('V11')
data['V11'] = data[todo][46000:47000]
files.append('V12')
data['V12'] = data[todo][48500:49500]

maximos = {}

for file in files:
    maximos[file] = np.array(mt.get_maxs(data[file]))

for file in files:
    maximos[file] = maximos[file][1:]

for file in files:
    plt.plot(data[file][0:,0], data[file][0:,1])
    plt.plot(maximos[file][0:,0],maximos[file][0:,1], '.')
plt.savefig('res/Todo.png')

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

plt.cla()

files.remove(todo)

x = np.linspace(omegas['V03']-1, omegas['V12']+1,300)

w0 = 6.511494874454993
g = 0.22203050220625292
A=[]
for file in files:
    A.append(vmaximos[file]*np.sqrt((w0**2-omegas[file]**2)**2+(2*g*omegas[file])**2))

plt.plot(x,np.average(A)*np.sqrt((w0**2-x**2)**2+(2*g*x)**2)**(-1))

for file in files:
    plt.plot(omegas[file], vmaximos[file], '.')
plt.savefig('reso.png')

import matplotlib.pyplot as plt, numpy as np, mytools as mt

files = [
    'I00A5',
    'I02A5',
    'I04A5',
    'I06A5',
    'I08A5'
    ]

data = {}

for file in files:
    data[file] = np.loadtxt('res/'+file+'.csv', delimiter = ';', encoding='utf-8-sig')

data['I00A5'][0:,1] -= 0.008
data['I04A5'] = data['I04A5'][20:]
data['I08A5'] = data['I08A5'][10:]

maximos = {}

for file in files:
    maximos[file] = np.array(mt.get_maxs(data[file]))

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

omegas['I00'] = 6.511494874454993

gammas = {}
maximosl = {}
print('gammas')
for file in files:
    maximosl[file] = maximos[file]
    maximosl[file][0:,1] = np.log(maximosl[file][0:,1])
    
    coef = np.polyfit(maximosl[file][0:,0], maximos[file][0:,1], 1)
    gammas[file] = -coef[0]
    print(file+': ', gammas[file])

    x = np.linspace(maximosl[file][0,0],maximosl[file][-1,0])
    plt.plot(x, x*coef[0]+coef[1])

    plt.plot(maximosl[file][0:,0],maximosl[file][0:,1], '.')
    plt.xlabel("tiempo, s")
    plt.ylabel("logaritmo de la Amplitud")
    plt.savefig('res/'+file+'l.png')
    plt.cla()

print('omega esperado')
for file in files:
    print(file+': ', (omegas['I00']**2-gammas[file]**2)**(1/2))

print('omega resonancia esperado')
for file in files:
    print(file+': ', (omegas['I00']**2-2*gammas[file]**2)**(1/2))


plt.plot(gammas['I00A5']**2, omegas['I00A5']**2,'b.')
plt.plot(gammas['I02A5']**2, omegas['I02A5']**2,'b.')
plt.plot(gammas['I04A5']**2, omegas['I04A5']**2,'b.')
plt.plot(gammas['I06A5']**2, omegas['I06A5']**2,'b.')
plt.plot(gammas['I08A5']**2, omegas['I08A5']**2,'b.')

cosita = np.array([
[gammas['I00A5']**2, omegas['I00A5']**2],
[gammas['I02A5']**2, omegas['I02A5']**2],
[gammas['I04A5']**2, omegas['I04A5']**2],
[gammas['I06A5']**2, omegas['I06A5']**2],
[gammas['I08A5']**2, omegas['I08A5']**2,]])

cositacoef = np.polyfit(cosita[1:-1,0],cosita[1:-1,1],1)

print('w0: ', (cositacoef[1])**(1/2))

x = np.linspace(cosita[0,0], cosita[-1,0])
plt.plot(x, x*cositacoef[0]+cositacoef[1])

plt.savefig('omega_corr.png')

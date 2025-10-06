def get_maxs(data, subida = False):
    Maximos = []
    L = data[0]
    for v in data:
        if L[1] < v[1] and subida:
            L = v
        if L[1] > v[1] and subida:
            subida = False
            Maximos.append([(v[0]-(data[2,0]-data[1,0])+L[0])/2,L[1]])
        if L[1] > v[1] and not subida:
            L = v
        if L[1] < v[1] and not subida:
            subida = True
            Maximos.append([(v[0]-(data[2,0]-data[1,0])+L[0])/2,-L[1]])
    return Maximos

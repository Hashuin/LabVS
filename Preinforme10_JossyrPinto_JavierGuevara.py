import numpy as np 
def utilidad():
    utilidad = np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])
    return utilidad
def ejercicio1(utilidad):
    cant = len(utilidad)
    prom1= (utilidad[cant-1]+utilidad[cant-2])/2
    prom2= (utilidad[0] + utilidad[1])/2
    dif = prom1 - prom2
    return dif

def ejercicio2(utilidad):
    cant = len(utilidad)
    dif = (utilidad[5] - (utilidad[9]))
    return dif

def ejercicio3(utilidad):
    orden = np.sort(utilidad)
    mediana = (orden[4]+ orden[5])/2
    return mediana

def ejercicio4(utilidad):
    mediana = (ejercicio3(utilidad))
    med = 0
    cant = len(utilidad)
    for i in range(0,cant):
        med += utilidad[i]
    prom = med/cant
    print("La media es: " + str(prom) + " y la mediana es: " + str(mediana))
    
def ejercicio5(utilidad):
    acum = 0
    cant = len(utilidad)
    for i in range(0, cant):
        acum += utilidad[i]
        
    porc = 0
    a = 2007
    for i in range(0, cant):
        porc = (utilidad[i]*100)/acum
        a += 1
        print("El porcentaje que aporta el año " + str(a) + " al acumulado es: " + str(porc) + "%")

def ejercicio6(utilidad):
    cant = len(utilidad)
    deficit = (utilidad[8] - (utilidad[9]))
    return deficit

def ejercicio7(utilidad):
    cant= len(utilidad)
    a = 2007
    for i in range(0, cant-1):
        d = utilidad[i] - utilidad[i+1]
        deficit = (d*100/utilidad[1])
        a += 1
        print(str("El deficit del año" + str(a) + " es " + str(deficit)))

utilidad = utilidad()
print("La diferencia de la media es: " + str(ejercicio1(utilidad)))
print("La diferencia del mayor y el menor es: " + str(ejercicio2(utilidad)))
ejercicio5(utilidad)
print("El decifit del año 2017 en comparación al anterior es: " + str(ejercicio6(utilidad)) + " Millones de COP")
ejercicio7(utilidad)
ejercicio4(utilidad)     
print("La mediana es " + str(ejercicio3(utilidad)))
import numpy as np

def generador(_min, _max):
    return (np.random.randint(_min, _max, size = 48).reshape(4,12))

ingresos = generador(100, 180)
egresos = generador(60, 130)

meses = np.array("enero", "febrero", "marzo", "abril","mayo","junio","julio","julio","agosto","septiembre","octubre", "noviembre", "diciembre")
ciudades = np.array("Giron","Piedecuesta","Bucaramanga", "floridablanca")

def imprimir(arr):
    txt = ""
    for j in range(0,12):
        txt += meses[j]+ " / "
    print(txt, "\n")


    for i in range(0,4):
        txt = ""
        for j in range(0,12):
            txt += str(arr[i,j])
            
            if (arr[i,j] >= 100) or (arr[i,j] <= -10):
                txt += "   "
            elif (arr[i,j] >= 10) or (arr[i,j] >= -10) and (arr[i.j] < 0):
                txt += "    "
            else:
                txt += "     "
        print(txt + ciudades[i])
    print("\n")
    
    
    
    
    
print("ingresos")
imprimir(ingresos)

print("egresos")
imprimir(egresos)



def calculador(arrA, arrB):
    arrR = arrA - arrB
    return arrR


print("ganancias")
ganancias = calculador(ingresos, egresos)
imprimir(ganancias)


def mejor_ciudad(arr):
    
    mejor = 0
    mejorGan = 0
    
    
    for i in range(0,4):
        gan = 0;
        for j in range (0,12):
            gan += arr[i,j]
        if gan > mejorGan:
            mejorGan = gan
            mejor = 1
    print( "la ciudad con mejores ganancias fue: ")


def peor_ciudad(arr):
    
    peor = 0;
    peorGan = 10000;
    
    for i in range(0,4):
        gan = 0;
        for j in range(0,12):
            gan += arr[i,j]
        if gan < peorGan:
            peorGan = gan
            peor = i
    print("la ciudad con peores ganancias fue: ", ciudades[peor], "con ganancias de: ", str(peorGan))
    
    
    



def mejor_mes(arr):
    
    best = 0;
    for i in range(0,4):
        gan = -1000;
        for j in range(0,12):
            if arr[i,j] > gan:
                gan = arr [i,j]
                best = j
        print("el mejor mes de: ", ciudades[i], "fue ", meses[best] )
        
        
        
    
    
def imprimir_pesonalizado(arr, stt, end):
    
    txt = ""
    
    for j in range(stt, end):
        txt += meses[j]+"/"
    print(txt, "\n")
    
    for i in range(0,4):
        txt =""
        for j in range(stt, end):
            
            txt += str(arr[i,j])
            
            if (arr[i,j] >= 100) or (arr[i,j] <= -10):
                txt += "   "
            elif (arr[i,j] >= 10) or (arr[i,j] >= -10) and (arr[i.j] < 0):
                txt += "    "
            else:
                txt += "     "
                
        print(txt + ciudades[i])

promSem = [110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,
            117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,
            122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,112.29,105.42,110.67,107.73,105.76,107.85]
promSem.sort()

print(promSem)
#Diferencia menor y mayor
dif = promSem[0]-promSem[-1]
print(dif)
#Promedio
suma = 0
for presion in promSem:
    suma += presion
media = suma/len(promSem)

print(media)
#Comparar mediana y media
mediana = (promSem[25] + promSem[26])/2
print(mediana)

Comparacion=  "la media es mayor debido a que los valores se encuentran más concentrados a la izquierda"

print(Comparacion)

promedio1 = sum(promSem)/(len(promSem))
lista1 = [] 
lista2 = [] 
for i in promSem:
    if i > promedio1:
        posicion = promSem.index(i)
        lista1.append(posicion+1)
    else:
        posicion = promSem.index(i)
        lista2.append(posicion+1)

print("Las semanas con datos mayores al promedio fue: ",lista1)
print("las semanas con datos menor al promedio fue: ",lista2)
print("")


#6.1 promedio temperatura
Temperatura = [(element*510)/(17.16*8.314472) for element in promSem ]

suma = 0
for i in Temperatura:
    suma += i
media = suma/len(Temperatura)
print("La temperatura promedio semanal es: ", media)
#6.2 derivación estandar

sumatoria = 0
for h in range(len(Temperatura)):
    sumatoria += (Temperatura[h]-media)**2
    
des = (sumatoria/len(Temperatura))**(1/2)
print("La desviacion estandar es: ", des)
#Semanas por encima y por debajo del promedio de la temperatura




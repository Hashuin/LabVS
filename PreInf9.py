
#Distancia Euclidiana
x1= int(input("Ingrese la coordenada x1: "))
x2= int(input("Ingrese la coordenada x2: "))
y1= int(input("Ingrese la coordenada y1: "))
y2= int(input("Ingrese la coordenada y2: "))
print("La distancia euclidiana es: " + str((((x2-x1)**2)+((y2-y1)**2))**(1/2)))
#%% 
#Invertir un numero dado
num = int(input("Ingrese un número: "))
inver = 0
while num > 0:
    residuo = num % 10
    inver = (inver * 10) + residuo
    num //=10
print('El inverso del numero es:', inver)
#%%
##Notas del estudiante
n1 = float(input('Ingrese la nota 1: '))
n2 = float(input('Ingrese la nota 2: '))
n3 = float(input('Ingrese la nota 3: '))
n4 = float(input('Ingrese la nota 4: '))
n5 = float(input('Ingrese la nota 5: '))

n1 = (n1*(0.15))
n2 = (n2*(0.2)) 
n3 = (n3*(0.15))
n4 = (n4*(0.3))
n5 = (n5*(0.2))
ntotal = (n1+n2+n3+n4+n5)
str(print(ntotal))
if ntotal<2.0: 
    print(str('El estudiante no puede habilitar'))
elif ntotal<3.0:
        print(str('Usted ha reprobado'))
elif ntotal>4.5:
    print(str('Felicitaciones por la nota que ha sacado'))
elif ntotal>=3.0:
    print(str('Usted ha aprobado'))
#%%
## Seriación Gráfica

n= int(input('Escriba el numero de filas: '))

empty_list = []
for x in range(1, n+1 , 1):
  empty_list.append(x)
  print(empty_list)

#%% 
#Punto Numero 7 ejemplos.
#Funcion sin parametros  de  entrada y sin retorno
def function():
    a= 2
    b= 2
    print("La suma es: ",a + b)

function()
#%%
#Funcion sin parametro de entrada y con retorno
def function():
    a = 2
    b = 2
    return a/b
c = function()
print('El resultado: '+ str(c + 22))
#%%
#Funcion con parametros de entrada y sin retorno
def lolsito (n1, n2, n3):
    CuadradoTotal = (n1+n2+n3)**2
    print("El cuadrado de la suma de los numeros es: " + str(float(CuadradoTotal)))
lolsito(5.2, 4.0, 12.2)
#%%
#Punto 7.
#Funciones Definidas por el usuario
def Funcion(nombre, apellido): 
    nombre_completo= nombre + " " + apellido 
    print(str(nombre_completo))
Funcion("Jossyr","Pinto")
#%%
#Funciones nativas
def area_triangulo(base, altura):
    at= (base * altura)/2
    return at
area_triangulo(5,4)
#%%
#Ejemplo2.
def media():
    media = (a + b) / 2
    print(f"La media de " ,a, "y" ,b, "es: ",media)
    return

a = 3
b = 5
media()
#%%
#Ejemplo3.
def calcula_media(*args):
    total= 0
    for i in args:
        total += 1
        resultado= total/ len(args)
        return resultado
a,b,c = 3, 5, 10
media = calcula_media(a, b, c)
print("La media de",a,",",b," y ",c,"es: ",media,)
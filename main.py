
a = int(input ("Ingrese el valor de a: "))
b = int(input ("Ingrese el valor de b: "))
c = int(input ("Ingrese el valor de c: "))

d = (b*2)-(4*a*c)

if d == 0 :
    print("X1 y X2 equivalen a "+ str(-b/(2*a)))
elif d>0 :
    print("X1 es igual a: " + str(((-b+(d**(1/2)))/(2*a))))
    print("X2 es igual a: " + str(((-b-(d**(1/2)))/(2*a))))

else: 
    print("No tiene raices dentro del dominio de los reales")
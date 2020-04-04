horas = float(input("numero de horas: "))
print("moto(1) carro(2) camioneta(3)")
tipo = int(input("tipo de vehiculo: "))
valorT = 0

if tipo==1 or horas < 1.25:
    valorT = 0
else :
    if tipo==2:
        valorT=int(horas)*2000
        if (horas*100)%100>=25 and horas > 2:
            valorT=valorT+2000
    if tipo==3:
        valorT=int(horas)*2500
        if (horas*100)%100>=25 and horas > 2:
            valorT=valorT+2500
    if tipo<1 or tipo>3:
        print("tipo de vehiculo no valido")
    if horas>=4.25:
        valorT=valorT/2
print(valorT)
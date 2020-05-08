# ----- Paquetes y librerías ----- #

import random

# -----Funciones----- #

# 13
def combinar(ponderado, simbolos):
    baraja = {} 
    for element in simbolos:    
        for key in ponderado:
            baraja[key+element] = ponderado[key]
        
    return baraja


# 14
def revolver(combinatoria):
    combi = combinatoria.copy()
    llaves = [i for i in combinatoria]
    llaves = random.sample(llaves, len(llaves))
    baraja = {}
    for element in llaves:
        for value in combi:
            if value[0] == element[0]:
                baraja[element] = combi[value]
            elif value == 1 and element[0] == "A":
                baraja[element] = combi[value]

    return baraja


def repartir(baraja_usuario ,carta):
    baraja_copia = carta.copy()
    cartasBaraja = [key for key in baraja_copia]
    cartasRepartidas = []
    
    if len(baraja_usuario) == 0 :
        for i in range(2):
            cart = random.choice(cartasBaraja)
            cartasRepartidas.append(cart)
            del baraja_copia[cart]
    else:
        cartasRepartidas = baraja_usuario
        cart = random.choice(cartasBaraja)
        cartasRepartidas.append(cart)
        del baraja_copia[cart]
        
    return cartasRepartidas


def sumar_cartas(cartas):
    blackjack = False
    AS = False
    
    suma = 0

    for carta in cartas:
        for cart in baraja:
            if carta==cart :
                suma += baraja[cart]
    
    for elemento in cartas:
        for valor in elemento:
            if valor == "A":
                AS = True
            if valor == "J" or valor == "K" or valor == "Q" :
                blackjack = True
                
    if (blackjack and AS) and len(cartas)==2 :
        suma = 21
    
    if AS == True and blackjack == False:
        suma21 = suma-1
        if (suma21+11) <= 21 :
            suma=suma21+11
            
    return suma


def mostrar(lista):
    if sumar_cartas(lista) > 21 :
        return "Has perdido"
    else:
        return ("Las cartas que posee son: " + str(lista) + " que suman " + str(sumar_cartas(lista)))
    
    
def tomar_cartas_jugador(jugador):
    
    print("\n" + "Jugador: " + str(mostrar(jugador)))
    if sumar_cartas(jugador) == 21 :
        return jugador
    tomar = input("¿Quiere tomar otra carta? ")
    cartas_jugador = jugador
    while (tomar == "si" or tomar == "yes") :     
        
        cartas_jugador = repartir(cartas_jugador, baraja)
        print(mostrar(cartas_jugador))  
        
        if mostrar(cartas_jugador) == "Has perdido":
            break
        tomar = input("¿Quiere tomar otra carta? ")

    return cartas_jugador
    
def tomar_cartas_tallador(tallador):
    
    print("\n" + "Tallador: " + str(mostrar(tallador)))
    if sumar_cartas(tallador) == 21 :
        return tallador
    
    cartas_tallador = tallador
    while (sumar_cartas(cartas_tallador) < sumar_cartas(cartas_jugador) 
           or sumar_cartas(cartas_tallador) == sumar_cartas(cartas_jugador)) :
        
        cartas_tallador = repartir(cartas_tallador, baraja)
        
        if sumar_cartas(cartas_tallador) > 21:
            break
        print("\n" + "Tallador: " + str(mostrar(tallador)))
        
    return cartas_tallador
    
def ganador(jugador, tallador):
    if mostrar(cartas_jugador) == "Has perdido" :
        return "El tallador gana"
    elif sumar_cartas(jugador) > sumar_cartas(tallador):
        return "El jugdador gana"
    elif sumar_cartas(jugador) == 21 :
        return "El jugador gana"
    elif sumar_cartas(tallador) == 21 :
        return "El tallador gana"
    elif sumar_cartas(tallador) > 21 :
        return "El jugador gana"
    elif sumar_cartas(jugador) < sumar_cartas(tallador) :
        return "El tallador gana" 


def new_partida(part):
    cartas_jugador = []
    cartas_tallador = []
    ganadas = ganada
    perdidas = perdida
    partidas_jugadas = 1
    while part == "YES" :
        ponderado = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "J": 10, "Q": 10, "K": 10}
        simbolos = ["C", "D", "T", "P"]
        baraja = combinar(ponderado, simbolos)
        baraja = revolver(baraja)
        cartas_jugador = repartir(cartas_jugador, baraja)
        cartas_tallador = repartir(cartas_tallador, baraja)
        
        cartas_jugador = tomar_cartas_jugador(cartas_jugador)
        cartas_tallador = tomar_cartas_tallador(cartas_tallador)
        
        winner = ganador(cartas_jugador,cartas_tallador)
        print(ganador(cartas_jugador,cartas_tallador))
        partidas_jugadas += 1
        if winner == "El jugador gana":
            ganadas += 1
        else:
            perdidas += 1
            
        part = input("¿Quiere jugar otra partida? ")
        
    print("Jugaste " + str(partidas_jugadas) + " de las cuales ganaste " + str(ganadas) + " y perdiste " + str(perdidas))
        
        
# -----Principal----- #

# 11
ponderado = {"A": 1,
             "2": 2,
             "3": 3,
             "4": 4,
             "5": 5,
             "6": 6,
             "7": 7,
             "8": 8,
             "9": 9,
             "J": 10,
             "Q": 10,
             "K": 10}

# 12
simbolos = ["C", "D", "T", "P"]

# 13
baraja = combinar(ponderado, simbolos)

baraja = revolver(baraja)


# 14 - 15
cartas_jugador = []
cartas_tallador = []

cartas_jugador = repartir(cartas_jugador, baraja)
cartas_tallador = repartir(cartas_tallador, baraja)


cartas_jugador = tomar_cartas_jugador(cartas_jugador)
cartas_tallador = tomar_cartas_tallador(cartas_tallador)



winner = print(ganador(cartas_jugador,cartas_tallador))

partidas_jugadas = 1
ganada = 0
perdida = 0
if winner == "El jugador gana":
    ganada += 1
else:
   perdida += 1

game = input("¿Quiere jugar otra partida? ")
if game=="YES":
    new_partida(game)
else:
  print("Jugaste " + str(partidas_jugadas) + " de las cuales ganaste " + str(ganada) + " y perdiste " + str(perdida))
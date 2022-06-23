import random

opcion = ["Piedra", "Papel", "Tijera"]
sistema = random.choice(opcion)

jugador = False
cpu_puntaje = 0
jugador_puntaje = 0

while True:

    jugador = input("Ingresa una opcion: Piedra/Papel/Tijera: ").capitalize()
   
  
    if jugador == sistema:
        print ("Es un empate")
    elif jugador == "Piedra" and sistema == "Tijera":
        print ("¡Has ganado!")
        jugador_puntaje+=1
    elif jugador == "Piedra" and sistema =="Papel":
        print ("Has perdido. Intentalo de nuevo")
        cpu_puntaje+=1
    elif jugador == "Tijera" and sistema == "Papel":
        print ("¡Has ganado!")
        jugador_puntaje+=1
    elif jugador == "Tijera" and sistema == "Piedra":
        print ("Has perdido. Intentalo de nuevo")
        cpu_puntaje+=1
    elif jugador == "Papel" and sistema == "Piedra":
        print ("¡Has ganado!")
        jugador_puntaje+=1
    elif jugador == "Papel" and sistema == "Tijera":
        print ("Has perdido. Intentalo de nuevo")
        cpu_puntaje+=1
    elif jugador == "Fin":
        print (f"El juego ha terminado, estos son los resultados: \n jugador: + {jugador_puntaje}  \n computadora: + {cpu_puntaje}") 
        break
    else:
       print ("La opcion ingresada no es valida, por favor ingresa 'Piedra', 'Papel', 'Tijera' o 'fin'")
   
        
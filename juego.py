# Juego de números aleatorios en Python
# Descripción: Habrán dos juadores: Jugador a y jugador b, cada jugador tiene su turno
# cuando el jugador presione "Enter" el programa genera un número aleatorio, el jugador que
# llegue primero a la meta gana
# IMPORTANTE: Colocar el rango de los números aleatorios y colocar la meta
import random

def aleatorio(rangAleatorio):
    a=random.randrange(rangAleatorio) 
    print("Número generado: "+str(a))
    return a
def iniciaJuego():
    meta = 25 # La meta a la que se quiere llegar
    rangAleatorio = 10 # Colocamos el intervalo del número aleatorio que se va a generar 1->10
    puntajeA = 0 #No tocar, solo es puntuación
    puntajeB = 0 #No tocar, solo es puntuación
    flag = True #No tocar, es una variable para intercalar entre JugadorA y JugadorB
    while(puntajeA < meta and puntajeB < meta):
        if(flag):
            flag = False
            a = input('El turno del jugador A')
            puntajeA = puntajeA + aleatorio(rangAleatorio)
            print("Puntaje: "+str(puntajeA))
        else: 
            flag = True
            a = input('El turno del jugador B')
            puntajeB = puntajeB + aleatorio(rangAleatorio)
            print("Puntaje: "+str(puntajeB))
            
    if puntajeA >= meta: print("GANA JUGADOR A, con: "+str(puntajeA)+" puntos")
    if puntajeB >= meta: print("GANA JUGADOR B, con: "+str(puntajeB)+" puntos")

iniciaJuego()

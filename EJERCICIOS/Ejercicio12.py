#Crear un juego donde se pide por consola un número entre 1 y 10, que se restará de un número 
# definido dentro del programa y después la "IA" restará otro 
# número comprendido entre el 1 y el 10, hasta que el resultado sea 0.
#Mostrar por consola tanto el resultado de la resta del número del jugador como el de la "IA" así como al llegar a 0 el número quien es el ganador 
#(aquella persona que con su resta ha conseguido el 0).
import random
def game():
    gameNum=20
    inGame=True
    currentNum=0
    playerNum=int(input("Introduce un número del 1 al 10 "))
    
    if playerNum>10 or playerNum<1:
        print("El número introducido es invalido")
        return
    
    while inGame:
        currentNum=gameNum-playerNum
        iaNum=random.randint(1,currentNum)       
        
        if currentNum==0:
            print("El jugador gana")
            inGame=False
        else:
            print("Resultado jugador:",currentNum)
        
        currentNum=gameNum-iaNum
        
        if currentNum==0:
            print("La IA gana")
            inGame=False
        else:
            print("Resultado IA:",currentNum)
            

game()

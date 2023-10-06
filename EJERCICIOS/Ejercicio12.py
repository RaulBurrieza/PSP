
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

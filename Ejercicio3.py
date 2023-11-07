
list=[]

def createList(list):
    userInput=""
    while userInput!="x": 
        print("Introduce un número")
        param=input()
        if param.isnumeric():
            print("Perfecto!!")
            list.append(param)
        else:
            print("Error")
        print("Deseas introducir otro?")
        print("z-----Si")
        print("x-----No")
        userInput=input() 
    print(list)

def orderList(list):
    list.sort()    
    print("Aqui tienes tu lista ordenada ")
    print(list)
    
createList(list)
orderList(list)      
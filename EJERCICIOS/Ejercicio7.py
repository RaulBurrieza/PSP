mytuple=["Pepe","Jose","Federico","Martin"]

def modifyTuple():
    name=input("Que nombre deseas modificar ")
    newName=input("Introduce el nuevo nombre ")
    for i, checkedName in enumerate(mytuple):
        if checkedName==name:
            mytuple[i]=newName
    print(mytuple)

modifyTuple()
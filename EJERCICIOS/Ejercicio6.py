plants=[{'Nombre': 'Rosa', 'Ciudad': 'Barcelona', 'Dias entre riego': 5, 'Tamaño en cm': 10}]
def createPlant():
    plant={}
    name=input("Introduce el nombre de la planta ")
    city=input("Introduce la ciudad de la planta ")
    btwWater=input("Introduce los dias de riego que necesita la planta ")
    size=input("Introduce el tamaño de la planta en cm ")
    
    if name and city:
        plant["Nombre"]= name
        plant["Ciudad"]= city
    else:
        print("Los valores nombre y ciudad deben estar rellenos")
    
    if btwWater.isnumeric and size.isnumeric:
        plant["Dias entre riego"]= int(btwWater)
        plant["Tamaño en cm"]= int(size)
    else:
        print("Debes introducir un valor numerico")
    plants.append(plant)
    
def showPlants():
    x=1
    for i in plants:
        print("Planta",x,i)
        x+=1

def modifyPlants():
    index=int(input("Que planta deseas modificar?(numero)"))+1
    
    newName=input("Introduce el nuevo nombre de la planta ")
    newCity=input("Introduce la nuevo ciudad de la planta ")
    newbtwWater=input("Introduce los nuevos dias de riego que necesita la planta ")
    newSize=input("Introduce el nuevo tamaño de la planta en cm ")
    
    newPlant={"Nombre":newName ,"Ciudad":newCity ,"Dias entre riego":newbtwWater ,"Tamaño en cm":newSize}
    plants.insert(index,newPlant)
    print(plants)

createPlant()
showPlants()
modifyPlants()

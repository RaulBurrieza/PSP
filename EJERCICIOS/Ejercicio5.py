
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
    print(plant)

createPlant()
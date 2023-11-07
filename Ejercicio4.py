def openScript():
    ex=input("Que ejercicio de python quieres abrir?(numero)")
    exec(open("Ejercicio"+ex+".py").read())

openScript()
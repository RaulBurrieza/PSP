course={"Flauta","Guitarra","Batería","Viola","Violín",}

def showList():
    print (course)

def addItem():
    item=input("Que instrumento deseas añadir ")
    course.add(item)
    print(course)

def deleteItem():
    item=input("Que instrumento deseas borrar ")
    if item in course:
        course.remove(item)
    else:
        print("El instrumento no ha sido encontrado")
    print(course)

showList()
addItem()
deleteItem()

def Area(b,h):
    area = b*h/2
    if b <= 0 or h <= 0 :
        print("Error")
    else:
        print ("El area del triangulo es",area)

print("Introduce la base de un triangulo")
b = int(input())
print("Introduce la altura de un triangulo")
h = int(input())
Area(b,h)
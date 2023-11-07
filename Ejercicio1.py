def ageCalculate(userName,userAge):
    finalAge=userAge*365
    print("Hola!!" ,userName, "has vivido " , finalAge, "dias")


print("Hola!! ¿Cuál es tu nombre?")
userName=input()
print("¿Cuantos años tienes?")
userAge=int(input())
ageCalculate(userName,userAge)   
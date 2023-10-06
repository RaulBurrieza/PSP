def checkMail():
    email=input("Introduce tu email")
    parts=email.split("@")
    
    if "@" in email:
        domainParts=parts[1].split(".")
        
        if "." in email:
            if len(domainParts[1]) > 3:
                print("dominio demasiado largo")
        else:
            print("El dominio no es correcto")
            
    else:
        print("El email no contiene arroba")
        
    print("Mail Valido")

checkMail()
def validar_email(email):
    if email.count("@") != 1:
        return False

    parte1, parte2 = email.split("@")

    if len(parte1) < 1:
        return False

    if "." not in parte2:
        return False

    parte_meio, *resto = parte2.split(".")

    if len(parte_meio) < 1:
        return False

    if len(resto[-1]) < 2:
        return False

    return True

print(validar_email("teste@email.com"))     
print(validar_email("a@b.co"))              
print(validar_email("@email.com"))          
print(validar_email("teste@email"))         
print(validar_email("testeemail.com"))      
print(validar_email("teste@.com"))          
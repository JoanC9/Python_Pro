import random

caracteres_contrasena = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
longitud_contrasena = int(input('Escriba la longitud que quiera la contraseña: '))

contrasena = ""

for i in range(longitud_contrasena):
    
    contrasena += random.choice(caracteres_contrasena)
    
print(f'Hola esta es tu contraseña {contrasena}')
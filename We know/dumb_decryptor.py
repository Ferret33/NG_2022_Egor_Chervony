enterline= input("Enter line to encrypt: ").lower()
translate="abcdefghijklmnopqrstuvwxyz"
decryptkey = int(input("Enter decrypt key (ROT13 - 13): "))
treanstaedline=""
for element in enterline:
    if element in translate:
        treanstaedline += (translate[translate.index(element)-decryptkey])
    else:
        treanstaedline += element
print("===================================================")
print(treanstaedline)
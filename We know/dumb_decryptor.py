enterline= input("Enter line to encrypt: ").lower()
translate="abcdefghijklmnopqrstuvwxyz"
treanstaedline=""
for element in enterline:
    if element in translate:
        treanstaedline += (translate[translate.index(element)-13])
    else:
        treanstaedline += element
print("===================================================")
print(treanstaedline)
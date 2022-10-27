enterline= input("Enter line to encrypt: ")
translaterline=str.maketrans('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                             'nopqrstuvwxyzabcdefghijklm NOPQRSTUVWXYZABCDEFGHIJKLM')
print("=========================================================")
print (enterline.translate(translaterline))
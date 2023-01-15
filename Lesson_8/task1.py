from hashlib import sha256
import itertools
from rich.console import Console
console = Console()
Userhash = input("Enter hash SHA256: ")
length = 1
dictionary="abcdefghijklmnopqrstuvwxyz1234567890 "
if len(Userhash) == 64:
    with console.status("Cracking hash...", spinner="arc"):
        while True:
            for letters in itertools.product(dictionary,repeat=length):
                    passwd="".join(letters)
                    if Userhash == sha256(passwd.encode()).hexdigest():
                        print(Userhash+" : "+ passwd)
                        quit()
            length+=1
else:
    print("Wrong hash!")

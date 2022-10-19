entersec = int(input("Enter the number of seconds: "))
seconds = entersec%60
minutes = (entersec//60)%60
hours = ((entersec//60)//60)%24
days = ((entersec//60)//60)//24
print(str(days)+":"+str(hours)+":"+str(minutes)+":"+str(seconds))

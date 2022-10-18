import time

introducedSeconds = int(input("Enter the number of seconds: "))
print(time.strftime("%d, %H:%M:%S", time.gmtime(0+introducedSeconds)))
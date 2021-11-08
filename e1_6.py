number = int(input())
if(number <= 0):
    print("error")
else:
    isPair = False
    lastNum = False
    if(number % 2 == 0):
        isPair = True
    if(number % 10 == 5):
        lastNum = True
if(isPair):
    print("Это чилсо чётное")
else:
    print("Это число не является чётным")

if(lastNum):
    print("Последняя цифра 5")
else:
    print("Последняя цифра не 5")
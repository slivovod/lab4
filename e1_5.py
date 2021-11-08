#если я правильно понял условие задачи, то количество часов <= 11, минут <= 59, секунд <= 59

hour = float(input())
min = float(input())
second = float(input())

corner = hour * 30 + min/2 + second/120
print(corner)
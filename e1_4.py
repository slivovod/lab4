sec = int(input())
hh = 3600
mm = 60
hour = 0
min = 0
while(sec - hh >= 0):
    hour += 1
    sec -= hh
while(sec - mm >= 0):
    min += 1
    sec -= mm
print("hour: ", hour)
print("min: ", min)
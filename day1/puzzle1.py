import math
sum = 0
file = open("input.txt", "r")
for line in file:
    fuel = math.floor(int(line) / 3) -2
    sum = sum + fuel

print (sum)

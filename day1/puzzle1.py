import math
import numpy as np

def calculate_fuel(amount):
    return math.floor(amount / 3) -2 


sum = 0
file = open("input.txt", "r")
for line in file:
    fuel = calculate_fuel(int(line))
    sum = sum + fuel

print ("first answer ",sum)

fuels = []
file = open("input.txt", "r")
for line in file:
    fuel = calculate_fuel(int(line))
    total_fuel = fuel
    while fuel > 0:
        fuel = calculate_fuel(fuel)
        if fuel > 0:
            total_fuel = total_fuel + fuel

    fuels.append(total_fuel)

print(fuels)
print("second answer ", np.sum(fuels))


from importer import Importer
import time

#Start Timer
start = time.time()

#Input
input = Importer(7).load()

#Parse
colon_split = [x.split(":") for x in input.split("\n")]
colon_split.pop()
full_split = [[y[0], y[1].split()] for y in colon_split]

#Solving p1 Function
def solvep1(input):

    target = int(input[0])
    values = input[1]

    #Iterate through binary strings representing + or *
    for i in range(2**(len(values)-1)):
        bini = bin(i).replace("0b", "").zfill(len(values)-1)
        
        #Calculate result
        roll_value = int(values[0])
        for j, operator in enumerate(bini):
            if operator == "0":
                roll_value += int(values[j+1])
            else:
                roll_value *= int(values[j+1])
        #Check if result is target and return True
        if roll_value == target:
            return True
    
    #Return false if target not found
    return False


#Base 3 Function
def base3(number):

    digits = ''
    while number:
        digits += str(number % 3)
        number //= 3
    return digits[::-1]


#Solving p2 Function
def solvep2(input):

    target = int(input[0])
    values = input[1]

    #Iterate through base3 strings representing +,* or ||
    for i in range(3**(len(values)-1)):
        terti = base3(i).zfill(len(values)-1)
        
        #Calculate result
        roll_value = int(values[0])
        for j, operator in enumerate(terti):
            if operator == "0":
                roll_value += int(values[j+1])
            elif operator == "1":
                roll_value *= int(values[j+1])
            else:
                roll_value = int(str(roll_value) + values[j+1])
        #Check if result is target and return True
        if roll_value == target:
            return True
        
    return False

p1sum = 0
p2sum = 0
for item in full_split:
    if solvep1(item):
        p1sum += int(item[0])
    if solvep2(item):
        p2sum += int(item[0])

print(f"P1 Answer: {p1sum}, P2 Answer: {p2sum}")

#End Timer
end = time.time()

print(f"Ran in {end - start}s")
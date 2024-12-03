from importer import Importer
import time
import re

#Start Timer
start = time.time()

#Input
input = Importer(3).load()

#Regex list of all mul(x,y)
instructionsp1 = re.findall('mul\(\d+,\d+\)', input)
instructionsp2 = re.findall("mul\(\d+,\d+\)|do\(|don\'t\(", input)

#Function to multiply pairs
def multiply(mul_string):
    ls = re.findall('\d+', mul_string)
    return int(ls[0]) * int(ls[1])

#Find Answer p1
def p1():
    sum = 0
    for item in instructionsp1:
        sum += multiply(item)
    return sum

#Find Answer p2
def p2():
    sum = 0
    current_mod = True
    for item in instructionsp2:
        if item == 'do(':
            current_mod = True
        elif item == "don't(":
            current_mod = False
        elif current_mod:
            sum += multiply(item)
    return sum

#Print Answers
print(p1())
print(p2())

#End Timer
end = time.time()
print(f"Ran in {end-start}s")
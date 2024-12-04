from importer import Importer
import time
import re

#Start Timer
start = time.time()

#Input
input = Importer(4).load()
array = input.split()

#Padding Function
def padArray(a):
    rowlen = len(a[0])
    padded = [''.ljust(rowlen+6, '0') for i in range(3)]
    base = padded

    for s in a:
       newS = s.ljust(rowlen+3, '0')
       newS = newS.rjust(rowlen+6, '0')
       padded.append(newS)

    padded.append(base)
    return padded

#Part 1 Search
def p1search(pA):
    counter = 0

    #Iterate
    for y, string in enumerate(pA):

        for x, char in enumerate(string):

            #Check for X
            if char == "X":

                #Check for XMAS
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        
                        if pA[y+j][x+i] == "M" and pA[y+(j*2)][x+(i*2)] == "A" and pA[y+(j*3)][x+(i*3)] == "S":
                            counter += 1
    return counter

#Part 2 Search
def p2search(pA):
    counter = 0

    #Iterate
    for y, string in enumerate(pA):

        for x, char in enumerate(string):

            #Check for X
            if char == "A":

                #Check for X-MAS
                if ((pA[y-1][x-1] == "M" and pA[y+1][x+1] == "S") or (pA[y-1][x-1] == "S" and pA[y+1][x+1] == "M")) and ((pA[y-1][x+1] == "M" and pA[y+1][x-1] == "S") or (pA[y-1][x+1] == "S" and pA[y+1][x-1] == "M")):
                    counter += 1

    return counter

print(f"P1 Answer: {p1search(padArray(array))}")
print(f"P2 Answer: {p2search(padArray(array))}")

#End Timer
end = time.time()

print(f"Ran in {end - start}s")

                        







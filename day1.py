from importer import Importer
import time

#Start Timer
start = time.time()

#Input
input = Importer(1).load()

#Split text into sides
splitString = str.split(input)

#Split into two lists
leftList = splitString[::2]
rightList = splitString[1::2]

#Sort both Lists
leftList.sort()
rightList.sort()

#Zip Lists
zipped = zip(leftList,rightList)

#Add distances
total = 0
for tuple in zipped:
    total += abs(int(tuple[0]) - int(tuple[1]))

#Print Part 1 Answer
print(f"Part 1: {total}")

#Similarity Score Function
def simScore(simList, targetList):

    simTotal = 0

    for item in simList:
        simTotal += int(item) * targetList.count(item)
    
    return simTotal

#Print Part 2 Answer
print(f"Part 2: {simScore(leftList, rightList)}")
    

#End Timer
end = time.time()

#Return time
print(f"run in {end-start} s")
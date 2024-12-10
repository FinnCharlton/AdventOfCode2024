from importer import Importer
import time

#Start Timer
start = time.time()

# #Input
input = Importer(10).load()

#Parse
array = ["."+x+"." for x in input.split("\n")]
array.pop()
padded_array = ["".zfill(len(array[0])).replace("0",".")]
base = padded_array[0]
for row in array:
    padded_array.append(row)
padded_array.append(base)

search_dirs = [(0,1), (0,-1), (1,0), (-1,0)]


#Tuple Add Function
def add(tup1, tup2):
    return tuple([x1 + x2 for x1, x2 in zip(tup1, tup2)])


#Recursive Search Function
def search(val, tuple, trailheads):

    global global_sum

    for dir in search_dirs:

        new_tup = add(tuple, dir)
        new_val = padded_array[new_tup[1]][new_tup[0]]

        if new_val != ".":
            if val==1 and int(new_val) == 0:
                trailheads.append(new_tup)
                global_sum += 1

            elif int(new_val) == val-1:
                search(int(new_val), new_tup, trailheads)


#Run Parts 1 & 2
sum = 0
global_sum = 0
for y, row in enumerate(padded_array):
    for x, char in enumerate(row):
        if char == "9":
            trailheads = []
            search(9, (x, y), trailheads)
            sum += len(set(trailheads))

print(f"P1 Answer: {sum}")
print(f"P2 Answer: {global_sum}")

#End Timer
end = time.time()

print(f"Ran in {end-start}s")

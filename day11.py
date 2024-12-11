from importer import Importer
import time

#Start Timer
start = time.time()

# #Input
input = Importer(11).load()

array = input.split()
index = {x:array.count(x) for x in array}

def p1_solve(input_array, count):
    if count == 25:
        print(f"P1 Solution: {len(input_array)}")
        return True
    
    next_array = []
    for item in input_array:
        if item == "0":
            next_array.append("1")

        elif len(item) % 2 == 0:
            halfway = int(len(item)/2)
            next_array.append(str(int(item[:halfway])))
            next_array.append(str(int(item[halfway:])))

        else:
            next_array.append(str(int(item)*2024))

    count += 1
    p1_solve(next_array, count)

def blink_rules_p2(num):
    if num == "0":
        return ["1"]

    elif len(num) % 2 == 0:
        halfway = int(len(num)/2)
        return [num[:halfway], str(int(num[halfway:]))]

    else:
        return [str(int(num)*2024)] 

def p2_solve(old_index, count):
    if count == 75:
        sum = 0
        for val in old_index.values():
            sum += int(val)
        print(f"P2 Solution: {sum}")
        return True

    new_index = {}
    for item in old_index:
        results = blink_rules_p2(item)
        for num in results:
            if num in new_index:
                new_index[num] = new_index[num] + old_index[item]
            else:
                new_index[num] = old_index[item]


    count += 1
    p2_solve(new_index, count)

p1_solve(array, 0)
p2_solve(index, 0)

#End Timer
end = time.time()

print(f"Ran in {end-start}s")



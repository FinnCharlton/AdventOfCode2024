from importer import Importer
import time

#Start Timer
start = time.time()

#Input
input = Importer(5).load()

#Parse Input
split = input.split("\n\n")

rule_list = split[0].split("\n")
rules = [x.split("|") for x in rule_list]
updates_list = split[1].split("\n")
updates = [y.split(",") for y in updates_list]
updates.pop()

#Order Update Lists
ordered_lists = []

for update in updates:

    #Find Required Rules
    required_rules = [x for x in rules if x[0] in update and x[1] in update]

    #Count times value appears in key of required rules
    first_nums = [y[0] for y in required_rules]
    last_nums = [y[1] for y in required_rules]
    counts = {val:first_nums.count(val) for val in first_nums}
    missing_val = [z for z in last_nums if z not in first_nums][0]
    counts[missing_val] = 0

    #Sort values by number of times they appear in key
    ordered = []
    while counts:
        key = max(counts, key=counts.get)
        v = counts.pop(key)
        ordered.append(key)

    ordered_lists.append(ordered)

#Identify lists that have changed
zipped = zip(updates, ordered_lists)
p1sum = 0
p2sum = 0
for item in zipped:
    if item[0] == item[1]:
        p1sum +=int(item[1][int(len(item[1])/2)])
    else:
        p2sum += int(item[1][int(len(item[1])/2)])

#Print Answers
print(f"P1 Answer: {p1sum}")
print(f"P2 Answer: {p2sum}")

#Start Timer
end = time.time()

print(f"Ran in {end - start}s")

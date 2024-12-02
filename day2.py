from importer import Importer
import time

#Start Timer
start = time.time()

#Input
input = Importer(2).load()

#Form Data Structure
reports = input.split('\n')
reports = [x.split(' ') for x in reports]
reports.pop()
intReports = []
for list in reports:
    intReports.append([int(y) for y in list])

#Define Testing Algo
def test(list):

    if list != sorted(list) and list != sorted(list, reverse=True):
        return False
    
    for i, item in enumerate(list):
        if i == 0:
            pass
        elif abs(int(item) - int(list[i-1])) < 1 or abs(int(item) - int(list[i-1])) > 3:
            return False
            
        
    return True

#Count Safe Reports
counter = 0
for report in intReports:
    for i in range(len(report)):
        if test([item for j, item in enumerate(report) if i != j]):
            counter += 1
            break

print(counter)

#End Timer
end = time.time()

print(f"Complete in {end - start} s")


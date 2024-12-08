from importer import Importer
import time

#Start Timer
start = time.time()

# #Input
input = Importer(8).load()

#Parse
array = [x for x in input.split("\n")]
array.pop()

#Index Array
height = len(array)
width = len(array[0])
index_dict = {}
for y, row in enumerate(array):
    for x, item in enumerate(row):
        if item == ".":
            pass
        elif item in index_dict:
            index_dict[item].append((x,y))
        else:
            index_dict[item] = [(x,y)]
        
#Bound Checker Function
def check_bounds(tuple, list):
    if tuple[0] >= 0 and tuple[0] < width and tuple[1] >= 0 and tuple[1] < height:
        list.append(tuple)

#Solve P1
# antinodes = []
# for position_list in index_dict.values():
#     for i, pos in enumerate(position_list):
#         for next_pos in position_list[i+1:]:

#             x_delta = next_pos[0] - pos[0]
#             y_delta = next_pos[1] - pos[1]

#             min_node = (pos[0] - x_delta, pos[1] - y_delta)
#             max_node = (next_pos[0] + x_delta, next_pos[1] + y_delta)

#             check_bounds(min_node, antinodes)
#             check_bounds(max_node, antinodes)
            
#Solve P2
antinodes = []
for position_list in index_dict.values():
    for i, pos in enumerate(position_list):
        for next_pos in position_list[i+1:]:
            antinodes.append(pos)
            antinodes.append(next_pos)

            x_delta = next_pos[0] - pos[0]
            y_delta = next_pos[1] - pos[1]

            for i in range(int(max(height, width) / min(abs(x_delta), abs(y_delta)))):

                min_node = (pos[0] - (x_delta*(i+1)), pos[1] - (y_delta*(i+1)))
                max_node = (next_pos[0] + (x_delta*(i+1)), next_pos[1] + (y_delta*(i+1)))

                check_bounds(min_node, antinodes)
                check_bounds(max_node, antinodes)

print(len(set(antinodes)))


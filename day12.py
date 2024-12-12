from importer import Importer
import time

#Start Timer
start = time.time()

# #Input
# input = Importer(12).load()

input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

#Parse
array = ["."+x+"." for x in input.split("\n")]
# array.pop()
padded_array = ["".zfill(len(array[0])).replace("0",".")]
base = padded_array[0]
for row in array:
    padded_array.append(row)
padded_array.append(base)

#Tuple Add Function
def add(tup1, tup2):
    return tuple([x1 + x2 for x1, x2 in zip(tup1, tup2)])

#Tuple Subtract Function
def subtract(tup1, tup2):
    print(f"{tup1} - {tup2} = {([x1 - x2 for x1, x2 in zip(tup1, tup2)])}")
    return tuple([x1 - x2 for x1, x2 in zip(tup1, tup2)])


#Recursive DFS Function
def dfs(test_point):
    global padded_array, visited_points, region_area, region_list, perimeter, perimeter_dict, directions
    
    visited_points.append(test_point)
    region_area += 1
    region_list.append(test_point)


    test_value = padded_array[test_point[1]][test_point[0]]

    for dir in directions:
        new_point = add(test_point, dir)
        new_value = padded_array[new_point[1]][new_point[0]]
        if test_value == new_value:
            if new_point not in visited_points:
                dfs(new_point)
        else:
            if test_point in perimeter_dict:
                perimeter_dict[test_point].append(new_point)
            else:
                perimeter_dict[test_point] = [new_point]
            perimeter += 1

# #Recursive DFS Function p2
# def dfs_p2(test_point, prev_point, prev_perimeters):
#     global padded_array, visited_points, region_area, region_list, perimeter, directions
#     print(f"Testing {test_point} with previous {prev_point} and prev perims {prev_perimeters}")
#     visited_points.append(test_point)
#     region_area += 1
#     region_list.append(test_point)


#     test_value = padded_array[test_point[1]][test_point[0]]

#     test_perimeters = [add(test_point, dir) for dir in directions if padded_array[add(test_point, dir)[1]][add(test_point, dir)[0]] != test_value]
#     print(f"Perimeters = {test_perimeters}")
#     for dir in directions:
        
#         new_point = add(test_point, dir)
#         new_value = padded_array[new_point[1]][new_point[0]]
#         print(f"dir {dir} with new point {new_point} and new value {new_value}")
#         if test_value == new_value:
#             if new_point not in visited_points:
#                 print(f"Running new test {new_point}")
#                 dfs_p2(new_point, test_point, test_perimeters)
#         elif subtract(new_point, subtract(test_point, prev_point)) not in prev_perimeters:
#             print(f"Adding 1 to perim - on {new_point}")
#             perimeter += 1
#         else:
#             print(f"NOT adding 1 to perim - on {new_point}")

#Solve p2
visited_points = []
directions = [(0,1), (0,-1), (1,0), (-1,0)]
overall_sum = 0
overall_regions = []
for y, row in enumerate(padded_array):
    for x, item in enumerate(row):
        perimeter = 0
        region_area = 0
        region_list = []
        perimeter_dict = {}

        if (x, y) not in visited_points and item != ".":
            dfs((x,y))
            # print(f"Start point {x, y}, area= {region_area}, perimeter= {perimeter}, price= {region_area*perimeter}")
            # overall_sum += (perimeter*region_area)
            # overall_regions.append(region_list)
            print(f"For region {x, y}, region area = {region_area} perimterlist = {perimeter_dict}")

# def prune_for_area(perim_list, region_list):
#     new_list = 



# print(overall_sum)
# print(overall_regions)






    





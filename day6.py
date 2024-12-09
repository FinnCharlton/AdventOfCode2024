from importer import Importer
import time

#Start Timer
start = time.time()

#Input
input = Importer(6).load()

#Parse
array = [list(x) for x in input.split("\n")]

#Index Map
og_hash_list = []
dot_list = []
for y, ls in enumerate(array):
    for x, item in enumerate(ls):
        if item in ['#']:
            og_hash_list.append((x, y))
        if item not in ['.','#']:
            og_arrow_coords = (x, y)
        else:
            dot_list.append((x, y))

height = len(array)
width = len(array[0])

#Direction Mapping dictionary
dir_map = {'>':(1, 0), '<':(-1, 0), '^':(0, -1), 'v':(0, 1)}

#Next Direction dictionary
next_dir = {'>':'v', '<':'^', '^':'>', 'v':'<'}

#Tuple add function
def add(tup1, tup2):
    return tuple([x1 + x2 for x1, x2 in zip(tup1, tup2)])

#p1 moving algorithm
def make_move_p1(arrow_coords, current_dir, positions, completed):

    #Calculate new position
    new_position = add(arrow_coords, dir_map[current_dir])

    #Check if next position is AoB
    if new_position[0] < 0 or new_position[0] >= width or new_position[1] < 0 or new_position[1] >= height:
        completed = True
        return arrow_coords, current_dir, positions, completed

    #Check if facing a hash, turn if True
    elif new_position in hash_list:
        current_dir = next_dir[current_dir]
        return arrow_coords, current_dir, positions, completed

    #Otherwise, move
    else:
        arrow_coords = new_position
        positions.append(new_position)
        return arrow_coords, current_dir, positions, completed
    
#p2 moving algorithm
def make_move_p2(arrow_coords, current_dir, moves, completed):

    #Calculate new position
    new_position = add(arrow_coords, dir_map[current_dir])

    #Check if next position is AoB
    if new_position[0] < 0 or new_position[0] >= width or new_position[1] < 0 or new_position[1] >= height:
        completed = True
        return arrow_coords, current_dir, moves, completed

    #Check if facing a hash, turn if True
    elif new_position in hash_list:
        current_dir = next_dir[current_dir]
        return arrow_coords, current_dir, moves, completed

    #Otherwise, move
    else:
        arrow_coords = new_position
        moves += 1
        return arrow_coords, current_dir, moves, completed
    
#Set initial conditions
completed = False
current_dir = '^'

#Solve p2
results_list = []
for dot in dot_list:
    completed = False
    current_dir = '^'
    moves = 0
    hash_list = og_hash_list + [dot]
    arrow_coords = og_arrow_coords

    while not completed and moves < 50000:
        arrow_coords, current_dir, moves, completed = make_move_p2(arrow_coords, current_dir, moves, completed)
    if moves > 49900:
        results_list.append(dot)


print(f"P2 Answer: {len(results_list)}")

#End Timer
end = time.time()
print(f"Ran in {end - start}s")






# #Solve p1
# while not completed:
#     arrow_coords, current_dir, positions, completed = make_move_p1(arrow_coords, current_dir, positions, completed)

# p1_answer = len(set(positions))

# print(p1_answer)
    

    




    



# arrow_x, arrow_y = find_arrow(array)
from importer import Importer
import time

#Start Timer
start = time.time()

# #Input
input = Importer(9).load()
input = input.replace("\n","")

# input = "2333133121414131402"

files = input[::2]


#Form Input Stack
# stack = []
# for i, item in enumerate(files):
#     for j in range(int(item)):
#         stack.append(i)

#Form Full String
full_string = []
for i, char in enumerate(input):
    if i % 2 == 0:
        for j in range(int(char)):
            full_string.append(str(int(int(i)/2)))
    else:
        for j in range(int(char)):
            full_string.append(".")

#Find Val Function
def find_val(file_list, length, val):
    for i in range(len(file_list) - (length -1)):
        if file_list[i:i+length] == [val for j in range(length)]:
            return i
    return -1

        
#Iterate through files backward        
for i, file in enumerate(files[::-1]):
    file_id = len(files)-(i+1)
    print(f"ID is {file_id}")

    #Find Spaces to move
    space_index = find_val(full_string, int(file), ".")

    #Find Vals to move
    val_index = find_val(full_string, int(file), str(file_id))

    if space_index < val_index and space_index != -1:

        #Change space index to vals
        full_string[space_index: space_index + int(file)] = [str(file_id) for x in range(int(file))]

        #Change vals index to spaces
        full_string[val_index: val_index + int(file)] = ["." for x in range(int(file))]

# num_files = len(stack)

# #Solve P1
# file_block = []
# file_cnt = 0
# pos_cnt = 0
# sum = 0
# while pos_cnt < num_files:
    
#     #Check if file or spaces
#     if file_cnt % 2 == 0:

#         #Add to list input[cnt] times
#         for i in range(min(int(input[file_cnt]), num_files-pos_cnt)):

#             sum += pos_cnt*stack.pop(0)
#             pos_cnt += 1

#     else:

#         #Add to list input[cnt] times
#         for i in range(min(int(input[file_cnt]), num_files-pos_cnt)):

#             sum += pos_cnt*stack.pop()
#             pos_cnt += 1

#     file_cnt += 1

# print(sum)
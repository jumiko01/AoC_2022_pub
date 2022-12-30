#!/usr/bin/python

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
#file = open("puzzle_input.txt","r")
file = open("puzzle_exmpl.txt","r")
result = 0

print("los gehts!")
for line in file:
    cur_line = line.rstrip()
#    print(cur_line)
    if (cur_line == 'A X'):
        result = result + 1

file.close()
print("\n\n the Result_1: \n" + str(result))

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
result = 0
for line in file:
    cur_line = line.rstrip()

file.close()
print("\n\n the Result_2: \n" + str(result))

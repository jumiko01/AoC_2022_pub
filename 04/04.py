#!/usr/bin/python

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
result = 0
file = open("puzzle_input.txt","r")
print("los gehts!")
for line in file:
    cur_line = line.rstrip()
#    print(cur_line)
    temp1 = cur_line.split(',')
    temp2 = temp1[0].split('-')
    temp3 = temp1[1].split('-')
    if ((int(temp2[0])<=int(temp3[0])) and (int(temp2[1])>=int(temp3[1]))) or ((int(temp3[0])<=int(temp2[0])) and (int(temp3[1])>=int(temp2[1]))):
        result = result + 1
file.close()
print("\n\n the Result_1: \n" + str(result))

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
result = 0
for line in file:
    cur_line = line.rstrip()
#    print(cur_line)
    temp1 = cur_line.split(',')
    temp2 = temp1[0].split('-')
    temp3 = temp1[1].split('-')
    if ( (  (int(temp2[0])<=int(temp3[0])) and (int(temp2[1])>=int(temp3[0]))) 
        or ((int(temp3[0])<=int(temp2[0])) and (int(temp3[1])>=int(temp2[0]))) ):
        result = result + 1
file.close()
print("\n\n the Result_2: \n" + str(result))

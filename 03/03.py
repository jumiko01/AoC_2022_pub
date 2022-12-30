#!/usr/bin/python

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\03\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")

prioString = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#print(prioString[0:int(len(prioString)/2)])
#print(prioString[int(len(prioString)/2):int(len(prioString))])
prioSum = 0

print("los gehts!")
for line in file:
    cur_line = line.rstrip()
    compartment_1 = cur_line[0:int(len(cur_line)/2)]
    compartment_2 = cur_line[int(len(cur_line)/2):int(len(cur_line))]

    foundChar = ""

    for x in compartment_1:
        if x in compartment_2:
            if x not in foundChar:
                foundChar = foundChar + x
                i_cnt = 0
                for y in prioString:
                    if x == y:
                        prioSum = prioSum + i_cnt
                        print(x+" is present. prio = " + str(i_cnt) + " prioSum = " + str(prioSum))
                    i_cnt = i_cnt + 1

file.close()
print("\n\n Result_1: \n" + str(prioSum))

file = open("puzzle_input.txt","r")

cur_line_1 = ""
cur_line_2 = ""
cur_line_3 = ""

prioSum = 0

bagdeCnt = 0
for line in file:
    bagdeCnt = bagdeCnt + 1
    cur_line_1 = cur_line_2
    cur_line_2 = cur_line_3
    cur_line_3 = line.rstrip()
    if bagdeCnt == 3 :
        bagdeCnt = 0

        cur_line_temp = ""
        if len(cur_line_2) > len(cur_line_1):
            cur_line_temp = cur_line_1
            cur_line_1 = cur_line_2
            cur_line_2 = cur_line_temp

        if len(cur_line_3) > len(cur_line_1):
            cur_line_temp = cur_line_1
            cur_line_1 = cur_line_3
            cur_line_3 = cur_line_temp

        foundChar = ""
        for x in cur_line_1:
            if (x in cur_line_2) and (x in cur_line_3):
                if x not in foundChar:
                    foundChar = foundChar + x
                    i_cnt = 0
                    for y in prioString:
                        if x == y:
                            prioSum = prioSum + i_cnt
                            print(x+" is present. prio = " + str(i_cnt) + " prioSum = " + str(prioSum))
                        i_cnt = i_cnt + 1
               
file.close()
print("\n\n Result_2: \n" + str(prioSum))


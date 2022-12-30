#!/usr/bin/python

file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\01\\puzzle_input.txt","r")
cal = 0
calMax_1 = 0
calMax_2 = 0
calMax_3 = 0
print("los gehts!")
for line in file:
    cur_line = line.rstrip()
#    print(cur_line)
    if (cur_line == '\n') or (cur_line == ''):
        if calMax_1 < cal :
            calMax_3 = calMax_2
            calMax_2 = calMax_1
            calMax_1 = cal
        elif calMax_2 < cal:
            calMax_3 = calMax_2
            calMax_2 = cal
        elif calMax_3 < cal:
            calMax_3 = cal
   
        print("---\n"+str(cal)+", "+str(calMax_1)+", "+str(calMax_2)+" ,"+str(calMax_3)+"\n---")
        cal = 0
    else:
        cal = cal + int(cur_line)
#        print(cal)
file.close()

print("\n\n the biggest: \n" + str(calMax_1)+"\n"+str(calMax_2)+"\n"+str(calMax_3)+"\n")
print("sum: " + str(calMax_1+calMax_2+calMax_3))

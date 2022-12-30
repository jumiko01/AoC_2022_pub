#!/usr/bin/python

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
#file = open("puzzle_exmpl.txt","r")
result = 0

cycleCnt = 0
regX = 1
signalStrength = 0
CRT = []
i = 0
while i < 6:
    CRT.append([])
    i=i+1
#print(CRT)

def printCRT(rX, cycle):
    pling = False
    print("rX: "+str(rX)+", cycle: "+str(cycle))

    if(cycle>=200):
        if(abs(rX+200-cycle) <=1):
            pling = True
        if pling:
            CRT[5].append('#')
        else:
            CRT[5].append('.')
    elif(cycle>=160):
        if(abs(rX+160-cycle) <=1):
            pling = True
        if pling:
            CRT[4].append('#')
        else:
            CRT[4].append('.')
    elif(cycle>=120):
        if(abs(rX+120-cycle) <=1):
            pling = True
        if pling:
            CRT[3].append('#')
        else:
            CRT[3].append('.')
    elif(cycle>=80):
        if(abs(rX+80-cycle) <=1):
            pling = True
        if pling:
            CRT[2].append('#')
        else:
            CRT[2].append('.')
    elif(cycle>=40):
        if(abs(rX+40-cycle) <=1):
            pling = True
        if pling:
            CRT[1].append('#')
        else:
            CRT[1].append('.')
    else:
        if(abs(rX-cycle) <=1):
            pling = True
        if pling:
            CRT[0].append('#')
        else:
            CRT[0].append('.')

print("los gehts!")
for line in file:
    cur_line = line.rstrip()

    if cur_line[0] == 'a':
        temp = cur_line.split(' ')
        v = int(temp[1])
#        print(temp)
        printCRT(regX, cycleCnt)
        cycleCnt = cycleCnt + 1
        if(cycleCnt == 20 or (((cycleCnt-20) % 40) == 0)):
            signalStrength = signalStrength + (cycleCnt * regX)
#            print("cycle: "+str(cycleCnt)+", regX: " +str(regX)+", strength: "+str(signalStrength))
        if(cycleCnt > 240):
            break
        
        printCRT(regX, cycleCnt)
        cycleCnt = cycleCnt + 1
        if(cycleCnt == 20 or (((cycleCnt-20) % 40) == 0)):
            signalStrength = signalStrength + (cycleCnt * regX)
#            print("cycle: "+str(cycleCnt)+", regX: " +str(regX)+", strength: "+str(signalStrength))
        if(cycleCnt > 240):
            break
        
        regX = regX + v
#        print(v)
#        print(regX)
    else:
        printCRT(regX, cycleCnt)
        cycleCnt = cycleCnt + 1
        if(cycleCnt == 20 or (((cycleCnt-20) % 40) == 0)):
            signalStrength = signalStrength + (cycleCnt * regX)
#            print("cycle: "+str(cycleCnt)+", regX: " +str(regX)+", strength: "+str(signalStrength))
        if(cycleCnt > 240):
            break
        

file.close()

result = signalStrength

print("\n\n the Result_1: \n" + str(result))

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
result = 0
for line in file:
    cur_line = line.rstrip()

file.close()
print("\n\n the Result_2:")
for x in CRT:
    tempLine = ''
    for y in x:
        tempLine=tempLine+y
    
    print(tempLine)

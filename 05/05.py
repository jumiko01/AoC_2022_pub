#!/usr/bin/python

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
result = True

print("los gehts!")
readLength = True
fillStacks = True

noOfLinesToAnalyze = 0
noOfStacks = 0
allLinesForStacks = []
allStacks = []
allStacks_2 = []

readOperations = False
noOfOperations = 0
operations = []

for line in file:
    cur_line = line.rstrip()
    #print(cur_line[0] + cur_line[1] + cur_line[2])
    if readLength:
        if cur_line[1] == "1":
            noOfStacks = int((len(cur_line)+2) / 4)
            print("noOfStacks: "+str(noOfStacks))
            readLength = False
        else:
            allLinesForStacks.append(cur_line)
            noOfLinesToAnalyze = noOfLinesToAnalyze + 1
    
    elif readOperations:
        noOfOperations = noOfOperations + 1
        curOp = []
        temp = cur_line.split(" ")
        curOp.append(int(temp[1]))
        curOp.append(int(temp[3]))
        curOp.append(int(temp[5]))

        operations.append(curOp)
    else:
        readOperations = True

print("operations: \n" + str(operations))
file.close()

### init stacks
i= 0
while i<noOfStacks:
    allStacks.append([])
    allStacks_2.append([])
    i = i + 1

### fill stacks
i = 0
while i < noOfLinesToAnalyze:
    index = noOfLinesToAnalyze - 1 - i
    noOfElementsInLine = int( ((len(allLinesForStacks[index])+1)/4) )
    print("noOfElementsInLine: "+str(noOfElementsInLine))
    j = 0
    while j < noOfElementsInLine:
        x = []
        x.append(allLinesForStacks[index][1+(j*4)])
        #print(x)
        if x[0] != ' ':
            allStacks[j].append(x)
            allStacks_2[j].append(x)
        j=j+1
    
    i=i+1

print("---- Stakcks ----")
print(allStacks)
print("--------")

### do operations
i = 0
while i < noOfOperations:
    cycles = operations[i][0]
    sorc = operations[i][1]
    dest = operations[i][2]
#    print(cycles)
#    print(sorc)
#    print(dest)
#    print("--------")

    j=0
    while j < cycles:
        temp = allStacks[sorc-1].pop()
#        print(allStacks)
        allStacks[dest-1].append(temp)
#        print(allStacks)
        j=j+1

    i=i+1

print("---- Stakcks new order ----")
print(allStacks)
print("--------")

result = ""

i=0
while i<noOfStacks:
    result = result + str(allStacks[i].pop())
    i=i+1

print("\n\n---- the Result_1: \n" + str(result))

#### puzzle 2
print("\n\n PUZZLE 2")

print("---- Stakcks 2 ----")
print(allStacks_2)
print("--------")

i = 0
while i < noOfOperations:
    cycles = operations[i][0]
    sorc = operations[i][1]
    dest = operations[i][2]

    j=0
    temp = []
    print("\n--- Runde: " + str(i+1) + " - operation: " + str(operations[i]))
    print("befor: " + str(allStacks_2))
    while j < cycles:
        temp.append(allStacks_2[sorc-1].pop())
        print("change_" + str(j+1) + ": " + str(allStacks_2))
        print("temp: "+ str(temp))
        j=j+1
    temp.reverse()
    allStacks_2[dest-1].extend(temp)
    print("after: " + str(allStacks_2))
    i=i+1

result = ""

i=0
while i<noOfStacks:
    result = result + str(allStacks_2[i].pop())
    i=i+1
print("---result ---")

print("\n\n the Result_2: \n" + str(result))

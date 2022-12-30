#!/usr/bin/python

from copy import deepcopy 

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
#file = open("puzzle_exmpl.txt","r")
result = 0

monkey = []
monkey_2 = []
monkeyData = [] # [items],[operation],[test],[true],[fals]
#monkeyData.append(([],[],[],[],[]))
monkeyInspectionCnt = []
monkeyInspectionCnt_2 = []
noOfMonkeys = 0
print("los gehts!")

def monkeyDataInit():
    monkeyData.clear() # [items],[operation],[test],[true],[fals]
#    monkeyData.append(([],[],[],[],[]))

def monkeyDataSave():
    temp = deepcopy(monkeyData)
    temp1 = deepcopy(monkeyData)
    temp.append(0) # Inspection counter
    temp1.append(0)
    monkey.append(temp)
    monkey_2.append(temp1)

def monkeyDataAnalyse(cur_line):
    if (cur_line[2] == 'S'):
        temp = cur_line.split(' ')
#                print(temp)
        items = []
        elementCnt = len(temp)
        i = 4
        while i < elementCnt:
            items.append(temp[i].split(',')[0])
            i=i+1
#                print('items: '+ str(items))
#                print(elementCnt)
        monkeyData.append(items)
    elif (cur_line[2] == 'O'):
        temp = cur_line.split(' ')
#                print(temp)
        operation = []
        operation.append(temp[6])
        operation.append(temp[7])
        monkeyData.append(operation)
    elif (cur_line[2] == 'T'):
        temp = cur_line.split(' ')
        monkeyData.append(temp[5])
    else:
        temp = cur_line.split(' ')
#                print(temp)
        if(temp[5] == 'true:'):
            monkeyData.append(temp[9])
        if(temp[5] == 'false:'):
            monkeyData.append(temp[9])
        
def monkeyInspektion(curMonkey, monkeyList):
    for item in curMonkey[0]:
        curMonkey[5] = curMonkey[5] + 1
        worryLevel = int(item)
#        print('worryLvl: '+str(worryLevel))
        if curMonkey[1][1] == 'old':
            worryModyfikstor = int(item)
        else:
            worryModyfikstor = int(curMonkey[1][1]) 
#        print('worryModyfikstor: '+str(worryModyfikstor))

        if curMonkey[1][0] == '+':
#            print('Op: '+'+')
            worryLevel = worryLevel + worryModyfikstor
        elif curMonkey[1][0] == '*':
#            print('Op: '+'*')
            worryLevel = worryLevel * worryModyfikstor
        elif curMonkey[1][0] == '-':
#            print('Op: '+'-')
            worryLevel = worryLevel - worryModyfikstor
        elif curMonkey[1][0] == '/':
#            print('Op: '+'/')
            worryLevel = worryLevel / worryModyfikstor

#        print('worryLevel post:'+str(worryLevel))
        worryLevel = int(worryLevel / 3)
#        print('worryLevel final:'+str(worryLevel))
#        print()

        test = int(curMonkey[2])
        true = int(curMonkey[3])
        false = int(curMonkey[4])
        if worryLevel % test == 0:
            monkeyList[true][0].append(worryLevel)
        else:
            monkeyList[false][0].append(worryLevel)

    curMonkey[0].clear()

def monkeyInspektion_2(curMonkey, monkeyList, testLcm):
    for item in curMonkey[0]:
        curMonkey[5] = curMonkey[5] + 1
        worryLevel = int(item)
#        print('worryLvl: '+str(worryLevel))
        if curMonkey[1][1] == 'old':
            worryModyfikstor = int(item)
        else:
            worryModyfikstor = int(curMonkey[1][1]) 
#        print('worryModyfikstor: '+str(worryModyfikstor))

        if curMonkey[1][0] == '+':
#            print('Op: '+'+')
            worryLevel = worryLevel + worryModyfikstor
        elif curMonkey[1][0] == '*':
#            print('Op: '+'*')
            worryLevel = worryLevel * worryModyfikstor
        elif curMonkey[1][0] == '-':
#            print('Op: '+'-')
            worryLevel = worryLevel - worryModyfikstor
        elif curMonkey[1][0] == '/':
#            print('Op: '+'/')
            worryLevel = worryLevel / worryModyfikstor
            
        if worryLevel > (testLcm):
            worryLevel = testLcm + (worryLevel % testLcm)

        test = int(curMonkey[2])
        true = int(curMonkey[3])
        false = int(curMonkey[4])
        if worryLevel % test == 0:
            monkeyList[true][0].append(worryLevel)
        else:
            monkeyList[false][0].append(worryLevel)

    curMonkey[0].clear()
    
### lowest common devider
def lcm(num_1, num_2):
	num_1 = int(num_1)
	num_2 = int(num_2)
	if num_1 < num_2:
		temp = num_1
		num_1 = num_2
		num_2 = temp
		
	num_1_mul = num_1
	cnt = 1
	while (num_1_mul % num_2) != 0:
		cnt = cnt + 1
		num_1_mul = num_1 * cnt
		
	return num_1_mul
	
    
##################################################
# read input
##################################################
for line in file:
    cur_line = line.rstrip()
#    print(cur_line)
    if (cur_line != ''):
        if (cur_line[0] == 'M'):
            print("monkeyData: " + str(monkeyData))
            if(noOfMonkeys > 0):
                monkeyDataSave()
#                print('Monkey'+str(noOfMonkeys-1))
#                print(monkey[noOfMonkeys-1])
#                print()
#            monkeyInspectionCnt.append(int(0))
#            print("monkeyInspectionCnt: " + str(monkeyInspectionCnt))
            noOfMonkeys = noOfMonkeys + 1
            monkeyDataInit()
            print("noOfMnkeys: " + str(noOfMonkeys))
        else:
            monkeyDataAnalyse(cur_line)

monkeyDataSave()
#print('Monkey'+str(noOfMonkeys-1))
#print(monkey[noOfMonkeys-1])
#print()

file.close()

################################
# Monkeys play their game
################################
print('\n\n ############### Round 1 #####################\n')
i=0
for m in monkey:
    print('\nM'+str(i))
    print(m)
    i=i+1

i=0
while i < 20:
    for m in monkey:
        monkeyInspektion(m, monkey)
    i = i + 1

i=0
print('\n---')
for m in monkey:
    print('\nM'+str(i))
    print(m)
    print(m[5])
    i=i+1

for m in monkey:
    monkeyInspectionCnt.append(m[5])

print("monkeyInspectionCnt: " + str(monkeyInspectionCnt))
monkeyInspectionCnt.sort()
print("monkeyInspectionCnt: " + str(monkeyInspectionCnt))

result=monkeyInspectionCnt[noOfMonkeys-1]*monkeyInspectionCnt[noOfMonkeys-2]

print("\n\n the Result_1: \n" + str(result))

###############################################################
# Round 2
###############################################################

print('\n\n ############### Round 2 #####################\n')
#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")

i=0
for m in monkey_2:
    print('\nM2_'+str(i))
    print(m)
    i=i+1

test_lcm = 1
for m in monkey_2:
	test_lcm = lcm(test_lcm, m[2])
#	print('lcm: '+ str(test_lcm))
	
print("\ntest_lcm: "+ str(test_lcm))
print()

i=0
while i < 10000:
    for m in monkey_2:
        monkeyInspektion_2(m, monkey_2, test_lcm)
    i = i + 1

i=0
print('\n---')
for m in monkey_2:
    print('\nM2_'+str(i))
    print(m)
    print(m[5])
    i=i+1

for m in monkey_2:
    monkeyInspectionCnt_2.append(m[5])

print("monkeyInspectionCnt: " + str(monkeyInspectionCnt_2))
monkeyInspectionCnt_2.sort()
print("monkeyInspectionCnt: " + str(monkeyInspectionCnt_2))

result=monkeyInspectionCnt_2[noOfMonkeys-1]*monkeyInspectionCnt_2[noOfMonkeys-2]

print("\n\n the Result_2: \n" + str(result))

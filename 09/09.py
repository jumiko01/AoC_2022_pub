#!/usr/bin/python

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
#file = open("puzzle_exmpl.txt","r")
#file = open("puzzle_exmpl_2.txt","r")
result = 0

moveSeq = []
tailPositions = []


print("los gehts!")
for line in file:
	cur_line = line.rstrip()
	temSeq=[]
	tempSeq=cur_line.split(" ")
	moveSeq.append(tempSeq)

file.close()


def moveTheSnake(instruction, snake, tailPositions):
	i = 0
	noOfSteps = int(instruction[1])	
#	print("noOfSteps: " + str(noOfSteps) )
	while i < noOfSteps:
		# Move Head
		if( instr[0] == 'R'):
			snake[0][0] = snake[0][0] + 1
			
		elif( instr[0] == 'L'):
			snake[0][0] = snake[0][0] - 1
		
		elif( instr[0] == 'U'):
			snake[0][1] = snake[0][1] + 1

		elif( instr[0] == 'D'):
			snake[0][1] = snake[0][1] - 1

		# Move Tail
		tailHaveToWait = False
		j = 1
		while j < len(snake):
			tailHaveToWait = ( (abs(snake[j-1][0] - snake[j][0]) <= 1) 
							and (abs(snake[j-1][1] - snake[j][1]) <= 1) )

			if(not tailHaveToWait):
				if (abs(snake[j-1][0] - snake[j][0]) >= 1): 
					if snake[j-1][0] > snake[j][0]:
						snake[j][0] = snake[j][0] + 1
					else:
						snake[j][0] = snake[j][0] - 1
		
				if (abs(snake[j-1][1] - snake[j][1]) >= 1):
					if snake[j-1][1] > snake[j][1]:
						snake[j][1] = snake[j][1] + 1
					else:
						snake[j][1] = snake[j][1] - 1
		
			j = j + 1

#		print(str(i+1)+ ". move =========> " + instruction[0])
#		print('tailHaveToWait: ' + str(tailHaveToWait))
#		print('snake: '+str(snake))
		newPosi = True
#		print(' --- check positions ---')
#		print('tailPositions: '+ str(tailPositions))
#		print('tail: '+ str(snake[len(snake)-1] ))
		if snake[len(snake)-1] in tailPositions:
			newPosi = False
#			print('newPosi: ' + str(newPosi))	
			
		if(newPosi == True):
#			print('+ add new position')
			temp = [0,0]
			temp[0] = snake[len(snake)-1] [0]
			temp[1] = snake[len(snake)-1] [1] 
			tailPositions.append(temp)
			
		i = i + 1


print("\n\n####	Round 1 #############")
snake = []

tailPositions.clear()
snake.clear()
lengthOfSnake = 2

i = 0
while i < lengthOfSnake:
	snake.append([0,0])
	i = i + 1

for instr in moveSeq:
	moveTheSnake(instr, snake, tailPositions)

#print(tailPositions)
result = len(tailPositions)
print("\n the Result_1: \n" + str(result))

print("\n\n####	Round 2 #############")
snake = []

tailPositions.clear()
snake.clear()
lengthOfSnake = 10

i = 0
while i < lengthOfSnake:
	snake.append([0,0])
	i = i + 1

for instr in moveSeq:
	moveTheSnake(instr, snake, tailPositions)

#print(tailPositions)
result = len(tailPositions)
print("\n the Result_2: \n" + str(result))

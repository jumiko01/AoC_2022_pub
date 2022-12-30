#!/usr/bin/python

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\02\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")

A = 1 # Rock
B = 2 # Paper
C = 3 # Scissiors

X = 1 # Rock        Lose
Y = 2 # Paper       Draw
Z = 3 # Scissiors   Win

Win = 6
Draw = 3
Lose = 0

score = 0
print("los gehts!")
for line in file:
    cur_line = line.rstrip()
#    print(cur_line)
    if (cur_line == 'A X'):
        score = score + X + Draw
    elif (cur_line == 'A Y'):
        score = score + Y + Win
    elif (cur_line == 'A Z'):
        score = score + Z + Lose

    elif (cur_line == 'B X'):
        score = score + X + Lose
    elif (cur_line == 'B Y'):
        score = score + Y + Draw
    elif (cur_line == 'B Z'):
        score = score + Z + Win

    elif (cur_line == 'C X'):
        score = score + X + Win
    elif (cur_line == 'C Y'):
        score = score + Y + Lose
    elif (cur_line == 'C Z'):
        score = score + Z + Draw

file.close()
print("\n the score R1: \n" + str(score))

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\02\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
score = 0
for line in file:
    cur_line = line.rstrip()
    if (cur_line == 'A X'):
        score = score + C + Lose
    elif (cur_line == 'A Y'):
        score = score + A + Draw
    elif (cur_line == 'A Z'):
        score = score + B + Win

    elif (cur_line == 'B X'):
        score = score + A + Lose
    elif (cur_line == 'B Y'):
        score = score + B + Draw
    elif (cur_line == 'B Z'):
        score = score + C + Win

    elif (cur_line == 'C X'):
        score = score + B + Lose
    elif (cur_line == 'C Y'):
        score = score + C + Draw
    elif (cur_line == 'C Z'):
        score = score + A + Win

file.close()

print("\n the score R2: \n" + str(score))

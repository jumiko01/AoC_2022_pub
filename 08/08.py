#!/usr/bin/python

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
result = 0

grid = []
noOfX = 0
noOfY = 0
print("los gehts!")
for line in file:
    noOfY = noOfY + 1
    cur_line = line.rstrip()
#    print(cur_line)
    row = []
    for x in cur_line:
        row.append(int(x))
    grid.append(row)

noOfX = len(grid[0])
file.close()

#print("noOfX: " + str(noOfX) + ", noOfY: " + str(noOfY) )
#print("0 _______x")
#print(" |")
#print(" |")
#print("y|")
#print(" ")
#print(grid)

#for row in grid:
#    print(row)

noOfVisibleTrees = 0
highestViewScore = 0
x = 1
y = 1

curTree = 0
treeIsVisible = True
while y < noOfY-1:
    x = 1

    while x < noOfX-1:
        noOfTreesUp = 0
        noOfTreesDown = 0
        noOfTreesLeft = 0
        noOfTreesRight = 0

        curTree = grid[y][x]
        treeIsVisible = True
#        print(" ---- ["+str(x)+"],["+str(y)+"] ----")
        i=0
        while i < x:
            neighboor = grid[y][x-1-i]
#            print("test:1."+str(i)+" - neighboor: "+str(neighboor)+ " -- tree: " + str(curTree))
            if (curTree <= neighboor):
#                print("Tree not visable")
                treeIsVisible = False
                i=x-1
            noOfTreesLeft = noOfTreesLeft + 1
            i=i+1

        if (not treeIsVisible):
            treeIsVisible = True
            i=i+1
            while i < noOfX:
                neighboor = grid[y][i]
#                print("test:2."+str(i)+" - neighboor: "+str(neighboor)+ " -- tree: " + str(curTree))
                if (curTree <= neighboor):
#                    print("Tree not visable")
                    treeIsVisible = False
                    i=noOfX 
                i=i+1
        else:
            i=i+1
            while i < noOfX:
                neighboor = grid[y][i]
                if (curTree <= neighboor):
                    i=noOfX 
                noOfTreesRight = noOfTreesRight + 1
                i=i+1

        if (not treeIsVisible):
            treeIsVisible = True
            i=0
            while i < y:
                neighboor = grid[y-1-i][x]
#                print("test:3."+str(i)+" - neighboor: "+str(neighboor)+ " -- tree: " + str(curTree))
                if (curTree <= neighboor):
#                    print("Tree not visable")
                    treeIsVisible = False
                    i=y-1
                i=i+1
        else:
            i=0
            while i < y:
                neighboor = grid[y-1-i][x]
                if (curTree <= neighboor):
                    i=y-1
                noOfTreesUp = noOfTreesUp + 1
                i=i+1


        if (not treeIsVisible):
            treeIsVisible = True
            i=i+1
            while i < noOfY:
                neighboor = grid[i][x]
#                print("test:4."+str(i)+" - neighboor: "+str(neighboor)+ " -- tree: " + str(curTree))
                if (curTree <= neighboor):
                    treeIsVisible = False
                    i=noOfY
                noOfTreesDown = noOfTreesDown + 1
                i=i+1
        else:
            i=i+1
            while i < noOfY:
                neighboor = grid[i][x]
                if (curTree <= neighboor):
                    i=noOfY
                noOfTreesDown = noOfTreesDown + 1
                i=i+1

        if (treeIsVisible):
            noOfVisibleTrees = noOfVisibleTrees + 1
            temp = noOfTreesUp * noOfTreesDown * noOfTreesLeft * noOfTreesRight
#            print("Up: " + str(noOfTreesUp) + " - Down: " + str(noOfTreesDown) + " - Left: " + str(noOfTreesLeft) + " - Right: " + str(noOfTreesRight) )
            if highestViewScore < temp:
                highestViewScore = temp 
             
#        print("x,y: "+ str(x) + "," + str(y)+ " - tree: " + str(grid[y][x]) + " -> visible: "+ str(treeIsVisible))

#        print("highestViewScore: "+str(highestViewScore))
        x=x+1

    y=y+1

noOfVisibleTrees = noOfVisibleTrees + (noOfX*2) + ((noOfY-2)*2)
result = noOfVisibleTrees
print("\n\n the Result_1: \n" + str(result))

result = highestViewScore
print("\n\n the Result_2: \n" + str(result))

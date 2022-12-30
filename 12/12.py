#!/usr/bin/python
#set PYTHONPATH=%PYTHONPATH%';C:\Repos\AoC_2022\12'

from _12func import MyMap
from _12func import Position
from _12func import Path
from _12func import PathList

from copy import deepcopy


print("los gehts!")

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
#file = open("puzzle_input.txt","r")
file = open("puzzle_exmpl.txt","r")
myMap = MyMap(file)
file.close()

myMap.PrintCoords()

hightVal = []
### create list of 'a' - 'z'    ################
i = ord('a')
while i <= ord('z'):
    hightVal.append(chr(i))
    i=i+1

print('\nhightVal: '+ str(hightVal))




def searchForNewPosi(Courses, MyMap, StartPosi):
#    coursesTemp = deepcopy(Courses)
    i = 0
    startFound = False

    for c in Courses:
        print('\ncheck for new Posiotions   ------')
        print('curCourse:' + str(c))
        print('len(c): '+ str(len(c)))

        NewPosiTemp = []

        if(len(c) == 0):
            Courses.remove(c)
        else:
            curPosi = c[len(c)-1]
#            print('curPosi:' + str(curPosi))
            if(curPosi == []):
                c.pop()
            else:
                if (curPosi[0] > 0):
                    temp=[curPosi[0]-1, curPosi[1], MyMap[curPosi[0]-1][curPosi[1]]]
                    NewPosiTemp.append(temp)
#                    print(NewPosiTemp)
                if (curPosi[0] < len(MyMap)-1):
                    temp=[curPosi[0]+1, curPosi[1], MyMap[curPosi[0]+1][curPosi[1]]]
                    NewPosiTemp.append(temp)
#                    print(NewPosiTemp)
                if (curPosi[1] > 0):
                    temp=[curPosi[0], curPosi[1]-1, MyMap[curPosi[0]][curPosi[1]-1]]
                    NewPosiTemp.append(temp)
#                    print(NewPosiTemp)
                if (curPosi[1] < len(MyMap[0])-1):
        #            print('curPosi[0]: ' + str(curPosi[0]) )
        #            print('curPosi[1]+1: '+ str(curPosi[1]+1))
        #            print('len(MyMap[0]:' + str(len(MyMap[0])))
        #            print('MyMap[curPosi[0]][curPosi[1]+1]): '+ str(MyMap[curPosi[0]][curPosi[1]+1]) )
                    temp=[curPosi[0], curPosi[1]+1, MyMap[curPosi[0]][curPosi[1]+1]]
                    NewPosiTemp.append(temp)
#                    print(NewPosiTemp)


                newCourse = False        
                i = 0
                print('\ncheck where to go ---------------')
                courseStps = True
                while i < len(NewPosiTemp):
                    
                    print('No: ' + str(i) )
                    print('New: ' + str(NewPosiTemp[i]))

                    if (NewPosiTemp[i][2] == 'E'):
                        NewPosiHight = 'z'
                    elif (NewPosiTemp[i][2] == 'S'):
                        NewPosiHight = 'a'
                    else:
                        NewPosiHight = NewPosiTemp[i][2]

                    if (curPosi[2] == 'E'):
                        curPosiHight = 'z'  
                    elif (curPosi[2] == 'S'):
                        curPosiHight = 'a'  
                    else:
                        curPosiHight = curPosi[2]

                    newPosiIsOneLower = coordVal.index(NewPosiHight) == coordVal.index(curPosiHight) - 1
                    newPosiIsEqual = coordVal.index(NewPosiHight) == coordVal.index(curPosiHight)

                    print('newPosiIsOneLower: ' + str(newPosiIsOneLower))
                    print('newPosiIsEqual: ' + str(newPosiIsEqual))
                    print('newPosIsInCourses:' + str(NewPosIsAlreadyPartOfAnotherCourse(Courses, c, NewPosiTemp[i])) ) 
                    
                    if( (NewPosiTemp[i] != c) and (newPosiIsOneLower or newPosiIsEqual) 
                    and not NewPosIsAlreadyPartOfAnotherCourse(Courses, c, NewPosiTemp[i]) ):     
                        if newCourse:
                            temp = deepcopy(c)
                            temp.append(NewPosiTemp[i])
                            tempCourse=[]
                            course.append(tempCourse)
                            Courses.append(tempCourse)
#                            startFound = NewPosiTemp == StartPosi
                            courseStps = False
                            startFound = StartPosi in c
                        else:
                            c.append(NewPosiTemp[i])
                            newCourse = True
                            courseStps = False
                            startFound = StartPosi in c

                    if startFound:
                        break

                    i=i+1
                
                if courseStps:
                    print('deleted')
                    Courses.remove(c)

                
    return startFound 

'''
#print(i-ord('a'))
print(coordVal)

courseList = []
course = []
course.append(desti)
courseList.append(course)
print("Courses: " + str(courseList))

startFound = False
steps = 0 
while startFound == False:
    startFound = searchForNewPosi(courseList, myMap, start)
    steps = steps + 1

print("Courses: " + str(course))
################################################################
#   Round 1 ####################################################
################################################################

result = len(course) - 1
print("\n\n the Result_1: \n" + str(result))
'''
################################################################
#   Round 2 ####################################################
################################################################

result = 0

file.close()
print("\n\n the Result_2: \n" + str(result))

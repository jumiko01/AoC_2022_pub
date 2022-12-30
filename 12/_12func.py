from copy import deepcopy as dcp 

####################################################################
####    Posiotns    ################################################
####################################################################
class Position():
    def __init__(self, X, Y, H):
        x = X
        y = Y
        hight = H
    x = 0
    y = 0
    hight = 'a'

    def SetPosition(self,X,Y,Z):
        self.x = X
        self.y = Y
        self.hight = Z

    def SetPositionWithList(self,Posi=[]):
        self.x = Posi[0]
        self.y = Posi[1]
        self.hight = Posi[2]

####################################################################
#####   Pathes  ####################################################
####################################################################
class Path():
    def __init__(self, Path):
        steps = dcp(Path)
        if len(steps) != 0:
            self.curPosi = steps[len(steps)-1]

    def AddStepWithPosition(self, Posi):
        self.steps.append(Posi)

    def AddStepWithCoordinates(self, X, Y, Z):
        tempPosi = Position(0,0,'a')
        tempPosi.SetPosition(X,Y,Z)
        self.steps.append(tempPosi)

    def AddStepWithList(self, Posi=[]):
        tempPosi = Position(0,0,'a')
        tempPosi.SetPositionWithList([])
        self.steps.append(tempPosi)

    def GetCurrentPosition(self):
        self.curPosi = self.steps[len(self.steps)-1]
        return self.curPosi

    curPosi = Position(0, 0, 'a')
    steps = []

####################################################################
####    Path list   ################################################
####################################################################
class PathList():
    def __init__(self,StartPosi):
        tempPosi = Position(0,0,'a')
        tempPosi.SetPosition(StartPosi.x, StartPosi.y, StartPosi.z)
        self.curPath.AddStepWithPosition(tempPosi)
        self.pathList.append(self.curPath)

    pathList = []

    curPath = Path([])

    def NewPosIsAlreadyPartOfAnotherCourse(self, CurPath, NewPosi):
        stepsInCurPath = len(CurPath)
        retVal = False
        for p in self.pathList:
            if( (p!=CurPath) and (NewPosi in p.steps) ):
                if stepsInCurPath >= len(p):
                    retVal = True
                    break
        
        return retVal

    def AddPath(self, NewPath):
        self.pathList.append(NewPath)

    def SearchNextStep(self, Map):
#    coursesTemp = deepcopy(Courses)
        i = 0
        endFound = False

        for p in self.pathList:
            print('\ncheck for new Positions   ------')
            print('cur path p:' + str(p))
            print('len(p): '+ str(len(p)))

            NewPosiTemp = []

            if(len(p) == 0):
                self.pathList.remove(p)
            else:
                curPosi = p.GetCurrentPositon()
    #            print('curPosi:' + str(curPosi))
                if(curPosi == []):
                    p.pop()
                else:
                    if (curPosi.x > 0):
                        temp=[(curPosi.x)-1, curPosi.y, Map[(curPosi.x)-1][curPosi.y]]
                        NewPosiTemp.append(temp)
    #                    print(NewPosiTemp)
                    if (curPosi.x < len(Map)-1):
                        temp=[(curPosi.x)+1, curPosi.y, Map[(curPosi.x)+1][curPosi.y]]
                        NewPosiTemp.append(temp)
    #                    print(NewPosiTemp)
                    if (curPosi.y > 0):
                        temp=[curPosi.x, (curPosi.y)-1, Map[curPosi.x][(curPosi.y)-1]]
                        NewPosiTemp.append(temp)
    #                    print(NewPosiTemp)
                    if (curPosi.y < len(Map[0])-1):
            #            print('curPosi[0]: ' + str(curPosi[0]) )
            #            print('curPosi[1]+1: '+ str(curPosi[1]+1))
            #            print('len(MyMap[0]:' + str(len(MyMap[0])))
            #            print('MyMap[curPosi[0]][curPosi[1]+1]): '+ str(MyMap[curPosi[0]][curPosi[1]+1]) )
                        temp=[curPosi.x, (curPosi.y)+1, Map[curPosi.x][(curPosi.y)+1]]
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

####################################################################
####    Map    ################################################
####################################################################
class MyMap():
    aMap = []
    start = Position(0,0,'S')
    end = Position(0,0,'E')

    def __init__(self, inputFile):
        i = 0
        j = 0
        for line in inputFile:
            cur_line = line.rstrip()
        #    print(cur_line)
            temp = []
            j = 0
            for x in cur_line:
                temp.append(x)
                if x == 'S':
                    self.start.x = i
                    self.start.y = j
                    self.start.hight = 'S'
                elif x == 'E':
                    self.end.x = i
                    self.end.y = j
                    self.end.hight = 'E'
                j=j+1

            self.aMap.append(temp)

            i=i+1

    def PrintCoords(self): #_map, Start, End):
        i=0
        yCoords = []
        yCoords.append('+')
        while i<len(self.aMap[0]):
            yCoords.append(str(i))
            i=i+1
        print(yCoords)

        i=0
        tempMap = dcp(self.aMap)
        for x in tempMap:
            x.insert(0, str(i))
            print(x)
            i=i+1

        print("start: " + str(self.start.x)+', '+ str(self.start.y)+', '+ str(self.start.hight))
        print("end:   " + str(self.end.x)+', '+ str(self.end.y)+', '+ str(self.end.hight))

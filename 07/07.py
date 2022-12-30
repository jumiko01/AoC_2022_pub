#!/usr/bin/python

xml_string = ('' \
    '<?xml version=\"1.0\"?>\n' \
    '<file_system name="root">' \
#    '   <size>0</size>\n' \
    '</file_system>'
)

print(xml_string)

import xml.etree.ElementTree as ET
#tree = ET.parse('country_data.xml')
#file_system = tree.getfile_system()
#Or directly from a string:
def xmlToString(input):
    return ET.canonicalize(ET.tostring(input)).replace('>', '>\n')

def createSubElement(el, sub):
    subEl = ET.SubElement(el, 'dir')
    subEl.set('name', sub)
    subEl.set('size', '0')
#    subSubEl = ET.SubElement(subEl, 'name')
#    subSubEl.text = sub
    return subEl

def setNewSize(El, size):
    El.set('size', str(size))    

def findDirsSmallerThanIn(limit, Element):
    for dir in Element.iter('dir'):
        if int(dir.get('size')) < limit:
            print(dir[0].text + ": " + dir.attrib['size'])

def getSumOfSpaceOfDirsSmallerThanIn(limit, Element):
    summ = 0
    for dir in Element.iter('dir'):
        if int(dir.get('size')) < limit:
            summ = summ + int(dir.attrib['size'])

    return summ




file_system = ET.fromstring(xml_string)

print(file_system.tag)
print(file_system.attrib)

#size = file_system.attrib
#print(size)
#print(size["size"])
#new_size = int(file_system.attrib["size"])+ 10
#file_system.set( 'size', str(new_size) )

#print(file_system.tag)
#print(file_system.attrib)

#print(ET.canonicalize(ET.tostring(file_system)))
# print(ET.tostring(file_system))
# print(xmlToString(file_system))

# a = createSubElement(file_system, 'a')
# print(xmlToString(file_system))
# b = createSubElement(file_system, 'b')
# print(ET.canonicalize(ET.tostring(file_system)))
# print(xmlToString(file_system))
# c = createSubElement(a, 'c')
# print(xmlToString(file_system))

# setNewSize(b, 100)
# setNewSize(c, 100000)

# print(xmlToString(file_system))

# findDirsSmallerThanIn(1000, file_system)

# print("Sum: " + str(getSumOfSpaceOfDirsSmallerThanIn(1000, file_system)) ) 


file = open("puzzle_input.txt","r")
result = 0

level = 0
dirChain = []

dirChain.append(file_system)

noOfDirs = 0
print("los gehts!")
for line in file:
    cur_line = line.rstrip()
#    print(cur_line)
    # --- Command   ---
    if(cur_line[0] == "$"):
        command = []
        command = cur_line.split(" ")
#        print(command)
        if (command[1] == "cd") and (command[2] != ".."):
            dirChain.append(createSubElement(dirChain[level], command[2]))
            level = level + 1
#            print("created: " + dirChain[level].attrib['name'])
            dirChain_txt = ""
            for x in dirChain:
                dirChain_txt = dirChain_txt + x.attrib['name'] + "; "
            
#            print("dirChain: " + dirChain_txt)
        elif (command[1] == "cd") and (command[2] == ".."):
            if level > 1:
#                print("remove: " + dirChain[level].attrib['name'])
                dirChain.pop()
                level = level - 1


    elif(cur_line[0] != "d"):
        space = cur_line.split(" ")
#        print(space)
        i = 0
        while i < level:
            setNewSize( dirChain[level-i], int(dirChain[level-i].attrib['size']) + int(space[0]) )
#            print( dirChain[level-i].attrib['name'] + ": " + dirChain[level-i].attrib['size'] )
            i=i+1

#    print("level:" + str(level))
#print(xmlToString(file_system))
file.close()

print(ET.canonicalize(ET.tostring(file_system)))

result = getSumOfSpaceOfDirsSmallerThanIn(100000, file_system)
print("\n\n the Result_1: \n" + str(result))

print("\n\n --- Puzzle_2 --- \n")
result = 0

currUsedSpace = dirChain[1].attrib['size']
spaceToFree = 30000000 - ( 70000000 - int(currUsedSpace))

print('currUsedSpace: ' + str(currUsedSpace))
print('spaceToFree: '+ str(spaceToFree))

listOfPossDirs = []
for dir in file_system.iter('dir'):
    if int(dir.attrib['size']) > spaceToFree:
        listOfPossDirs.append(int(dir.attrib['size']))

result = min(listOfPossDirs)
print("\n the Result_2: \n" + str(result))

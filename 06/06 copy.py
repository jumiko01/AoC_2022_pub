#!/usr/bin/python

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
result = 0

print("los gehts!")
for line in file:
    cur_line = line.rstrip()
    charMarker = ""
    pos = 0
    for x in cur_line:
        pos = pos + 1
        if len(charMarker) < 4:
            charMarker = charMarker + x

        else:
            # check for marker
            charMarker_found = True
            for y in charMarker:
#                print("charMarker.count(y): y=" + y + " count="+ str(charMarker.count(y)) )
                if charMarker.count(y) > 1:
                    charMarker_found = False
            
            if charMarker_found:
                break
#                print("--- found ---")
            i = 0
            temp = ""
            while i < 3:
                temp = temp + charMarker[i+1]
#               print(i)
#               print(temp)
                i=i+1
            charMarker = temp
            charMarker = charMarker + x
#        print("charMarker: " + charMarker)
#        print(pos)

result = pos - 1

file.close()
print("\n\n the Result_1: \n" + str(result))

#file = open("C:\\Users\\uif32935\\Documents\\Privat\\AoC\\05\\puzzle_input.txt","r")
file = open("puzzle_input.txt","r")
result = 0
for line in file:
    cur_line = line.rstrip()
    charMarker = ""
    pos = 0
    for x in cur_line:
        pos = pos + 1
        if len(charMarker) < 14:
            charMarker = charMarker + x

        else:
            # check for marker
            charMarker_found = True
            for y in charMarker:
#                print("charMarker.count(y): y=" + y + " count="+ str(charMarker.count(y)) )
                if charMarker.count(y) > 1:
                    charMarker_found = False
            
            if charMarker_found:
                break
 #               print("--- found ---")
            i = 0
            temp = ""
            while i < 13:
                temp = temp + charMarker[i+1]
#                print(i)
#                print(temp)
                i=i+1
            charMarker = temp
            charMarker = charMarker + x
#        print("charMarker: " + charMarker)
#        print(pos)

result = pos - 1

file.close()
print("\n\n the Result_2: \n" + str(result))

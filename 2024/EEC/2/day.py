import argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", default = "false", help="Use test file")
parser.add_argument("-p", "--part", dest="part", default = "1", help= "Problem part to run")
args = parser.parse_args()

def printtest(text):
    if args.test == "true":
        print(text)

def getLines(file):
    p = Path(__file__).with_name(file)
    f = p.open('r')
    lines = f.readlines()
    return lines
words = {}

def setWords(row):
    word_list = row.strip().split(":")[1].split(",")
    for word in word_list:
        if len(word) not in words:
            words[len(word)] = [word]
        else:
            words[len(word)].append(word)       

def readGroup(group_number, row):
    count = 0
    for i in range(0,len(row)+1 - group_number):
        group = row[i:i + group_number]
        if group in words[group_number]:
            count += 1
            if args.test == "true":
                print(group + " in " + str(words[group_number]) + " ?")
    return count

words_backwards = {}
def setWordsBackwards():
    for i in words:
        new_list = []
        for word in words[i]:
            new_list.append(word[::-1])
        words_backwards[i]=new_list

def mergeLists(list_input,list_target):
    for item in list_input:
        if item not in list_target:
            list_target.append(item)

def readGroupPart2(group_number, row,  index_of_runes):
    for i in range(0,len(row)+1 - group_number):
        group = row[i:i + group_number]
        if group in words[group_number] or group in words_backwards[group_number]:
            if args.test == "true":
                print(group + " is in words. indexes are from " + str(i) + " to " + str(i + group_number -1))
            for j in range(i, i + group_number):
                if j not in index_of_runes:
                    index_of_runes.append(j)

def readGroupPart3(group_number, grid, coords):
    for row in range(0,len(grid)):
        for column in range(0,len(grid[0])):
            #check left to right 
            left_to_right = ""
            temp_coords = []
            for i in range (column, column+group_number):
                left_to_right += grid[row][i % len(grid[0])]
                temp_coords.append((row,i % len(grid[0])))
            if left_to_right in words[group_number]:
                if args.test == "true":
                    print(left_to_right + " is in words (left_to_right). coords are " + str(temp_coords))
                mergeLists(temp_coords,coords)
            #check rigt to left
            right_to_left = ""
            temp_coords = []
            for i in range (column, column-group_number,-1):
                right_to_left += grid[row][i % len(grid[0])]
                temp_coords.append((row,i % len(grid[0])))
            if right_to_left in words[group_number]:
                if args.test == "true":
                    print(right_to_left + " is in words (right_to_left). coords are " + str(temp_coords))
                mergeLists(temp_coords,coords)  
            #check top to bottom (does not wrap around)
            top_to_bottom = ""
            temp_coords = []
            if(row+group_number<=len(grid)):
                for j in range (row, row + group_number):
                    top_to_bottom += grid[j][column]
                    temp_coords.append((j,column))
            if top_to_bottom in words[group_number]:
                if args.test == "true":
                    print(top_to_bottom + " is in words (top_to_bottom). coords are " + str(temp_coords))
                mergeLists(temp_coords,coords) 
            #check bottom to top (does not wrap around)
            bottom_to_top = ""
            temp_coords = []
            if(row-group_number>=-1):
                for j in range (row, row - group_number, -1):
                    bottom_to_top += grid[j][column]
                    temp_coords.append((j,column))
            if bottom_to_top in words[group_number]:
                if args.test == "true":
                    print(bottom_to_top + " is in words (bottom_to_top). coords are " + str(temp_coords))
                mergeLists(temp_coords,coords) 
        

#Solution to Part 1
def part1(lines):
    count = 0
    setWords(lines[0])
    for group_number in words:
        row = lines[2].strip()
        count += readGroup(group_number, row)
    print("There are " + str(count) + " rune words.")

#Solution to Part 2
def part2(lines):
    count = 0
    setWords(lines[0])
    setWordsBackwards()
    for row in lines[2:]:
        normal_row = row.strip()
        index_of_runes = []
        for group_number in words:
            readGroupPart2(group_number, normal_row, index_of_runes)
        count += len(index_of_runes)
    print("There are " + str(count) + " runes.")

#Solution to Part 3
def part3(lines):
    count=0
    setWords(lines[0])
    grid = []
    for row in lines[2:]:
        grid.append(row.strip())
    coords = []
    print("There are " + str(len(words)) + " group numbers.")
    for group_number in words:
        print("reading group " + str(group_number) + "...")
        readGroupPart3(group_number, grid, coords)
    count += len(coords)
    print("There are " + str(count) + " runes.")

if __name__ == "__main__":
    if args.test == "true":
        lines = getLines("test"+args.part+".txt")
    else:
        lines = getLines("input"+args.part+".txt")
    if args.part == "1":
        part1(lines)
    elif args.part == "2":
        part2(lines)
    elif args.part == "3":
        part3(lines)
    else:
        print("Error: Part number invalid: " + args.part)
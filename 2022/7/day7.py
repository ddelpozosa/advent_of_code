import os
from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

### File system builder ### 

class Node(object):
    def __init__(self, size, name, parent = None):
        self.parent = parent
        self.size = size
        self.name = name
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def get_parent(self):
        return self.parent

    def get_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def print_node(self, indentation):
        padding = ' '*indentation
        if self.size == 0:
            print(f'{padding}- {self.name} (dir)')
        else:
            print(f'{padding}- {self.name} (file, size={self.size})')
        for child in self.children:
            child.print_node(indentation + 2)

def getTotalSize(node):
    totalSize = 0
    totalSize += node.size
    for child in node.children:
        totalSize += getTotalSize(child)
    return totalSize

def buildTree(input):
    fileSystem = Node(0,"/")
    currentChild = fileSystem
    for line in input:
        ### Command ###
        if line[0] == '$':
            command = line.strip().split(" ")[1]
            if command == "cd":
                #print("Command cd!")
                childName = line.strip().split(" ")[2]
                if childName == "..":
                    currentChild = currentChild.get_parent()
                    #print("Moved back to folder: " + currentChild.name)
                else:
                    currentChild = currentChild.get_child_by_name(childName)
                    #print(f'Moved into directory: {currentChild.name}')
        else:
            metadata = line.strip().split(" ")[0]
            name = line.strip().split(" ")[1]
            if metadata == "dir":
                #print(f'Creating Dir with name: {name}')
                currentChild.add_child(Node(0,name,currentChild))
            else:
                #print(f'Creating file with name: {name} and size {metadata}')
                currentChild.add_child(Node(int(metadata),name,currentChild))

        

    return fileSystem

fileSystem = buildTree(lines[1:])
fileSystem.print_node(0)

### Part 1 ###
def getPart1(currentNode):
    result = 0
    total = 0
    if currentNode.size == 0:
        result = getTotalSize(currentNode)
        #print(f'{currentNode.name} is a folder with total size: {result}')
        if result < 100000:
            #print(f'{result} is smaller than 100000 so its added to the total')
            total += result
        for child in currentNode.children:
            total += getPart1(child)
    return total

resultPart1 = getPart1(fileSystem)
print(f'The total value of all folders with less than 100000 size is: {resultPart1}')

### Part 2 ###
totalDiskSpace = 70000000
usedSpace = getTotalSize(fileSystem)
neededSpace = 30000000 - (totalDiskSpace - usedSpace)

#print(f'usedSpace: {usedSpace} --- neededSpace: {neededSpace}')
def getPart2(currentNode, neededSpace, smallestNode):
    if currentNode.size == 0:
        result = getTotalSize(currentNode)
        if result > neededSpace and result < smallestNode:
            smallestNode = result
        for child in currentNode.children:
            smallestNode = getPart2(child, neededSpace, smallestNode)
    return smallestNode

resultPart2 =  getPart2(fileSystem, neededSpace, totalDiskSpace)

print(f'The size of the smallest folder that would be free enough space for the update if deleted is: {resultPart2}')
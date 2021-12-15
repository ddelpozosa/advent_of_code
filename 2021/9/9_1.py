file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/9/input1.txt', 'r')
lines = file1.readlines()

surface = []
for line in lines:
    row = []
    for number in line.replace("\n",""):
        row.append(int(number))
    surface.append(row)

totalRisk = 0
for r in range(0,len(surface)):
    for c in range(0,len(surface[0])):
        min = True
        if r-1 >= 0:
            if surface[r-1][c] <= surface[r][c]:
                min = False
        if r+1 < len(surface):
            if surface[r+1][c] <= surface[r][c]:  
                min = False  
        if c-1 >= 0:
            if surface[r][c-1] <= surface[r][c]:
                min = False
        if c+1 < len(surface[0]):
            if surface[r][c+1] <= surface[r][c]:  
                min = False  
        if min == True:
            print(str(surface[r][c]) + " is a minimum!")
            totalRisk += surface[r][c] + 1
print("The total risk is " + str(totalRisk))

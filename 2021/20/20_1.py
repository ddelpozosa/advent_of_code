from os import path
import timeit

def parse_matrix(lines, infinite_char):
    matrix = []
    temp = []
    for line in lines:
        row = [infinite_char]
        for char in line:
            if char == "#":
                row.append("#")
            else:
                row.append(".")
        row.append(infinite_char)
        if len(matrix) == 0:
            for r in row:
                temp.append(infinite_char)
            matrix.append(temp)
        matrix.append(row)
    matrix.append(temp)
    return matrix

def matrix_to_str(matrix):
    txtMat=[]
    for row in matrix:
        txt = ""
        for r in row:
            txt+=str(r)
        txtMat.append(txt)
    return txtMat

deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
def get_result(matrix, row, col, infinite_char):
    rows, cols = len(matrix),len(matrix[0])
    bin_str = ""
    for delta in deltas:
        if row + delta[0] >= 0 and row + delta[0] < rows and col + delta[1] >= 0 and col + delta[1] < cols:
            if matrix[row + delta[0]][col + delta[1]] == "#":
                bin_str += "1"
            else:
                bin_str += "0"
        else:
            if infinite_char == ".":
                bin_str += "0"
            else:
                bin_str += "1"
        
    return int(bin_str,2)


start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "test1.txt"))
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

algorithm = lines[0]

matrix = parse_matrix(lines[2:],".")

print("Original Matrix")

str_matrix = matrix_to_str(matrix)
for line in str_matrix:
    print(line)
print("")

step = 0

while step < 2:
    
    infinite_char = matrix[0][0]
    print("Step " + str(step) + " and the infinite char is: " + infinite_char)
    new_matrix = []
    rows, columns = len(matrix),len(matrix[0])
    for row in range(0,rows):
        new_row = []
        for col in range(0,columns):
            newChar = algorithm[get_result(matrix,row,col,infinite_char)]
            #print("Row: " + str(row) + ". Col: " + str(col) + ". New Char: " + newChar)
            new_row.append(newChar)
        new_matrix.append(new_row)
    
    str_matrix = matrix_to_str(new_matrix)
    if algorithm[0] == "#" and step % 2 == 0:
        matrix = parse_matrix(str_matrix,"#")
    else:
         matrix = parse_matrix(str_matrix,".")
    str_matrix = matrix_to_str(matrix)
    print("New matrix calculated:")
    for line in str_matrix:
        print(line)
    step +=1

total = 0
for row in matrix:
    for item in row:
        if item == "#":
            total += 1
print("After " + str(step) + " steps there are a total of " + str(total) + " pixels lit.")



stop = timeit.default_timer()

print(" ")
print('Time: ', stop - start)  
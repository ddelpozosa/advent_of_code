file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/8/input1.txt', 'r')
lines = file1.readlines()

def sort_str(str):
    return "".join(sorted(str))

def add_str(str1,str2):
    return sort_str("".join(set(str1 + str2))).strip()

def sub_str(str1,str2):
    for letter in str2:
        str1 = str1.replace(letter,"")
    return sort_str(str1)

def common_chars(str1,str2):
    return ''.join(set(str1).intersection(str2))


digitLength = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
uniqueLengths = [2,4,3,7]

outputSum = 0
for line in lines:
    
    digitsParsed = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
    digits = line.split(" | ")[0]
    output = line.split(" | ")[1]
    print(digits)
    #Deduce unique number
    for digit in digits.split(" "):
        if len(digit) in uniqueLengths:
            number = list(digitLength.keys())[list(digitLength.values()).index(len(digit))]
            digitsParsed[number]=sort_str(digit)

    #Find 6
    for digit in digits.split(" "):
        if len(digit) == digitLength[6]:
            for letter in digitsParsed[1]:
                if sub_str(digitsParsed[8],letter) == sort_str(digit):
                    digitsParsed[6]=sort_str(digit) 

    #Find 0
    for digit in digits.split(" "):
        if len(digit) == digitLength[6]:
            for letter in sub_str(digitsParsed[4],digitsParsed[1]):
                if letter not in digit:
                    digitsParsed[0] = sort_str(digit)

    #Find 9
    for digit in digits.split(" "):
        if len(digit) == digitLength[6]:
            if sort_str(digit) not in list(digitsParsed.values()):
                digitsParsed[9] = sort_str(digit)

    #Find 5
    digitsParsed[5] = sort_str(common_chars(digitsParsed[6],digitsParsed[9]))

 
    #Find 2
    for digit in digits.split(" "):
        if len(digit) == digitLength[5]:
            if sort_str(digit) not in list(digitsParsed.values()):
                for letter in digitsParsed[1]:
                    if letter not in digit:
                        digitsParsed[2]=sort_str(digit)

    #Find 3
    for digit in digits.split(" "):
        if len(digit) == digitLength[5]:
            if sort_str(digit) not in list(digitsParsed.values()):
                digitsParsed[3] = sort_str(digit)
    #digitsParsed[9] = add_str(digitsParsed[4],digitsParsed[7])
    print(digitsParsed)

    #decode output

    outputTotal = ""
    for outputDigit in output.split(" "):
        outputTotal += str(list(digitsParsed.keys())[list(digitsParsed.values()).index(sort_str(outputDigit).replace("\n",""))])
        
    print("Output: " + outputTotal)
    outputSum += int(outputTotal)

print("The total sum of all outputs is " + str(outputSum))

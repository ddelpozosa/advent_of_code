file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/3/input1.txt', 'r')
lines = file1.readlines()

gammaRate = ""
epsilonRate = ""

for i in range(0,len(lines[0])-1):
    digitSum = 0
    for line in lines:
        if line[i] == "1":
            digitSum += 1
        else:
            digitSum -= 1
    if digitSum >= 0:
        gammaRate += "1"
    elif digitSum < 0:
        gammaRate += "0"

for digit in gammaRate:
    if digit == "1":
        epsilonRate += "0"
    else:
        epsilonRate += "1"

electricityConsumption = int(gammaRate, 2) * int(epsilonRate, 2)

print("Gamma Rate: " + gammaRate)
print("Epsilon Rate: " + epsilonRate)
print("Electricity Consumption: " + str(electricityConsumption))



#Position for oxygen calculation
print("Calculating Oxygen")
oxygenSet = lines
oxygenRate = ""
for i in range(0,len(lines[0])-1):

    #calculating the most common digit for that position
    digitSum = 0
    mostCommonDigit = ""
    for line in oxygenSet:
        if line[i] == "1":
            digitSum += 1
        else:
            digitSum -= 1
    if digitSum >= 0:
        mostCommonDigit = "1"
    elif digitSum < 0:
        mostCommonDigit = "0"
    print("The most common digit for position " + str(i+1) + " is " + mostCommonDigit)
    newOxygenSet = []
    for line in oxygenSet:
        if line[i] == mostCommonDigit:
            print(line.strip() + " has a " + mostCommonDigit + " in position " + str(i+1) + ". Saving...")
            newOxygenSet.append(line)
    if len(newOxygenSet) == 0:
        print("We run out of numbers to match the condition. Taking last number:")
        oxygenRate = oxygenSet[-1]
        break
    elif len(newOxygenSet) == 1:
        oxygenRate = newOxygenSet[0]
        break
    oxygenSet = newOxygenSet

print("Calculating C02")
co2Set = lines
c02Rate = ""
for i in range(0,len(lines[0])-1):

    #calculating the most common digit for that position
    digitSum = 0
    mostCommonDigit = ""
    for line in co2Set:
        if line[i] == "1":
            digitSum += 1
        else:
            digitSum -= 1
    if digitSum >= 0:
        mostCommonDigit = "0"
    elif digitSum < 0:
        mostCommonDigit = "1"
    print("The least common digit for position " + str(i+1) + " is " + mostCommonDigit)
    newCo2Set = []
    for line in co2Set:
        if line[i] == mostCommonDigit:
            print(line.strip() + " has a " + mostCommonDigit + " in position " + str(i+1) + ". Saving...")
            newCo2Set.append(line)
    if len(newCo2Set) == 0:
        print("We run out of numbers to match the condition. Taking last number:")
        c02Rate = co2Set[-1]
        break
    elif len(newCo2Set) == 1:
        c02Rate = newCo2Set[0]
        break
    co2Set = newCo2Set

print("Oxygen Rate : " + oxygenRate.strip() + " --- Decimal: " + str(int(oxygenRate,2)))
print("CO2 Rate : " + c02Rate.strip() + " --- Decimal: " + str(int(c02Rate,2)))
print("Life Support Rating : " + str(int(oxygenRate,2) * int(c02Rate,2)) )
            




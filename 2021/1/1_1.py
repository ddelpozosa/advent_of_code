file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/1/input1.txt', 'r')
lines = file1.readlines()
 
lastMeasurement = 0
increaseCount = 0
window=[]
# Strips the newline character
for line in lines:

    currentMeasurement = int(line)
    
    if len(window) < 3:
        window.append(currentMeasurement)
    else:
        del window[0]
        window.append(currentMeasurement)
        if lastMeasurement > 0 and sum(window) > lastMeasurement:
                increaseCount += 1
    lastMeasurement = sum(window)
    
print(increaseCount)




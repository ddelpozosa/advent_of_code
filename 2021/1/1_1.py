import os

from pathlib import Path

p = Path(__file__).with_name('input1.txt')
with p.open('r') as f:
    lines = f.readlines()
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




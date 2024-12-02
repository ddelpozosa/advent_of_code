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

def getReports(lines):
    reports = []
    for line in lines:
        report = []
        for level in line.split():
            report += [int(level)]
        reports += [report]
    return reports

def removeIndex(report, i):
    newReport = report.copy()
    del newReport[i]
    return newReport

def isReportSafe(report):
    printtest("Analyzing report: " + str(report))
    if sorted(report) != report and sorted(report, reverse=True) != report:
        printtest("The report is not all increasing or decreasing. Not safe")
        return False

    prev_level = report[0]
    for level in report[1:]:
        dif = abs(level-prev_level)
        if dif < 1 or dif > 3:
            printtest("Diff for " + str(prev_level) + " and " + str(level) + " is either 0 or > 3. ")
            return False
        prev_level = level
    printtest("Report is safe")
    return True

#Solution to Part 1
def part1(lines):
    reports = getReports(lines)
    safe_count = 0
    for report in reports:
        if isReportSafe(report):
            safe_count += 1
    print("There are " + str(safe_count) + " safe reports.")

#Solution to Part 2
def part2(lines):
    reports = getReports(lines)
    safe_count = 0
    for report in reports:
        if isReportSafe(report):
            safe_count += 1
        else:
            for i in range(0,len(report)):
                if isReportSafe(removeIndex(report,i)) == True:
                    printtest("After removing " + str(i) + " report actually becomes safe")
                    safe_count += 1
                    break
    print("There are " + str(safe_count) + " safe reports.")

if __name__ == "__main__":
    if args.test == "true":
        lines = getLines("test"+args.part+".txt")
    else:
        lines = getLines("input"+args.part+".txt")
    if args.part == "1":
        part1(lines)
    elif args.part == "2":
        part2(lines)
    else:
        print("Error: Part number invalid: " + args.part)
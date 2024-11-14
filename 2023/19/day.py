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
#rule -> symbol, sign, value 
#workflow = {"workflow1":[rules]}

def parseWorkflows(lines):
    workflows = {}
    for line in lines:
        workflow_name = line.split("{")[0]
        rules = []
        raw_rules = line.split("{")[1].split("}")[0].split(",")
        for rule in raw_rules:
            if ":" in rule: ### complex rule
                dest = rule.split(":")[1]
                if "<" in rule:
                    cond = "<"
                    value = rule.split("<")[1].split(":")[0]
                    unit = rule.split("<")[0]
                if ">" in rule:
                    cond = ">"
                    value = rule.split(">")[1].split(":")[0]
                    unit = rule.split(">")[0]
                rules += [[unit,cond,int(value),dest]]
            else: ## simple "else" rule
                rules += [[rule]]
        workflows[workflow_name] = rules
    
    return workflows

def parseParts(lines):
    parts = []
    for line in lines:
        part = {}
        attributes = line.split("{")[1].split("}")[0].split(",")
        for attribute in attributes:
            unit = attribute.split("=")[0]
            value = int(attribute.split("=")[1])
            part[unit] = value
        parts += [part]
    return parts

def parseAll(lines):
    workflowText = []
    partsText = []
    begin = True
    for line in lines:
        if line.strip() == "":
            begin = False
        elif begin == True:
            workflowText += [line.strip()]
        else:
            partsText += [line.strip()]
    workflows = parseWorkflows(workflowText)
    parts = parseParts(partsText)
    return workflows,parts

def analyzePart(workflows,part,currentWorkflow = "in", path = []):
    path += [currentWorkflow]

    if currentWorkflow == "A" or currentWorkflow == "R":
        return currentWorkflow,path
    
    workflow = workflows[currentWorkflow]
    for rule in workflow:
        if len(rule) != 1:
            if rule[1] == "<":
                if part[rule[0]] < rule[2]:
                    return analyzePart(workflows,part,rule[3],path)
            elif rule[1] == ">":
                if part[rule[0]] > rule[2]:
                    return analyzePart(workflows,part,rule[3],path)
            else:
                raise Exception("rule not supported")
            
        else: ##else condition (rule length is 1, just the workflow)
            return analyzePart(workflows,part,rule[0],path)

    return None

#Solution to Part 1
def part1(lines):

    workflows,parts = parseAll(lines)
    count = 0
    for part in parts:
        decision,path = analyzePart(workflows,part,"in",[])
        printtest("part: " + str(part) + " has been: " + decision + " following this workflow path: " + str(path))
        if decision == "A":
            for att in part:
                count += part[att]
    print("The sum of all attributes of accepted parts is: " + str(count))
#Solution to Part 2
def part2(lines):
        
    print(lines)

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
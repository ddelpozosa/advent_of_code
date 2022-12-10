import os
from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

class Chain(object):
    def __init__(self, numberOfLinks):
        self.visited_nodes = set()
        self.links = []
        self.links.append(Link("H"))
        if numberOfLinks == 2:
            self.links.append(Link("T"))
        else:
            for i in range(1,numberOfLinks):
                self.links.append(Link(i))
    def move_chain(self, x_mov, y_mov):
        link = self.links[0].move_head(x_mov,y_mov)
        for i in range(1,len(self.links)):
            link = self.links[i].move_link(link)
        self.visited_nodes.add(tuple([self.links[-1].x,self.links[-1].y]))
        #print(f'New node visited: {tuple([self.links[-1].x,self.links[-1].y])}')
   
    def get_name(self, x, y):
        for link in self.links:
            if link.x == x and link.y == y:
                return link.name
        return "."
    
    def print_chain(self):
        output = ""
        max_x, min_x, max_y, min_y = 0,0,0,0
        for link in self.links:
            if link.x < min_x:
                min_x = link.x
            if link.x > max_x:
                max_x = link.x
            if link.y < min_y:
                min_y = link.y
            if link.y > max_y:
                max_y = link.y
        #print(f'{min_x}{min_x}{max_y}{min_y}')
        for i in range(min_x, max_x+1):
            for j in range(min_y, max_y+1):
                if i == 0 and j == 0 and str(self.get_name(i,j)) == ".":
                    output += "s"
                else:
                    output += str(self.get_name(i,j))
                output += " "
            output += "\n"
        print(output)

class Link(object):
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0


    def move_head(self, mov_x, mov_y):
        self.x += mov_x
        self.y += mov_y
        return self

    def move_link(self, parent_link):
        
        ##horizontal movemnt
        if abs(parent_link.x-self.x) > 1 and abs(parent_link.y-self.y) == 0:
            if parent_link.x > self.x:
                self.x = parent_link.x - 1
            else:
                self.x = parent_link.x + 1

        ##vertical movement
        if abs(parent_link.y-self.y) > 1 and abs(parent_link.x-self.x) == 0:
            if parent_link.y > self.y:
                self.y = parent_link.y - 1
            else:
                self.y = parent_link.y + 1
        
        ##diagonal movement
        elif abs(parent_link.x-self.x) > 1 or abs(parent_link.y-self.y) > 1:
            if parent_link.x > self.x and parent_link.y > self.y:
                self.x += 1
                self.y += 1
            elif parent_link.x > self.x and parent_link.y < self.y:
                self.x += 1
                self.y += -1
            elif parent_link.x < self.x and parent_link.y > self.y:
                self.x += -1
                self.y += 1
            elif parent_link.x < self.x and parent_link.y < self.y:
                self.x += -1
                self.y += -1
        return self


def order_chain(chain: Chain, order):
    if order == "U":
        #print("Moving UP")
        chain.move_chain(-1,0)

    elif order == "R":
        #print("Moving RIGHT")
        chain.move_chain(0,1)

    elif order == "D":
        #print("Moving DOWN")
        chain.move_chain(1,0)
    elif order == "L":
        #print("Moving LEFT")
        chain.move_chain(0,-1)
    return chain

chain = Chain(10)

for i, line in enumerate(lines):
    #print(f'Step {i} -- {line}')
    order = line.strip().split(" ")[0]
    amount = int(line.strip().split(" ")[1])
    #print(f'=== {line.strip()} ===')
    for time in range(amount):
        order_chain(chain,order)
        #chain.print_chain()

print(f'{len(chain.visited_nodes)} nodes have been visited by the tail.')
#print(chain.visited_nodes)


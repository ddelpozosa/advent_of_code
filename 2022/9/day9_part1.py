import os
from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

class Cell(object):
    def __init__(self, tail=False, head=False, visited = False):
        self.tail = tail
        self.head = head
        self.visited = visited
    
    def get_cell_string(self):
        if self.head == True:
            return "H"
        elif self.tail == True:
            return "T"
        else:
            return "."

class Board(object):
    def __init__(self):
        self.cells = []
        row = []
        row.append(Cell(True, True, True))
        self.cells.append(row)
    
    def get_head(self):
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell.head == True:
                    return i,j
        return -1,-1 ### in case of error (head not found)
    
    def get_tail(self):
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell.tail == True:
                    return i,j
        return -1,-1 ### in case of error (tail not found)
    
    def increase_board(self,i,j):
        final_i = i
        final_j = j
        if i == -1:
            new_row = []
            for col in self.cells[0]:
                new_row.append(Cell())
            self.cells.insert(0,new_row)
            final_i = 0
        elif j == -1:
            for i, row in enumerate(self.cells):
                self.cells[i].insert(0,Cell())
            final_j = 0
        elif i == len(self.cells):
            new_row = []
            for col in self.cells[0]:
                new_row.append(Cell())
            self.cells.append(new_row)
        elif j == len(self.cells[0]):
            for i, row in enumerate(self.cells):
                self.cells[i].append(Cell())

        return final_i, final_j

    def move_head(self, init_i, init_j, dest_i, dest_j):
        if dest_i >= 0 and dest_j >= 0 and dest_i < len(self.cells) and dest_j < len(self.cells[0]):
            self.cells[init_i][init_j].head = False
            self.cells[dest_i][dest_j].head = True
        else:
            #print("OUT OF BOUNDS. Making the board larger...")
            self.cells[init_i][init_j].head = False
            dest_i, dest_j = self.increase_board(dest_i,dest_j)
            self.cells[dest_i][dest_j].head = True

            

    def move_tail(self, i,j):
        head_i, head_j = self.get_head()
        tail_i, tail_j = self.get_tail()

        if abs(head_i-tail_i) > 1 or abs(head_j-tail_j) > 1:
            self.cells[tail_i][tail_j].tail = False
            self.cells[head_i+i][head_j+j].tail = True
            self.cells[head_i+i][head_j+j].visited = True

    def print_board(self):
        output = ""
        for row in self.cells:
            for cell in row:
                output += cell.get_cell_string()
                output += " "
            output += "\n"
        print(output)

    def get_visited_cells(self):
        nOfVisitedCells = 0
        for row in self.cells:
            for cell in row:
                if cell.visited == True:
                    nOfVisitedCells += 1
        return nOfVisitedCells

def moveCell(board: Board, order):
    head_i, head_j = board.get_head()
    if order == "U":
        #print("Moving UP")
        board.move_head(head_i, head_j, head_i - 1, head_j)
        board.move_tail(1,0)

    elif order == "R":
        #print("Moving RIGHT")
        board.move_head(head_i, head_j, head_i, head_j + 1)
        board.move_tail(0,-1)

    elif order == "D":
        #print("Moving DOWN")
        board.move_head(head_i, head_j, head_i + 1, head_j)
        board.move_tail(-1,0)
    elif order == "L":
        #print("Moving LEFT")
        board.move_head(head_i, head_j, head_i, head_j - 1)  
        board.move_tail(0,1)
    return board


### Init array ###
board = Board()

#print("INITIAL POSITION")
#board.print_board()

for i, line in enumerate(lines):
    print(f'Step {i} -- {line}')
    order = line.strip().split(" ")[0]
    amount = int(line.strip().split(" ")[1])
    #print(f'=== {line.strip()} ===')
    for time in range(amount):
        moveCell(board,order)
        #board.print_board()
        
nOfVisitedCells = board.get_visited_cells()

print(f'A total of {nOfVisitedCells} cells have been visited by the tail of the rope at least once.')
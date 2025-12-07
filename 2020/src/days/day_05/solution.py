from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 820, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": None}
]

def parse(data):
    bin_ids = parse_lines(data)
    return bin_ids

def get_sit_position(id):
    id = id.replace("F","0").replace("B","1").replace("R","1").replace("L","0")
    row_set = int(id[:7],2)
    column_seat = int(id[7:],2)
    debug(id,": row ", row_set, ", column " , column_seat, ", seat ID ", row_set*8 + column_seat)
    return row_set, column_seat

def get_sit_id(row_set,column_seat):
    return row_set*8 + column_seat 

def to_bin_id(raw_bin_1, raw_bin_2):
    raw_bin_1 = raw_bin_1.replace("0","F").replace("1","B")
    raw_bin_2 = raw_bin_2.replace("1","R").replace("0","L")
    return raw_bin_1 + raw_bin_2

# Clues: 
#  1. The only missing Id in the plane
#  2. Our row will be totally filled except one (7 seats in the row)

def get_my_sit_id(bin_ids):
    # First, we get the number of filled seats per row
    filled_rows = defaultdict(int)
    for bin_id in bin_ids:
        row_set, column_seat = get_sit_position(bin_id)
        filled_rows[row_set] += 1
    for row in filled_rows:
        # We look for the row missing one seat
        if filled_rows[row] == 7:
            my_row = int(row)
            # Found our row! Now check all Ids and look for the missing one
            for i in range(1,9):
                bin_id = to_bin_id(f'{my_row:07b}',f'{i:03b}')
                # Found our seat (in airline format)! Now convert back to seat_id
                if bin_id not in bin_ids:
                    row_seat, column_seat = get_sit_position(bin_id)
                    seat_id = get_sit_id(row_seat, column_seat)
                    print("Success: ", bin_id," (",seat_id,")")
                    return seat_id
    return -1 # Seat not found

def part1(data):
    bin_ids = parse(data)
    max = 0
    for bin_id in bin_ids:
        row_seat, column_seat = get_sit_position(bin_id)
        seat_id = get_sit_id(row_seat, column_seat)
        if seat_id > max:
            max = seat_id
    return max

def part2(data):
    bin_ids = parse(data)
    return get_my_sit_id(bin_ids)

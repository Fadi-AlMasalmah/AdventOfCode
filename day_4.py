
###### Q1 ##########
# problem summary: count XMAS in a 2D grid of characters, check all 8 directions.
# solution idea: from each cell in the 2D grid, test the 8 directions and see if it has XMAS in that direction. 


data = []
with open("input_4.txt", "r") as f:
    for line in f:
        parts = list(line.strip())
        data.append(parts)

n = len(data)
m = len(data[0])
directions = [(1, 0), (1, 1), (0,1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)] 

def is_valid(i,j):
    ''' Check if the index (i,j) is valid in the 2D grid '''
    return i >= 0 and i < n and j >= 0 and j < m

def step_in_direction(steps , direction):
    ''' Step in the given direction (dx, dy) for the given number of steps '''
    return steps * direction[0], steps * direction[1]

def count_xmas_at_ij(i, j, data):
    ''' Count the number of XMAS starting from (i,j) in all 8 directions '''
    res = 0
    if data[i][j] == 'X':
        for dir in directions:
            str = "X"
            for k in range(1,4):
                ni, nj = step_in_direction(k, dir)
                if is_valid(i + ni, j + nj):
                    str += data[i + ni][j + nj]
                else:
                    break
            if str == "XMAS":
                res += 1
    return res

xmas_count = 0
for i in range(n):
    for j in range(m):
        xmas_count += count_xmas_at_ij(i, j, data)

print(f"Q1: The number of XMAS is: {xmas_count}")


########## Q2 ##########

# Problem summary: Recognize (MAS,MAS) located in an X pattern, each one could be forwards or backwards
# solution idea: check the diagonal and anti-diagonal directions for each A in the grid, and check if there is a MAS in that direction.

def is_MAS_diag(i, j, data):
    ''' Check if there is a MAS in the diagonal direction starting from A at (i,j) '''
    if not (i > 0 and i < n-1 and j > 0 and j < m-1):
        return False
    if data[i][j] != 'A':
        return False
    if data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S':
        return True
    if data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M':
        return True
    return False

def is_MAS_antidiag(i, j, data):
    ''' Check if there is a MAS in the anti-diagonal direction starting from A at (i,j) '''
    if not (i > 0 and i < n-1 and j > 0 and j < m-1):
        return False
    if data[i][j] != 'A':
        return False
    if data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S':
        return True
    if data[i-1][j+1] == 'S' and data[i+1][j-1] == 'M':
        return True
    return False

def is_MAS(i, j, data):
    ''' Check if there is a MAS in the diagonal or anti-diagonal direction starting from A at (i,j) '''
    return is_MAS_diag(i, j, data) and is_MAS_antidiag(i, j, data)

count_MAS = 0

for i in range(n):
    for j in range(m):
        if is_MAS(i, j, data):
            count_MAS += 1

print(f"Q2: The number of MAS is: {count_MAS}")


                



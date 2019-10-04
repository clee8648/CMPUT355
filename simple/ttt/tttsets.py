# bitset ttt program

import numpy as np

# Cells    0  1  2
#          3  4  5
#          6  7  8

Empty, Black, White = -1, 0, 1
Num_Cells = 9
Num_Lines = 8
EmptySet = 0  # interpret integer as 9-element bitset
R0, R1, R2, C0, C1, C2, D0, D1 = 0, 1, 2, 3, 4, 5, 6, 7

Board  = np.array([Empty] * Num_Cells)
Powers = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256])  # for setting bitset values
Lines  = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8],
                   [0, 3, 6], [1, 4, 7], [2, 5, 8],
                   [0, 4, 8], [2, 4, 6]])
LinesOfCell = [np.array([R0, C0, D0]), np.array([R0, C1]),      np.array([R0, C2, D1]),
               np.array([R1, C0]),     np.array([R1, C1, D0, D1]),  np.array([R1, C2]),
               np.array([R2, C0, D1]), np.array([R2, C1]),      np.array([R2, C2, D0])]

Line_Sums = np.array([ [0] * Num_Cells, [0] * Num_Cells ])  # for Black, White

def addStone(B, c, color):
  assert(B[c] == Empty)
  for ll in LinesOfCell[c]:
     LineSets[color][ll] |= Powers[c]

print(Lines)
print(Powers)
print(Board)
print(LinesOfCell)
print(LineSets)
addStone(Board, 0, Black)
addStone(Board, 4, Black)
addStone(Board, 8, Black)
print(LineSets)
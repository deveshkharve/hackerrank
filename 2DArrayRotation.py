"""
    rotate a given matrix n times in anticlockwise direction
    https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
    difficulty: Hard, section: algorithms
    
You are given a 2D matrix of dimension (m x n) and a positive integer 'r'. You have to rotate the matrix  times and print the resultant matrix. Rotation should be in anti-clockwise direction.

Rotation of a (4 x 4)  matrix is represented by the following figure. Note that in one rotation, you have to shift elements by one step only.
It is guaranteed that the minimum of m and n will be even.
As an example rotate the Start matrix by 2:
    
    Start               First               Second
    1   2   3   4       2   3   4   5       3   4   5   6
    12  1   2   5  ->   1   2   3   6  ->   2   3   4   7
    11  4   3   6       12  1   4   7       1   2   1   8
    10  9   8   7       11  10  9   8       12  11  10  9

"""



"""
Solution:

we are given a matrix which needs to be rotated r times. 

BASIC APPROACH:
the basic solution requires us to rotate the matrix once r times to get the solution. for this we need to rotate each ring once.
1 replace the first left element with the fiest element, start by sliding items from the first column down, save the last element replaced and use in next step
2 start with last saved element, slide items from the last row to right, save the last element replaced and use in next step
3 start with last saved element, slide items from the last column up, save the last element replaced and use in next step
4 start with last saved element, slide items left from first row left.
move to the inner rings, by reducing the top, bottom, left and right and perform the same operation.


OUR APPROACH:
we rotate each ring one by one. we fix the number of rotation of each ring by calculating the modulo of roatation count with the perimeter of the ring. and rotate the rings with this new roatation count.
algo:

while we have a ring to rotate:
    p = 2(length + width) // check the perimter of the ring
    r = r % p // calculate effective roatation required
    for i=1....r:
        rotate ring by 1

"""
def matrixRotation(matrix, r):
    rows = len(matrix)
    cols = len(matrix[0])

    first = 0
    last = rows - 1
    left = 0
    right = cols - 1
    ringNumber = 0
    # rotate each ring, until the last ring is reached
    while left < right and first < last:
        # number of rotation for each ring
        # number of elements in ring
        print('element count = ', 2 * (right-left + last - first))
        n = r%(2 * (right-left + last - first))
        for counter in range(n):
            # slide items from the first column down, save the last element replaced and use in next step
            temp = matrix[first][left+1]
            for i in range(first, last):
                curr = matrix[i][left]
                matrix[i][left] = temp
                temp = curr

            # start with last saved element, slide items from the last row to right, save the last element replaced and use
            # in next step
            for j in range(left, right):
                curr = matrix[last][j]
                matrix[last][j] = temp
                temp = curr

            # start with last saved element, slide items from the last column up, save the last element replaced and use in
            # next step
            for i in range(last, first, -1):
                curr = matrix[i][right]
                matrix[i][right] = temp
                temp = curr

            # start with last saved element, slide items left from first row left.
            for j in range(right, left, -1):
                curr = matrix[first][j]
                matrix[first][j] = temp
                temp = curr
        # move to the inner rings, by reducing the top, bottom, left and right
        left += 1
        right -= 1
        first += 1
        last -= 1
        ringNumber += 1

    for row in matrix:
        print(" ".join(map(str, row)))


# my_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# rotation_count = 12
# m = 4
# n = 4
# m = matrixRotation(my_matrix, rotation_count)

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)

"""
    rotate a given matrix n times in anticlockwise direction
    https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
    difficulty: Hard, section: algorithms
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

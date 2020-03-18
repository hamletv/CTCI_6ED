'''Given a m * n matrix grid which is sorted in non-increasing order both
row-wise and column-wise. Return the number of negative numbers in grid.'''


def countNegatives(grid):
        return len([num for row in grid for num in row if num < 0])


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))

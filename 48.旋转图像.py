# coding=utf-8
"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


def rotate(matrix):
    """
    之前做的189题，根据这题想到先反转matrix[i]；之后自己又苦想的再正斜杠对角线镜像反转。
    耗时3小时，打败99.62%
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    for i in matrix:
        i.reverse()
    # p(matrix)

    for i in range(1, len(matrix)):
        for j in range(len(matrix)-i, 0, -1):
            matrix[i-1][j-1], matrix[-j][-i] = matrix[-j][-i], matrix[i-1][j-1]


def rotate1(matrix):
    """
    先正斜杠对角线镜像反转，再反转matrix[i]，逻辑上更好想
    """
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in matrix:
        i.reverse()


def p(matrix):
    for i in matrix:
        print i
    print '\n'


if __name__ == "__main__":
    matrix1 =[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 =[
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    rotate1(matrix1)
    p(matrix1)
# coding=utf-8
"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1:
输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true

示例 2:
输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

说明:
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。
"""


def is_valid_sudoku(board):
    """
    真复杂，写了2小时，战胜43.62%。
    :type board: List[List[str]]
    :rtype: bool
    """
    dict_column = {}  # 列的集合
    for a in range(9):
        dict_column[a] = []
    dict_block = {}  # 3X3方块的集合
    for b in range(9):
        dict_block[b] = []

    for i in range(len(board)):
        for j in range(len(board)):
            # 判断行
            if (board[i][j] != '.') and (board[i].count(board[i][j]) > 1):
                return False
            # 装填dict_column
            dict_column[j].append(board[i][j])
        # 装填dict_block
        for k in range(3):
            dict_block[i/3+k+i/3*2].extend(board[i][3*k:3*k+3])

    # 判断列
    for column in dict_column.values():
        for x in range(8):  # 最后一个必定不会重复，所以不用判断
            if (column[x] != '.') and (column.count(column[x]) > 1):
                return False
    # 判断3X3方块
    for block in dict_block.values():
        for y in range(8):
            if (block[y] != '.') and (block.count(block[y]) > 1):
                return False
    return True


def is_valid_sudoku1(board):
    """官方解法
    :type board: List[List[str]]
    :rtype: bool
    """
    # init data
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]

    # validate a board
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3) * 3 + j // 3

                # keep the current cell value
                rows[i][num] = rows[i].get(num, 0) + 1
                print rows[i][num]
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                # check if this value has been already seen before
                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False
    return True


if __name__ == "__main__":
    a=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    b=[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print is_valid_sudoku1(a)
    print is_valid_sudoku1(b)

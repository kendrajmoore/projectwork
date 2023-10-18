from collections import collections

from requests import head

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def is_valid(s):
    stack = []
    m = {
        "]":"[",
        "}":"{",
        ")":"("
    }
    for i in s:
        if i not in m:
            stack.append(i)
            continue
        if not stack or stack[-1] != m[i]:
            return False
        stack.pop()
    return not stack
        

print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))

def valid(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if [r][c] == '.':
                continue
            if board[r][c] in rows[r] or board[r][c] in cols or board[r][c] in squares[(r // 3, c // 3)]:
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True

def buy(lst):
    result = 0
    lowest = lst[0]
    for i in lst:
        if i < lowest:
            lowest = i
        result = max(result, i - lowest)
    return result

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

def reverse_lst(lst):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

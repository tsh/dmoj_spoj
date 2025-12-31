import sys

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.candy = 0

def read_tree(line):
    pos = 0
    def parse_tree():
        nonlocal pos
        node = Node()
        if line[pos] == '(':
            pos+= 1  # skip (
            node.left = parse_tree()
            pos+= 1
            node.right = parse_tree()
            pos+= 1  # skip )
        else:
            node.candy = int(line[pos])
            pos += 1
            if line[pos] != ' ' and line[pos] != ')':
                node.candy = node.candy * 10 + int(line[pos])
                pos += 1
        return node
    return parse_tree()

def walk(node):
    if node is None:
        return 0
    if node.candy:
        return node.candy
    res = 0
    res += walk(node.left)
    res += walk(node.right)
    return res

def num_streets(node):
    if not node.left and not node.right:
        return 0
    return num_streets(node.left) + num_streets(node.right) + 4

def height(node):
    if not node.left and not node.right:
        return 0
    return 1 + max(height(node.left), height(node.right))

# ((1 5) 8)
for line in sys.stdin.readlines():
    tree = read_tree(line)
    candies = walk(tree)
    n = num_streets(tree) - height(tree)
    print(f'{n} {candies}')

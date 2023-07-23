import sys

sys.stdin = open('test.txt','r')
n = int(input())
"""
class Node:
    def __init__(self,root,left, right):
        self.root = root
        self.left = left
        self.right = right
"""
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left,right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end = '')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')
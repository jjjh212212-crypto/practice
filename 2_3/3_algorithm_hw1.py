class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)



for t in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        root  = node(1)
        if len(arr[i]) > 2:
            root.left=arr[i][2]
            if len(arr[i]) == 4:
                root.right=arr[i][3]
        




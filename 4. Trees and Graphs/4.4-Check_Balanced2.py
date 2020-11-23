from graph import Node

def checkBalanced(node) -> bool:
    if findDiffHeight(node) < 0:
        return False
    return True

def findDiffHeight(node):
    #post-order traversal with extra steps
    if node:
        L = findDiffHeight(node.left)  + 1
        R = findDiffHeight(node.right) + 1
        if L == -1 or R == -1 or abs(L - R) > 1:
            return -2
        return max(L, R)
    return -1

if __name__ == "__main__":
    test = Node(0, 
                Node(1, 
                    Node(2,
                        Node(3)),
                Node(37))
                )

    test2 = Node(1,
                Node(2),
                Node(3)
                )

    assert(checkBalanced(test) == False)
    assert(checkBalanced(test2) == True)


        
    
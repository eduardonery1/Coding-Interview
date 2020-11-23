from graph import Node

def findHeight(node, height=0) -> int:
    if node:
        height += 1
        left_height = findHeight(node.left, height=height)
        right_height = findHeight(node.right, height=height)
        return max(left_height, right_height)
    return height

def isBalanced(node, balanced_left=True, balanced_right=True) -> bool:
    #               1
    #           2       3
    #       4      6        5       
    #                 7     
    #
    left_height = findHeight(node.left)
    right_height = findHeight(node.right)

    if not abs(left_height - right_height) > 1:
        if node.left:
            balanced_left = isBalanced(node.left)
        if node.right:
            balanced_right = isBalanced(node.right)

        return balanced_left and balanced_right

    return False

if __name__=="__main__":
    test = Node(1, 
                Node(2, 
                    Node(4), 
                    Node(6, 
                        right=Node(7))),
                Node(3, 
                    right=Node(5, 
                        Node(8))))

    test2 = Node(1, 
                left=Node(2, 
                    left=Node(4), 
                    right=Node(6, 
                        right=Node(7))),
                right=Node(3, 
                    right=Node(5)))
    
    assert(isBalanced(test)==False)
    assert(isBalanced(test2)==True)
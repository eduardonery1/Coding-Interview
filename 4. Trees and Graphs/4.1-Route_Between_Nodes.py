from graph import Node

def route(node, targetNode):
    from collections import deque
    queue = deque()
    queue.append(node)
    while queue:
        current = queue.popleft()
        if current == targetNode:
                return True
        current.marked = True
        for child in current.children:
            if not child.marked: 
                queue.append(child)
    return False


if __name__=="__main__":

    targetTrue = Node(4)
    targetFalse = Node(0)
    test = Node(1, children=[Node(2), Node(3), Node(4, children=[Node(6), Node(3), Node(90, children=[targetTrue])])])

    print(route(test, targetTrue))
    print(route(test, targetFalse))


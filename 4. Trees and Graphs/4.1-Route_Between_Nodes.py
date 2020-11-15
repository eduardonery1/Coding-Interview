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

        
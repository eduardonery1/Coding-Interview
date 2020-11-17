from graph import Node
from LinkedList.linkedlist import Node as ListNode

lists = {}

def listofDepths(node, depth=0):
    #DFS 
    #           1           d1
    #       2       3       d2
    #   4       5 6     7   d3
    if depth not in lists:
        head = ListNode(node)
        tail = head
        lists[depth] = [head, tail]
    else:
        tail = lists[depth][1]
        tail.next = node
        tail = tail.next

    if node.left:
        listofDepths(node.left, depth=depth+1)
    if node.right:
        listofDepths(node.right, depth=depth+1)

    
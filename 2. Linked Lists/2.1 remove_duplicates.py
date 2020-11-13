import linkedlists 
from random import randint

def llist_gen(size=5):
    l = linkedlists.LinkedList(None)
    value = [randint(1, 10) for val in range(size)]
    gen = False
    for val in value:
        if gen == False:
            l = linkedlists.LinkedList(linkedlists.Node(val))
            gen = True
        else:
            l.append(linkedlists.Node(val))
    return l
            
def llist_printer(llist):
    current = llist.data
    while current:
        if current is llist.data:
            print(current.data, " -> ", end=None)
        else:
            print(current.data.data, " -> ", end=None)
        current = current.next

def remove_dubs(llist):
    mem = {}
    mem[llist.data.data] = None
    current = llist.data.next
    prev = None
    while current:
        if current.data.data in mem:
            current = prev
            current.next = current.next.next
        else:
            mem[current.data.data] = None
        prev = current
        current = current.next

def remove_dubs_nobuffer(llist):
    p1 = llist
    p2 = p1.data.next
    prev = p1
    while p1 and p2:
        while p2:
            if p1.data.data == p2.data.data:
                if prev is not None:
                    prev.next = p2.next
                p2 = p2.next
                continue
            prev = p2
            p2 = prev.next
        p1 = p1.next
        p2 = p1.next
        prev = p1


if __name__=="__main__":
    linked = llist_gen()
    llist_printer(linked)
    print("#"*30)
    remove_dubs_nobuffer(linked)
    llist_printer(linked)
    

    

        
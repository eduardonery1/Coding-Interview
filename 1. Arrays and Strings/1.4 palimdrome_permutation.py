def palimdrome_perm(string):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    string = string.replace(" ", "")
    string = string.lower()
    mem = {}
    odds = 0
    for i in string:
        if i not in mem:
            mem[i] = 1
        else:
            mem[i] += 1
        if mem[i] % 2 == 0:
            odds -= 1
        else:
            odds += 1
    return odds <= 1

def palimdrome_perm_bit(string):
    """
    Voltar depois que estudar bitshifting
    """
    string = string.replace(" ", "")
    string = string.lower()
    mask = 0

    for i in string:
        mask ^= (1 << ord(i))
    checker = mask - 1

    if len(string) % 2 == 0:
        return checker and mask
    else:
        return not (checker and mask)

if __name__=="__main__":
    assert(palimdrome_perm("Tact Coa")==True)
    assert(palimdrome_perm("Tac Coa")==False)
    
    assert(palimdrome_perm_bit("Tact Coa")==True)
    assert(palimdrome_perm_bit("Tact Co")==False)

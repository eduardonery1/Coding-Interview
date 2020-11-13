def isunique(string: str):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    memory = {}
    for letter in string:
        if letter in memory:
            return False
        memory[letter] = None
    return True

def isunique_constantspace(string: str):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(string) > 128: return False
    o = ord
    book = []
    for i in string:
        idx = o(i)
        for i in range(len(book), idx+1):
            book.append(0)
        if book[idx] > 0:
            return False
        book[idx] += 1
    return True

def isunique_bit(string: str):
    """
    Voltar depois que estudar bitshifting
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    checker = 0
    for i in range(len(string)):
        val = ord(string[i]) - ord('a')
        if (checker and (1 << val)) > 0:
            return False
        checker ^= (1 << val)
    return True

def isunique_nods(string: str):
    """
    Time Complexity: O(n*log(n)) to O(n^2) depending the algorithm
    Space Complexity: O(n) or O(1) depending on the algorithm
    """
    new_string = sorted(string)
    #string = sorted(string)
    for idx in range(1, len(new_string)):
        if new_string[idx] == new_string[idx-1]:
            return False
    return True


if __name__ =="__main__":
    assert(isunique("aab")==False)
    assert(isunique("abcda")==False)
    assert(isunique("abbc")==False)
    assert(isunique("abcde")==True)

    assert(isunique_bit("aab")==False)
    assert(isunique_bit("abcda")==False)
    assert(isunique_bit("abbc")==False)
    assert(isunique_bit("abcde")==True)

    assert(isunique_nods("aab")==False)
    assert(isunique_nods("abcda")==False)
    assert(isunique_nods("abbc")==False)
    assert(isunique_nods("abcde")==True)
    
    
    
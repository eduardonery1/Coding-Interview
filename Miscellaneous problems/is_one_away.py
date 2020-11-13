def case1(s1, s2, l1, l2, changes):
    for idx, letter in enumerate(s1):
            if s2[idx] != letter:
                if changes >= 1:
                    return False
                if idx < l2 - 1:
                    s2 = s2[:idx] + letter + s2[idx+1:]
                else:
                    s2 = s2[:idx] + letter
                changes += 1
    return True

def case2(s1, s2, l1, l2, changes):
    if l1 > l2:
        big = s1
        small = s2
    else:
        big = s2
        small = s1
    LIMIT = len(big)
    marked = False
    for idx in range(LIMIT):
        if marked:
            idx -= 1
            if idx+1 == LIMIT:
                break
        letter = big[idx]
        print(big, small, idx, letter, changes, "\n")
        if idx == len(small) and changes == 0:
            return True
        if letter != small[idx]:
            if changes >= 1:
                return False
            if idx < len(big) - 1:
                big = big[:idx] + big[idx+1:]
            else:
                big = big[:idx]
            changes += 1
            marked = True
    return True

def is_one_away(s1: str="", s2: str="")->bool:
    l1, l2 = len(s1), len(s2)
    if abs(l1 - l2) > 1: return False
    changes = 0
    if l1 == l2:
        return case1(s1, s2, l1, l2, changes)
    else:
        return case2(s1, s2, l1, l2, changes)

if __name__ == "__main__":
    # NOTE: The following input values will be used for testing your solution.
    assert(is_one_away("abcde", "abcd")==True)  # should return True
    assert(is_one_away("abde", "abcde")==True)  # should return True
    assert(is_one_away("a", "a")==True)  # should return True
    assert(is_one_away("abcdef", "abqdef")==True)  # should return True
    assert(is_one_away("abcdef", "abccef")==True)  # should return True
    assert(is_one_away("abcdef", "abcde")==True)  # should return True
    assert(is_one_away("aaa", "abc")==False)  # should return False
    assert(is_one_away("abcde", "abc")==False)  # should return False
    assert(is_one_away("abc", "abcde")==False)  # should return False
    assert(is_one_away("abc", "bcc")==False)  # should return False


        
        
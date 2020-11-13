def check(str1, str2):
    if len(str1) != len(str2): return False
    mem = {}
    for i in str1:
        if i not in mem:
            mem[i] = 1
        else:
            mem[i] += 1
    for i in str2:
        if i not in mem: return False
        mem[i] -= 1
        if mem[i] == -1: return False
    return True

def sorted_check(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1==sorted_str2

if __name__=="__main__":
    assert(check("abc", "cba")==True)
    assert(check("aab", "aba")==True)
    assert(check("aaaa", "aaa")==False)
    assert(check("abc", "aba")==False)

    assert(sorted_check("abc", "cba")==True)
    assert(sorted_check("aab", "aba")==True)
    assert(sorted_check("aaaa", "aaa")==False)
    assert(sorted_check("abc", "aba")==False)

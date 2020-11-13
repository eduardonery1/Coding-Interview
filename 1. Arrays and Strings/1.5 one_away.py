def same_len(str1, str2, l1):
    count = 0
    for i in range(l1):
        if str1[i] != str2[i]:
            count += 1
            if count > 1: return False
    return True

def diff_len(big, small, LEN_SMALL):
    pb = 0
    ps = 0
    count = 0
    while ps <= LEN_SMALL:
        if big[pb] != small[ps]:
            pb += 1
            count += 1
            if count > 1: return False
            continue
        pb += 1
        ps += 1
    return True

def one_away(str1, str2):
    l1, l2 = len(str1), len(str2)
    if l1 == l2:
        return same_len(str1, str2, l1)
    elif l1 - l2 == 1:
        return diff_len(str1, str2, l2-1)
    elif l2 - l1 == 1:
        return diff_len(str2, str1, l1-1)
    else:
        return False
        
if __name__=="__main__":
    assert(one_away("pale", "ple")==True)
    assert(one_away("pales", "pale")==True)
    assert(one_away("pale", "bale")==True)
    assert(one_away("pale", "bake")==False)
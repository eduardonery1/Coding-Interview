def unique(a: str): #O(N)
    if len(a) > 128: return False
    chars = [False for _ in range(128)]
    for letter in a:
        if chars[ord(letter)]: return False
        else: chars[ord(letter)] = True

    return True

print(unique('abc%'))
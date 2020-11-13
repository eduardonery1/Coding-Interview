def check(a: str, b: str):
    if len(a) != len(b): return False
    counter = {}
    
    for letter in a:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1

    for letter in b:
        if letter in counter: counter[letter] -= 1
        else: return False
        if counter[letter] == 0: del counter[letter]

    return True


print(check('abaae', 'aabad'))
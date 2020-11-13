def str_compress_slow(string):
    """
    Concatenação é um processo lento que gera uma nova string, existe uma forma melhor de fazer
    mas o objetivo seria usar um char array que não existe em python, então a solução seria:
    
    -com char array
    Time complexity: O(n)
    Space Complexity: O(n)

    -sem char array 
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    count = 0
    current = ""
    compressed_str = ""
    for letter in string:
        if letter != current: count = 0
        if count == 0:
            current = letter
            compressed_str += letter
            idx = len(compressed_str) 
        count += 1
        compressed_str = compressed_str[:idx] + str(count) 
    return compressed_str if len(compressed_str) < len(string) else string


if __name__ == "__main__":
    assert(str_compress_slow("aabcccccaaa")=="a2b1c5a3")
        

        

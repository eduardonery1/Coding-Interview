def urlfy(string, true_size):
    """
    A operação de cortar a string é necessária pois strings são imutaveis em python
    Idealmente se usaria um array de char para fazer isso, pois o slicing leva O(n)
    O propósito aqui é mostrar o raciocínio caso fosse um array de char
    Time Complexity: O(n^2)
    Space complexity: O(1)
    """
    count = 0
    for i in range(true_size):
        if string[i] == " ":
            count += 1
    index = true_size + count*2
    for i in range(true_size-1, -1, -1):
        if string[i] == " ":
            stack = ["0", "2", "%"]
            for j in range(1, 4):
                string = string[:index-j] + stack[j-1] + string[index-j+1:]
            index -= 3
        else:
            try:
                string = string[:index-1] + string[i] + string[index:]
            except:
                string = string[:index-1] + string[i]
            finally:
                index -= 1
    return string

if __name__=="__main__":
    assert(urlfy("Mr John Smith    ", 13)=="Mr%20John%20Smith")
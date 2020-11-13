import unittest

def unique(string):

    if len(string)>128: return False

    chars = [False for _ in range(128)]

    for char in string:
        if chars[ord(char)]: return False
        chars[ord(char)] = True

    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test(self):
        for test in self.dataT:
            actual = unique(test)
            self.assertTrue(actual)

        for test in self.dataF:
            actual = unique(test)
            self.assertFalse(actual)
            
if __name__ == "__main__":
    unittest.main()
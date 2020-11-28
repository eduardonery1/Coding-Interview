def isSubstring(S, word) -> bool:
	pw, pS = 0, 0
	while pw < len(word) and pS < len(S):
		if word[pw] != S[pS]: pS += 1
		else: pw += 1
	return pw == len(word) #if True means it found all letters of word in order 

def findLongestSub(string, dictWords) -> str:
	longestWord = ""
	for word in dictWords:
		if isSubstring(string, word):
			if len(word) > len(longestWord):
				longestWord = word
	return longestWord
################################################################

def createHashTable(S) -> dict:
	Letters = {}
	for idx, letter in enumerate(S):
		Letters[letter].append(idx)
	return Letters

def binarySearchClosestIdx(array, target) -> int:
    if target is None: return array[0]
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if  array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return array[mid]

def isSubstringWorstCase(word, LettersInS) -> bool:
    lastIdx = None
    for letter in word:
        if letter in LettersInS:
            foundIdx = binarySearchClosestIdx(LettersInS[letter], lastIdx)
            if lastIdx is not None and foundIdx < lastIdx: return False
            lastIdx = foundIdx
        else: return False
    return True

def findLongestSubWorstCase(string, dictWords) -> str:
    LettersInS = createHashTable(string)
    longestSub = ""
    for word in dictWords:
        if isSubstringWorstCase(word, LettersInS):
            if len(word) > len(longestSub): longestSub = word
    return longestSub
			
		
if __name__=="__main__":
    S = "abppplee"
    Dd = {"able", "ale", "apple", "bale", "kangaroo"}
    Dl = ["able", "ale", "apple", "bale", "kangaroo"]
    assert(findLongestSub(S, Dd)=="apple")
    assert(findLongestSub(S, Dl)=="apple")

    assert(findLongestSubWorstCase(S, Dd)=="apple")
    assert(findLongestSubWorstCase(S, Dl)=="apple")

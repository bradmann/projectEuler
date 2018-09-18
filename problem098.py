'''
Created on Nov 17, 2011

@author: bradmann
'''

wordmap = {}
maxSquareVal = 0

def strip_quotes(x):
    return x.strip('"')

def is_anagram(word1, word2):
    for c in word1:
        word2 = word2.replace(c, "", 1)
    if len(word2) == 0:
        return True
    else:
        return False

def anagrams(length):
    anarray = []
    words = wordmap[length]
    while len(words) > 0:
        word = words.pop(0)
        arr = [word]
        for word2 in words:
            if is_anagram(word, word2):
                arr.append(word2)
        if len(arr) > 1:
            anarray.append(arr)
    return anarray

def forms_squares(arr):
    global maxSquareVal
    l = len(arr[0])
    squares = []
    val = 0
    base = 2
    while len(str(val)) <= l:
        val = base**2
        if len(str(val)) == l:
            squares.append(val)
        base += 1
    
    seed = arr[0]
    for square in squares:
        squaremap = {}
        squareUnmap = {}
        for idx, c in enumerate(list(seed)):
            squaremap[c] = str(square)[idx]
        for idx, c in enumerate(list(seed)):
            squareUnmap[str(square)[idx]] = c
        if len(squaremap.keys()) != len(squareUnmap.keys()):
            continue
        for anagram in arr[1:]:
            num = ''
            for c in anagram:
                num += squaremap[c]
            if num[0] == '0':
                continue
            num = int(num)
            if num**.5 % 1 == 0:
                print("%s %s %s %s" % (seed, anagram, square, num))
                if num > maxSquareVal:
                    maxSquareVal = num
                if square > maxSquareVal:
                    maxSquareVal = square
        

if __name__ == '__main__':
    f = open('data/words.txt', 'r')
    words = map(strip_quotes, f.read().split(','))
    maxlen = 0
    for word in words:
        l = len(word)
        wordmap.setdefault(l, [])
        wordmap[l].append(word)
        
    for key in wordmap.keys():
        a_grams = anagrams(key)
        for arr in a_grams:
            forms_squares(arr)
            
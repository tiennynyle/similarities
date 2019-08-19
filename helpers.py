from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    #take in string inputs a, b, split each string into lines, compute a list of all lines that appear in both a and b
    lines_a = set(a.split('\n'))
    lines_b = set(b.split('\n'))
    #return the list
    return lines_a & lines_b


def sentences(a, b):
    """Return sentences in both a and b"""
    sentences_a = set(sent_tokenize(a))
    sentences_b = set(sent_tokenize(b))

    return sentences_a & sentences_b


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    substrings_a = []
    substrings_b = []

    for i in range (len(a)-n +1):
        substrings_a.append(a[i: i+n])

    for j in range (len(b)-n+1):
        substrings_b.append(b[j: j+n])
    #s[i:j] - return substrings of s from index i to (but not including) j
    return (set(substrings_a) & set(substrings_b))


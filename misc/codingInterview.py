def isUnique(string):
    '''O(n) space, O(n) time'''
    chars = set()
    for char in string:
        if char in chars:
            return False
        chars.add(char)
    return True

def isUniqueNoDataStructures(string):
    '''O(1) space, O(nlog(n)) time'''
    if len(string) == 0:
        return True
    string = sorted(string)
    prev = string[0]
    for char in string[1:]:
        if char == prev:
            return False
       	prev = char
    return True

def check_permutation(first, second):
    '''O(1) space, O(mlog(m)) time'''
    if len(second) < len(first):
        return False
    first = sorted(first)
    second = sorted(second)
    second_index = 0
    for char in first:
        while second[second_index] != char:
            second_index += 1
            if second_index == len(second):
                return False
    return True

def URLify(string):
    return '%20'.join(string.split())

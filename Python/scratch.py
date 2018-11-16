'''
need to split the list into 3 distinct parts
the maximum element to become the sum
the list of elements in the first sum
the list of elements in the second sum

list[-1] is the highest number, check sums against that
start from list[-2]
find next highest number in list such that list[-2] + num <= list[-1]

find a subset of numbers that adds up to the max
if that exists, check that the remainder also add up to the max

proposition:
if you find one subsequence of l (lets call it a) that sums to x and
the remainder of l (lets call it !a) does not sum to x, then there
exists no partition of l where both halves sum to x

assume this is not true. Let there be a partition b with complement
!b where b and !b sum to x. then this partition b != a, because if it
were then !b = !a, which is not true because by our assumptions !b = x
and !a != x

actually wait you're doing this totally wrong

just need to find two sublists that don't necessarily contain everything
that sum to a certain value

#pick a value
#divy the thing up into 3 parts
#all possible sublists of one part
#all possible sublists of another part


still feel like it could be better
like we only have to try including each item once
like here it is: its a binary tree
include item 1? yes or no
include item 2? yes or no
so start at item 1.
-include it. if its too big, return false. if its not, recurse on the rest of the list
-don't include it. recurse on the rest of the list

'''

def car(l):
    return l[0]

def cdr(l):
    return l[1:]

def cons(i,l):
    return [i] + l


def find_remainder(l,target):
    if not l or target <= 0:
        return l
    subseq = find_subseq(cdr(l),target-car(l))
    return cons(car(l),subseq) if not subseq else find_subseq(cdr(l),target)
        

def find_subseq(l,target):
    if not l or target <= 0:
        return []
    subseq = find_subseq(cdr(l),target-car(l))
    return cons(car(l),subseq) if subseq else find_subseq(cdr(l),target)
        
def remove(item,l):
    a = l[:]
    a.remove(item)
    return a

def find_sum_subseq(l,val,subseq=[]):
    for num in l:
        next_subseq = subseq + [num]
        next_l = remove(num,l)
        total = sum(next_subseq)
        if total == val: return True,next_l
        #if total > val: continue
        success,remainder = find_sum_subseq(next_l,val,next_subseq)
        if success: return success,remainder
    return False,[]

def has_subtarget(l):
    for i in range(len(l)):
        list_without_target = l[:i] + l[i+1:]
        target = l[i]
        success,remainder = find_sum_subseq(list_without_target,target)
        success,remainder = find_sum_subseq(remainder,target)
        if success: return True
    return False

t1 = [2,1,3,9,4,8] #t
t2 = [1,1,2,2] #t
t3 = [1,1,2] #f
t4 = [5,6,7] #f
t5 = [17,35,1,26,24,12,25,40,33,31] #f
t6 = [6,21,84,66,100,53,73,38,29,81,66,69,54,8,94] #t

from math import log, floor, exp

def sigmoid(x):
    return 1/(1+exp(-x))

def encode(l):
    return l[0] + sigmoid(encode(l[1:])) if l else 0

def sigmoid_inverse(x):
    return -log(1/x - 1)

def decode(x):
    l = []
    while abs(x) > 0.001:
        x = sigmoid_inverse(x-floor(x))
        l.append(floor(x))
    return l


def id(x):
    return x

def compose(f,g):
    return lambda x: f(g(x))

def memoize(f):
    '''memoize function of 1 argument'''
    memo = {}
    def memoized(x):
        if x in memo:
            return memo[x]
        new_x = f(x)
        memo[x] = f(x)
        return new_x
    return memoized

def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2) if n > 1 else 1

fibonacci = memoize(fibonacci)

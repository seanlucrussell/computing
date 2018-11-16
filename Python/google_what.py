from math import exp

def is_prime(number,primes):
    '''checks if a number is prime'''
    '''requires a list up primes up to that number'''
    for prime in primes:
        if number % prime == 0:
            return False
        if prime ** 2 > number:
            break
    return True

def list_primes(n):
    '''return a list of primes up to index n'''
    primes = []
    current_prime = 2
    for i in range(n):
        primes.append(current_prime)
        while True:
            current_prime += 1
            if is_prime(current_prime,primes):
                break
    return primes

def answer(n):
    primes = list_primes(n+5)
    relevant_primes = primes[n:n+5]
    prime_string = ""
    for prime in relevant_primes:
        prime_string += str(prime)
    return prime_string[:5]


'''
Elevator Maintenance
====================

You've been assigned the onerous task of elevator maintenance - ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on. 

Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

Given a list of elevator versions represented as strings, write a function answer(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function answer(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.
'''


'''
alright this is a really silly solution to this
problem but im very proud of it

so the sorted function takes as a parameter a
function that basically assigns a numerical
value to each element of the list being sorted

but since there are three different values to
each revision, in order to make this key function
i needed a function that has a domain over the
entire real numbers but a finite range. if i've
got a finite range of values, then i can just
offset the major revision by some value that
takes the range of major revisions out of the
range of minor revisions.

the other thing i needed for this function was
for it to be an increasing function, that is if
x < y, then key(x) < key(y). This preserves the
ordering, like if one revision is 12 and the other
is 1, then key(12) should definitely be bigger than
key (1)

since i've like always got machine learning on the
mind, i immediately went to the sigmoid function.
it has finite range with infinite domain, and it is
monotonically increasing (a strictly increasing
function would be better, but i'll bet theres a
theorem somewhere out there that a strictly
increasing function cannot have both infinite domain
and finite range

anyhow i think this solution is a little bit
suceptible to floating point error and could probably
be improved on by tweaking the sigmoid, but whatever
'''

def sigmoid(x):
    return 1 / (1 + exp(-x / 1000))

def order(version):
    return version[0] + sigmoid(order(version[1:])) if version else 0

def parse(version):
    split = version.split('.')
    return [int(s) for s in split]

def unparse(version):
    return '.'.join([str(i) for i in version])
    
def answer(l):
    parsed_l = [parse(v) for v in l]
    sorted_l = sorted(parsed_l,key=order)
    unparsed_l = [unparse(i) for i in sorted_l]
    return unparsed_l


test = ['1.0.1','1.1','1.0','1','2.0.0','1.0.1200000']

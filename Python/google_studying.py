from random import shuffle


def merge_sort(l):
    if len(l) > 2:
        lower = merge_sort(l[:len(l)//2])
        upper = merge_sort(l[len(l)//2:])
        sorted_list = []
        while lower and upper:
            if lower[0] < upper[0]:
                sorted_list.append(lower[0])
                lower = lower[1:]
            else:
                sorted_list.append(upper[0])
                upper = upper[1:]
        return sorted_list + lower + upper
    elif len(l) == 2:
        if l[0] > l[1]:
            l[0],l[1] = l[1],l[0]
    return l

def quick_sort(l):
    #doesn't sort lists with same element multiple times
    def partition(low, high):
        if low >= high:
            return
        pivot = l[low]
        x,y = low,high
        while x < y:
            while l[x] < pivot and x < y:
                x += 1
            while l[y] > pivot and x < y:
                y -= 1
            if l[x] > l[y]:
                l[x],l[y] = l[y],l[x]
        #l[low],l[x] = l[x],l[low]
        partition(low,x-1)
        partition(x+1,high)
    partition(0,len(l)-1)
    return l

class hash_map:
    def __init__(self):
        self.size = 60
        self.map = [(None,None) for x in range(self.size)]
    def hash(self,item):
        hash_value = 0
        i = 1
        for c in item:
            hash_value += i * ord(c)
            i += 1
        return hash_value % self.size
    def add(self,key,value):
        hash_value = self.hash(key)
        self.map[hash_value] = (hash_value,value)
    def contains(self,key):
        hash_value = self.hash(key)
        return self.map[hash_value][0] != None
    def get(self,key):
        hash_value = self.hash(key)
        return self.map[hash_value][1]

class set:
    def __init__(self):
        self.dict = {}
    def add(self,item):
        self.dict[item] = item
    def contains(self,item):
        return item in self.dict
    def remove(self,item):
        del self.dict[item]


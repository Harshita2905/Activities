#TOPIC_LIST
#APPEND()
a = [20,30,40]
print(a) #[20, 30, 40]
a.append(50)
print(a) #[20, 30, 40, 50]
b = [60,70]
a.append(b)
print(a) #[20, 30, 40, 50, [60, 70]]
a.append('str')
print(a) #[20, 30, 40, 50, [60, 70], 'str']

#the append() method only appends one new element to the end of the list. If you append a list to another list, the list that you append becomes a single element at the end of the first list.
print(a[4]) #[60, 70]

#EXTEND()
c = [80,90,100]
a.extend(c)
print(a) #[20, 30, 40, 50, [60, 70], 'str', 80, 90, 100]
a.extend(range(3))
print(a) #[20, 30, 40, 50, [60, 70], 'str', 80, 90, 100, 0, 1, 2]

#index(value, start_index)
print(a.index(40)) #2
#error will occur that ValueError: 70 is not in list
#print(index(15))
print(a.index(80,5)) #6

#insert(index, value) : inserts value just before the specified index. 
a.insert(0,0)
print(a) #[0, 20, 30, 40, 50, [60, 70], 'str', 80, 90, 100, 0, 1, 2]

#pop(index)
a.pop(5)
print(a) #[0, 20, 30, 40, 50, 'str', 80, 90, 100, 0, 1, 2]

#remove(value)
a.remove('str')
print(a) #[0,20, 30, 40, 50, 80, 90, 100, 0, 1, 2]

#reverse()
a.reverse() 
print(a) #[2, 1, 0, 100, 90, 80, 50, 40, 30, 20, 0]
a.reverse()

#count(value)
print(a.count(50)) #1

#sort()
a.sort()
print(a) #[0, 0, 1, 2, 20, 30, 40, 50, 80, 90, 100]
a.sort(reverse=True)
print(a) #[100, 90, 80, 50, 40, 30, 20, 2, 1, 0, 0]


#Better way to sort using attrgetter and itemgetter
import itertools
from operator import itemgetter,attrgetter
people = [{'name':'chandan','age':20,'salary':2000},
          {'name':'chetan','age':18,'salary':5000},
          {'name':'guru','age':30,'salary':3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')
people.sort(key=by_age) #in-place sorting by age people.sort(key=by_salary) #in-place sorting by salary

#Replication
b = ["blah"] * 3
print(b)

#deletion
del b[-1]
print(b)

#copy
c = a[:]
d = list(a)

#Accessing List values
lst = [1, 2, 3, 4] 
lst[0] # 1
lst[1] # 2
lst[1:]
lst[:3]
lst[::2]
lst[::-1]
lst[-1:0:-1]
lst[5:8]
lst[1:10]
#reverse
lst[::-1] # [4, 3, 2, 1]

# #Any and All
# nums = [1, 1, 0, 1] all(nums)
# # False
# chars = ['a', 'b', 'c', 'd'] all(chars)
# # True


#reversed : Reversing list elements

rev = reversed(lst)

#zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist): 
    print(a, b)

#itertools
alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']
for a,b,c in itertools.zip_longest(alist, blist, clist): 
    print(a, b, c)

# #remove duplication
# names = ["aixk", "duke", "edik", "tofp", "duke"] list(set(names))




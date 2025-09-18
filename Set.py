'''
→ mutable
→ not duplicate
→ Semi_hetergenous: Store Only integer , number, tuple
→ Unordered
'''
'''
s ={1,2,3,4,5,6,7}
for i in s:
    print(i)

'''
# set use hash() method to store multiple value that why the values are store in random form in the set 
#you can't access the value by index 
# # you can access the value by for loop

# directly iterating on it


# METHOD OF SET 

#ADD
'''
s ={1,2,3}

s.add(4)
print(s)
'''
#Remove and discard are same
'''
s ={1,2,3,4}
s.remove(4)
print(s)
'''

# pop is use to remove last element in the list but in set it remove the random value
'''
s ={1,"hello",7,45,78}
p=s.pop()
b =hash(p)
print(b)
'''

# clear is use to empty the set
'''
s ={1,2,3,4}
s.clear()
print(s)
'''


# SET OPERATIPON


a ={1,2,3}
b ={4,5,6,7,8,9 ,10}
# print(a|b)  Union
# print(a-b) Difference
# print(a&b) Intersection

# print(a^b) Symmetric Difference

# Membership Operator
# print(4 in a)
# print(4 not in a)

# Set Relations
'''
print(a.issubset(b))
print(b.issuperset(a))
print(b.isdisjoint(a))

'''

# frozen set make set immutable
'''
a =frozenset({1,2,3})
a.add(12)

'''

# usage with list

#Remove duplicates from a list:
'''
li =[1,2,2,3,3,4,4,5,5]
li =list(set(li))
print(li)

'''
'''
li = [1, 2, 2, 3, 3, 4, 4, 5, 5]
r_list = []

for i in li:
    if i not in r_list:   # only add if not already present
        r_list.append(i)

print(r_list)

'''
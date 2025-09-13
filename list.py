# List → a collection of items
'''
→ mutaqbl
→ duplicate
→ hetergenous
→ ordered
'''
'''
a =[23,56,48,78]
max =0
for i in range(len(a)):
   for j in range(len(a)):
      if a[i]>a[j]:
         max=a[i]
         
print(f"The maximum number is {max}") 
'''

#Methode

# Append
'''
a = [23,56,48,78]
a.append(45)
print(a)
'''

# Insert
'''
n =[1,2,3,4,5]

n.insert(2,23)

print(n)

'''

# Remove
'''
a = [23,56,48,78]
a.remove(48)
print(a)
'''

#extends
'''
n =[1,2,3,4,5,6]
n.extend([23,43,56])
print(n)
'''

#index
'''
n =[1,2,3,4,5,6]
index =n.index(4)
print(index)
'''

# Reseverse

n =[1,2,2,3,4,5,6]
n.reverse()
print(n)
#sort
n.sort()
print(n)

#count
count= n.count(2)
print(count)
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
'''
n =[1,2,2,3,4,5,6]
n.reverse()
print(n)
#sort
n.sort()
print(n)

#count
count= n.count(2)
print(count)
'''
# Assignment Task
'''
After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads

'''
'''
coin =['head','tail','head','head','head','tail']
count = 0

for i in range(0,len(coin)-1):
   if coin[i] == 'head':
      count += 1

print(f"Total time head come : {count}")
'''

# print positive nad negative number in list
'''
arr = [0,-2,5,-1,-6,7,-8]
positive=[]
negative =[]
for i in range(0,len(arr)):
   if arr[i]>=0:
      positive.append(arr[i])
   else:
      negative.append(arr[i])

print(f'Positive: {positive}')
print(f'Negative: {negative}')

'''


# Mean of the list element
'''
li = [1,7,3,2,-5]
add =0
for i in li:
   add+=i
result =add/len(li)
print(f"Mean: {result}  ")

'''

# find the second greatest element in the list
'''
li = [1,7,3,2,-5]
li.sort()
print(li[-2])
'''

'''
n = [1,2,53,67,24,78,65,70]
f_largest =n[0]
sec_largest =n[0]
for i in range(1,len(n)):
   if n[i]>f_largest:
      sec_largest=f_largest
      f_largest = n[i]
   elif n[i] > sec_largest:
      sec_largest = n[i]

print(f"First largest: {f_largest}")
print(f"Second largest: {sec_largest}")
'''
# check if the list is sorted or not

n =[1,2,3,4,5,6]
sor = True
for i in range(len(n)-1):
   if n[i]>n[i+1]:
         sor = False
         break

if sor == True:
   print("The list is sorted")
else:
   print("The list is not sorted")

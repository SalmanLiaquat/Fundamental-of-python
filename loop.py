# loop : allow block of code to run multiple time
#for loop :work on the basis of number or range e.g; to remove 4 items from the backets
#while loop :work on the basis of condition e.g; to remove  items from the backets until it empty


#range function:
#range(start,end,step)
'''
a =range( 1,21,1)
for i in a:
    print(i)

'''

# basic Question:
'''
for i in range(20,51,1):
    print(i)
'''
'''
for i in range(16,0,-1):
    print(i)
'''
'''
for i in range(-3,-16,-1):
    print(i)
'''
# question 2 print table 5
'''

for i in range(1,11,1):
    result =5*i
    #print("5 *",i,"=",result)
    print(f'5 * {i} ={result}'.format(i=i,result=result))

'''


# loop for String : two ways _ by indexing and _ by directly iterating on the string


# 1st way
'''
name ="Salman"
for i in range(len(name)):
    print(name[i])

'''
#2nd way
'''
name='salman'
for char in name:
    print(char)
'''
# Continue and break

# Suppose you have a string"heello!Salman" and you want  when you iterating on the string and ! mark come apply continue it
'''
st= "hello!salman"
for i in range(len(st)):
    if st[i]=='!':
        continue
    print(st[i])

'''

# Suppose you have a string"heello Salman" and you want  when you iterating on the string and ! mark come apply break it
'''
greeting= "Hello salman"
for char in greeting:
    if char==" ":
        break
    print(char)
'''

# Elae in for loop

for i in range(0,20,4):
    if i ==5:
        print ("break is executed")
        break
    print(i)
else:
    print("else is not executed")
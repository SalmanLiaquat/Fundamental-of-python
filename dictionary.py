'''
→ mutable
→ duplicate just values not keys
→ hetergenous
→ ordered
'''

student_info ={
    'name':'salman liaquat',
     'age':23,
     'course':'python',
     'fees':5000

}
student_info.clear()
print(student_info)
'''
student_info['fees'] =10000
student_info.update({'course2':'java'})
student_info['m_num']= 923264177168 # creating new key
print(student_info)
del student_info['m_num']
print(student_info)
print(f"The {student_info['course']} and {student_info['course2']} courses fee is {student_info['fees']}")
'''

'''
# loop in dictionary

for key,value in student_info.items():
    print(f"{key}: {value}")
'''

# METHODS 
# DEEP COPY AND SHALLOW COPY

#deep copy()
'''
li = [1,2,3,4,5,6]
b = li
b[0] =10
print(li)
'''

#SHALLOW COPY 
'''
li = [1,2,3,4,5,6]
b =li.copy()
b[0] =10
print(li)
'''

#Get 
'''
dic = {
    'name':'salman liaquat',
     'age':23,
     'course':'python',
     'fees':5000
}
'''
 # print(f"The name is {dic.get('name')}") # get method is use to get values of specific key


# pop → remove key and popitem → remove last key and value
'''
print(f"THE LAST KEY OF THE DICTIONARY IS:{dic.pop('fees')}")
print(dic)
print(f"THE LAST KEY OF THE DICTIONARY IS:{dic.popitem()}")
print(dic)
'''

# QUESTION
#Merge two dictionary
'''
dic = {
    'name':'salman liaquat',
     'age':23,
     'course':'python',
     'fees':5000
}
course_info={
    'total_credits':3,
    'per_credit_fee':1700
}

dic.update(course_info)
print(dic)
'''


#Q2"
#sum all the value in the dictionary
'''
d ={
    '1': 10,
    '2': 20,
    '3': 30
}
sum = 0
for i in d:
    sum += d[i]

print(sum)
'''

# Q3: count the frequency of the element in the list
'''
li =[1,2,2,2,2,3,3,3,4,4,5,5]
d={}
for i in li:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''
#Q4: write a program in the python two add the 2 dic values from the keys

dic = {
    'name':'salman liaquat',
     'age':23,
     'course':'python',
     'fees':5000
}
course_info={
    'fees':1000,
    'total_credits':3,
    'per_credit_fee':1700
}

for i in course_info:
    
    if i in dic.keys():
        dic[i] += course_info[i]
    else:
        dic[i] = course_info[i]
print(dic)
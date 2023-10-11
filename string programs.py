'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#Count of occurence of particular character in string:
''' n=input("Enter a string:")
c=input("Enter a character:")
count=0
for i in range(len(n)):
    if(n[i]==c):
        count=count + 1
print("the occurace of character is:", count) '''
#anagram:
''' str1=input("Enter a string:")
str2=input("Enter a string:")
if(sorted(str1)==sorted(str2)):
    print("given Two strings '%s' and '%s' are anagram: " %(str1, str2))
else:
    print("not anagram") '''


#palindrome:
''' str1="madam"
str2=str1[::-1]
if(str1==str2):
    print(" Given string '%s' is a palindrome: "%(str1))
else:
    print("Not palindrome") '''

#character digit or not:
''' str1=input("Enter a string")
ch=input("enter a character:")
if ch>='0' and ch<='9':
    print("given charcter is a digit:")
else:
    print("not a digit") ''' 
    
#replace a string with particular character:(instead of space)
''' string = input("Enter a String : ")
result = '' 
ch = input("Enter a Character : ")
for i in string:  
        if i == ' ':  
            i = ch   
        result += i   
print("String after removing space with t=  ",result) '''
##convert lowercase character of a string to uppercase:
''' str1=input("Enter a charcter:")
result=''
for i in str1:
    if i.islower():
             i=i.upper()
    result+=i
print(" after transformation string is:" , result) '''


##convert uppercase character of a string to lowercase:
''' str1=input("Enter a charcter:")
result=''
for i in str1:
    if i.isupper():
             i=i.lower()
    result+=i
print(" after transformation string is:" , result) '''

#program to remove vowels in string:
''' str1=input("Enter a charcter:")
result=''
for i in str1:
    if i in('a','e','i','o','u','A','E' ,'I','O','U'):
             i=' '
    result += i
print(" after transformation string is:" ,result) '''
#program to count vowels, consontants:
''' str1=input("Enter a string:")
vowels=0
consonants=0
for i in str1:
    if i in('a','e','i','o','u','A','E' ,'I','O','U'):
        vowels=vowels+1
    elif i.isalpha():
        consonants=consonants+1
print(" the count of vowels and consonants in given string is %d and %d " % (vowels,consonants)) '''
    
#Lowercase vowel into uppercase
''' str1=input("Enter a string")
result=" "
for i in str1:
    if i in('a','e','i','o','u'):
       i=i.upper()
    result+=i
print("after transformation string is:",result) '''
    
#highest frequency character in the string:
''' str1=input("Enter a string:")
lst={}
for i in str1:
    if i in lst:
        lst[i]+= 1
    else:
        lst[i]=1
max_freq=max(lst, key=lst.get)
print("highest frequency character in the string is:",max_freq)
print(lst) '''

#count the frequencies of characters in the string:
''' str1=input()
lst={}
for i in str1:
    if i in lst:
        lst[i]+=1
    else:
        lst[i]=1
print(lst)
for key,value in lst.items():
    print(f"{key} occurs {value} times in the string ") '''
    
#replace first occurence of vowel with '-': method1
''' str1=input()
str2=""
vowels="AEIOUaeiou"
for i in range(len(str1)):
    if str1[i] in vowels:
        str2=str1[:i]+'-'+str1[i+1:]
        break
print("After modification string is:",str2) '''

#method2
''' str1=input()
str2=""
#vowels="AEIOUaeiou"
for char in str1:
    if char in ('A','E','I','O','U','a','e','i','o','u'):
       str2= str1.replace(char,'-',1)
print("After modification string is:",str2) ''' #Compiler error

#replace particular character from string:
''' string=input()
ch='a'
print(string.replace(ch,' ')) '''

#method2:
''' string=input()
ch={97 :' '}
print(string.translate(ch)) '''


#separate characters in the string:
''' string=input()
for i in string:
    print(i)
    print() '''

#remove space from string:
''' string = input("Enter a String : ")
result=''
#iterating the string
for i in string:
    #if the character is not a space
    if i!=' ':
        result += i
print("String after removing the spaces :",result) '''

#join two strings:
''' string1=input()
string2=input()
print("".join([string1,string2])) '''

#remove repeated characters in the string:m1-using set:
''' string=input()
result=" "
setr=set()
for i in string:
    if i not in setr:
        setr.add(i)
        result+=i
print(result) '''


#calculate sum of integers in string:
''' string=input()
sum=0
for i in string:
    if i.isdigit():
        sum+=int(i)
print("sum of integers in string:",sum) '''

#print all non repeating characters in string:
''' string=input()
result=" "
setr=set()
for i in string:
    if i not in setr:
        setr.add(i)
        print(i,end=" ") '''

#program to copy one string into another:
''' string=input()
result=" "
result=string[0:]
print(result) '''

#sort the characters in the ascending order:
''' string=input()
slist=list(string)
sort=sorted(slist)
print(sort)
result=""
for i in sort:
    result+=i
print(result) '''

#sort the characters in the descending order:
''' string=input()
slist=list(string)
sort=sorted(slist,reverse=True)
print(sort)
result=""
for i in sort:
    result+=i
print(result) '''

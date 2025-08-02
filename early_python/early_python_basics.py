# name="arun"
# age=15
# fav_clr="black"
# student='yes'
# print(f"Hi, my name is {name}.I am {age} years old.My favourite colour is {fav_clr} .Am I a student? {student}")   
# print(name+str(age))
# no=14
# no1=0.1
# no2=0.0000005
# w="arun"
# b=True            
# print (no)
# print (type(no)  ) 
# print (no1)
# print (type(no1))      
# print (no2)
# print (type(no2))  
# print (w)
# print (type(w)) 
# print (b)
# print (type(b)) 
# a = 10
# b = 20

# a,b=b,a

# print("a =", a)
# print("b =", b)
# num1=int(input("Please enter a number : "))
# num2=int(input("Please enter another number : "))
# sum=num1+num2
# product=num1*num2
# difference=num1-num2


# print(f"sum={sum}")
# print(f"difference={difference}")
# print(f"product={product}")
# if num2!=0:
#     division=num1/num2
#     print(f"division={division}")
# else:
#     print("division by zero is not possible")
# import math

# r=float(input("Please enter radius of circle : "))
# area=math.pi*r*r
# print(f"Area={area}")
# name=input(" enter your name : " ).strip()
# sc=input(" enter mark out of 100 : " ).strip()
# if sc=='' or name=='':
#     print("!Enter valid input")
# else:
#     try:
#         sc=float(sc)
#         if sc<0 or sc> 100:
#             print("enter a valid number between 0 to 100")
#         elif sc>=90:
#             print(f"Hi,{name} you scored {sc} and  you passed with first class and distinction")
#         elif sc>=40:
#             print(f"Hi,{name} you scored {sc} and  you passed ")
#         else:
#             print(f"Hi,{name} you scored {sc} and  you failed,But keep trying ")
#     except ValueError:
#         print("enter valid numbers")
# n=input(" enter a number of elements: " ).strip()
# if n.isdigit:
#     n=int(n)
#     i=1
#     while(i<=n):
#         if i%2==0:
#             print(f"{i} even")
#         else:
#             print(f"{i} odd")
#         i=i+1
# else:
#     print("enter valid number")

# n=input(" enter a number of elements: " ).strip()

# if n.isdigit():
#     n=int(n)
#     for i in range (1,n+1):
#         if i%3==0 and i%5==0:
#             print("FizzBuzz")
#         elif i%3==0:
#             print("Fizz")
#         elif i%5==0:
#             print("Buzz")
#         else:
#             print(i)
# else:
#     print("enter valid number")
# name=input(" enter student name: " ).strip()
# n=input(" How many subjects: " ).strip()
# sum=0
# marks=[]
# if n.isdigit():
#     n=int(n)
#     for i in range(1,n+1):
#         while True:
#             m=input(f" enter mark of {i}   subject  : " ).strip()
#             try:
#                 m=float(m)
#                 if 0<=m<=100 :
#                     marks.append(m)
#                     sum+=m
#                     break
#                 else:
#                     print("mark should be between 0 and 100")
#             except ValueError:
#                 print(" enter valid marks")
#     if len(marks)>0:
#         avg=sum/len(marks)
#         print(f"Hi, {name} ")
#         print(f"marks : {marks}")
#         print(f"average mark : {avg:.2f}")
#         if avg>=90:
#             print(f"Remarks : Excellant")
#         elif avg>=80:
#             print(f"Remarks : Very good")
#         elif avg>=70:
#             print(f"Remarks : Good")
#         elif avg>=60:
#             print(f"Remarks : Average")
#         elif avg>=40:
#             print(f"Remarks : Pass")
#         else:
#             print(f"Remarks : Fail.But Keep trying")
#     else:
#         print("no valid marks entered")
# else:
#     print("enetr a valid number")
# n=input(" how many favorite items you want to enter: " ).strip()
# fav=[]
# if n.isdigit():
#     n=int(n)
#     for _ in range(n):
#          while True:
#             i=input("   enter items : ").strip()
#             if not i.isdigit():
#                 fav.append(i)
#                 break
#             else:
#                 print(" Enter valid items only ! ")
# else:
#     print(" Enter valid number : ")
# print(f" your favpurite items are : {fav} ")
# print(f" 1st item in your list is  : {fav[0]} ")
# print(f" last item in your list is  : {fav[-1]} ")
# print(f" Total number of items in your list is  : {len(fav)} ")
# if len(fav)>0:
#     for i in reversed(fav):
#         print(f" Items in reverse order : {i}")
# c=input(" Enter  Item to check :").strip()
# if not c.isdigit():
#     if c in fav:
#         print(f" yes, {c} is in your list")
#     else:
#         print(f" No, {c} is not in your list")
# else:
#     print(" Enter valid items only ! ")
# d=input(" Enter  Item to delete :").strip()
# if not d.isdigit():
#     if d in fav:
#         fav.remove(d)
#         print(f" {d} is removed from moved your list")
#         print(fav)
#     else:
#         print(f" {d} is not in your list")
# else:
#     print(" Enter valid items only ! ")
# e=input(" Enter  Item to check the frequency :").strip()
# count=0
# if not e.isdigit():
#     count=fav.count(e)
#     if count>0:
#         print(f" The frequency is {count} ")
#     else:
#         print("f {e} is not in the list")
# else:
#     print(" Enter valid items only ! ")
# n=input(" how many favorite items you want to enter: " ).strip()
# fav=[]
# if n.isdigit():
#     n=int(n)
#     for _ in range(n):
#          while True:
#             i=input("   enter items : ").strip()
#             if not i.isdigit():
#                 fav.append(i)
#                 break
#             else:
#                 print(" Enter valid items only ! ")
#     fav.sort()
#     print(f" This is sorted list : {fav}")
#     while True:
#         a=input(" ENter a item to insert: " ).strip()
#         b=input(" enter the index: " ).strip()
#         if not a.isdigit() and b.isdigit():
#             b=int(b)
#             if 0<=b<=len(fav):
#                 fav.insert(b,a)
#                 break
#             else:
#                 print("index out of range ! ")
#         else:
#             print("enter valid elements correctly")
#     print(fav)
#     if fav:
#         fav.pop()
#         print(f"last element is poped : {fav}")
#     else:
#         print("The lis is empty.Cannot pop ! ")
#     while True:
#         y=input("enter an element to check : ")
#         if not y.isdigit():
#             if y in fav:
#                 position=fav.index(y)
#                 print(f"The elements first occurance is at {position} ")
#             else:
#                 print(f"The element is not available : ")
#             break
#         else:
#             print("please enter valid item ! ")
# else:
#     print(" Enter valid number : ")
# while True:
#     str1=input(" enter a swntence : " ).strip()
#     words=[]
#     if not str1.isdigit():
#         words=str1.split()
#         filtered=[word for word in words if len(word)>3 ]
#         print(f"filtered words are : {filtered}")
#         break
#     else:
#         print("enter valid number only ! ")
# def square(n):
#     return n*n
# while True:
#     n=input("enter a number : ").strip()
#     if n.isdigit():
#         n=int(n)
#         s=square(n)
#         print(f"The square is {s} ")
#         break
#     else:
#         print(" Enter valid number !")
# def greet_name(name):
#     for j in name:
#         print(f"Hello, {[j]} !, Hope you're doing well!")
# while True:
#     n=input("enter n : ")
#     if n.isdigit():
#         n=int(n)
#         name=[]
#         for i in range(n):
#             while True:
#                 c=input("Enter names : ").strip()
#                 if not c.isdigit():
#                     name.append(c)
#                     break
#                 else:
#                     print("enter valid names !")
#         break 
#     else:
#         print("Enter valid number only!")
# greet_name(name)
# def sa(number):
#     sum=0
#     for s in number:
#             sum+=s

#     return sum/len(number) , sum
    
# while True:
#     n=input("enter n : ").strip()
#     if n.isdigit():
#         n=int(n)
#         number=[]
#         for i in range(n):
#             while True:
#                 a=input("enter numbers : ").strip()
#                 if a.isdigit():
#                     a=int(a)
#                     number.append(a)
#                     break
#                 else:
#                     print("enter valid numbers ! ")
#         break
#     else:
#         print("enter valid characters !")
# avg,sm=sa(number)
# print(f"average : {avg}")
# print(f"sum : {sm}")
# def greet(name,city="Trivandrum"):
#     print(f"Hello!, {name},You are from {city} ")
# name=input("Enter your name : ").strip()
# if not name.isdigit() and name:
#     city=input("Enter your city (Optional) :").strip()
#     if city=='':
#         greet(name)
#     else:
#         greet(name,city)
# else:
#     print(" enter valid inputs !")
# def reg_student(name,age,course="python",location="Online"):
#     print(f"\n Name : {name} \n Age : {age} \n course : {course} \n location : {location}")
# name=input("Enter your name : ").strip()
# age=input("Enter your age : ").strip()
# if not name.isdigit() and age.isdigit():
#     age=int(age)
#     c=input("Enter your course (Optional) :").strip()
#     l=input("enter the location (Optional) : ").strip()
#     if c=='' and l=="":
#         reg_student(name,age)
#     elif c=='':
#         reg_student(name,age,location=l)
#     elif l=='':
#         reg_student(name,age,course=c)
#     else:
#         reg_student(name,age,course=c,location=l)
# else:
#     print(" enter valid inputs !")
# def power(n,p=2):
#     return n**p
# while True:
#     num=input("Enter a number : ")
#     if num.isdigit():
#         num=int(num)
#         pow=input("Enter the power(optional) :")
#         if not pow.isdigit():
#             c=power(num)
#             print(f"{num} to the power 2 : {c}")
#             break
#         else:
#             pow=int(pow)
#             c=power(num,pow)
#             print(f"{num} to the power {pow} : {c}")
#             break
#     else:
#         print("Enetr a valid number ! ")
# def charcount(words):
#         count=[j for j in words if len(j)>5 ]
#         return count
# while True:
#     n=input("enter how many words : ").strip()
#     if n.isdigit():
#         n=int(n)
#         word=[]
#         for i in range(n):
#             while True:
#                 w=input(f"Enter {1+i} element : ").strip()
#                 if not w.isdigit():
#                     word.append(w)
#                     break
#                 else:
#                     print("Enter valid words !")
#         break
#     else:
#          print("Enter valid elements ! ")
# c=charcount(word)
# print(f" words with more than 5 characters are : {c}")
# def numcount(num):
#     e=[j for j in num if j%2==0]
#     o=[j for j in num if j%2!=0]
#     total=sum(num)
#     avg=total/len(num)
#     return len(e),len(o),avg
# while True:
#     n=input("How many numbers : ").strip()
#     if n.isdigit():
#         n=int(n)
#         if n==0:
#             print("List can't be empty !")
#             continue
#         num=[]
#         for i in range(n):
#             while True:
#                 c=input(f"Enter the {i+1} number : ").strip()
#                 if c.isdigit():
#                     num.append(int(c))
#                     break
#                 else:
#                     print("Enter valid numbers ")
#         break
#     else:
#         print("Enter valid number ! ")
# even,odd,average=numcount(num)
# print(f"Count of even numbers are : {even}")
# print(f"Count of odd numbers are : {odd}")
# print(f"Average of these numbers are : {average}")
# def countword(str1):
#     str1=str1.lower()
#     words=str1.split()
#     count={}
#     for word  in words:
#             word=word.strip('.,?/!-_')
#             if word in count:
#                 count[word]+=1
#             else:
#                 count[word]=1
#     return count
# while True:
#     str2=input("Enter a sentence  : ").strip()      
#     if not str2.isdigit():
#         cw=countword(str2)
#         print(f"count of words are : {cw}")
#         break
#     else:
#         print("Enter valid inputs ! ")
# while True:
#     n=input("How many students? : ").strip()
#     if n.isdigit():
#         n=int(n)
#         student={}
#         for i in range(n):
#             while True:
#                 str2=input("Enter name  : ").strip()
#                 m=input("Enter mark of student : ").strip()
#                 if str2=='':
#                     print("Enter valid inputs !")
#                 elif not str2.isdigit() and m.isdigit():
#                         student[str2]=int(m)
#                         break
#                 else:
#                     print("Enter valid inputs ! ")
#         break
#     else:
#          print("Enter valid inputs ! ")
# s=input("Enter name to search : ").strip()
# if s in student:
#     print(f"{s}'s mark is {student.get(s)}")
#     u=input(f"If you want to update {s}'s mark enter(or leave blank to skip) : ").strip()
#     if u.isdigit():
#         student[s]=int(u)
#         print(f"Updated mark : {student[s]}")
#     elif u=='':
#         print("Mark not updated !")
#     else:
#          print("enter valid marks !")
# else:
#     print("Not found !")
# print("\nAll student's  and mark : ")
# for name,mark in student.items():
#     print(f"{name}->{mark}")
# while True:
#     fn=input("Enter a file name : ").strip()
#     if fn=='':
#         print("please enter a name ! ")
#     elif not fn.isdigit():
#             n=input("How many lines do you want to add in this file : ").strip()
#             if n.isdigit():
#                 n=int(n)
#                 for i in range(n):
#                     while True:
#                         l=input(f"Enter {i+1} lines of text :").strip()
#                         if l=='':
#                             print("please enter any text ! ")
#                         else:
#                             with open(fn,'a')as f:
#                                 f.write('\n'+l)
#                                 break
#                 with open(fn,'r')as f:
#                     c=f.read()
#                     print(f"Content of file is : {c}")
#                     break
#             else:
#                 print("Enter valid numbers only ! ")
#     else:
#         print("Enter valid inputs only ! ")
# while True:
#     fn=input("Enter a file name : ").strip()
#     if fn=='':
#         print("please enter a name ! ")
#     elif not fn.isdigit():
#             n=input("How many lines do you want to add in this file : ").strip()
#             if n.isdigit():
#                 n=int(n)
#                 l=[]
#                 for i in range(n):
#                     while True:
#                         l1=input(f"Enter {i+1} lines of text :").strip()
#                         if l1=='':
#                             print("please enter any text ! ")
#                         else:
#                             l.append(l1)
#                             break
#                     with open(fn,'w')as f:
#                         for line in l:
#                             f.write(line+'\n')
#                 with open(fn,'r')as f:
#                     c=f.read()
#                     print(f"Content of file is : {c}")
#                     break
#             else:
#                 print("Enter valid numbers only ! ")
#     else:
#         print("Enter valid inputs only ! ")
# while True:
#     fn=input("enter a file name : ").strip()
#     if fn=='':
#         print("file name cannot be blank ! ")
#     elif not fn.isdigit():
#         n=input("enter how many lines : ").strip()
#         if n.isdigit():
#             n=int(n)
#             with open(fn,'w') as f:
#                 for i in range(n):
#                     while True:
#                         f1=input(f"enter {i+1} line  : ").strip()
#                         if not f1=="":
#                                 f.write(f1+'\n')
#                                 break
#                         else:
#                             print("enter valid content ! ")
#             with open(fn,'r') as f:
#                         print("printing lines using readline :")
#                         for i in range(n):   
#                             print(f.readline())
#             with open(fn,'r') as f:
#                 c=f.readlines()
#                 print(c)
#             break
#         else:
#             print("Enter valid number ! ")
#     else:
#         print("Enter valid name for file !")    
# while True:
#     fn=input("enter a file name : ").strip()
#     if fn=='':
#         print("file name cannot be blank ! ")
#     elif not fn.isdigit():
#         n=input("enter how many lines : ").strip()
#         if n.isdigit():
#             n=int(n)
#             with open(fn,'w') as f:
#                 for i in range(n):
#                     while True:
#                         f1=input(f"enter {i+1} line  : ").strip()
#                         if not f1=="":
#                                 f.write(f1+'\n')
#                                 break
#                         else:
#                             print("enter valid content ! ")
#             with open(fn,'r') as f:
#                 c=f.readlines()
#                 print("The content of this file is : ")
#                 for line in c:
#                     print(line.strip())
#                 print(f"The no of lines in this file is : {len(c)} ")
#                 wc=0
#                 for i in range(len(c)):
#                     lines=c[i]
#                     w=lines.split()
#                     wc+=len(w)
#                 print(f"The number of words in this files are : {wc}")
#             break
#         else:
#             print("Enter valid number ! ")
#     else:
#         print("Enter valid name for file !")  
# while True:
#     fn=input("enter a file name : ").strip()
#     if fn=='':
#         print("file name cannot be blank ! ")
#     elif not fn.isdigit():
#         n=input("enter how many lines : ").strip()
#         if n.isdigit():
#             n=int(n)
#             with open(fn,'w') as f:
#                 for i in range(n):
#                     while True:
#                         f1=input(f"enter {i+1} line  : ").strip()
#                         if not f1=="":
#                                 f.write(f1+'\n')
#                                 break
#                         else:
#                             print("enter valid content ! ")
#             with open(fn,'r') as f:
#                 c=f.readlines()
#                 a=0
#                 d=0
#                 o=0
#                 print("The content of this file is : ")
#                 for line in c:
#                     print(line.strip())
#                     for ch in line:
#                           if ch.isalpha():
#                             a+=1
#                           elif ch.isdigit():
#                             d+=1
#                           elif ch!='\n':
#                             o+=1
#                 print(f"The number of alphabets in this file is : {a}")
#                 print(f"The number of digits in this files are : {d}")
#                 print(f"The number of other characters in this files are : {o}")
#             break
#         else:
#             print("Enter valid number ! ")
#     else:
#         print("Enter valid name for file !")          
# while True:
#     fn=input("enter a file name : ").strip()
#     if fn=='':
#         print("file name cannot be blank ! ")
#     elif not fn.isdigit():
#         n=input("enter how many lines : ").strip()
#         if n.isdigit():
#             n=int(n)
#             with open(fn,'w') as f:
#                 for i in range(n):
#                     while True:
#                         f1=input(f"enter {i+1} line  : ").strip()
#                         if not f1=="":
#                                 f.write(f1+'\n')
#                                 break
#                         else:
#                             print("enter valid content ! ")
#             with open(fn,'r') as f:
#                 c=f.readlines()
#                 print(f"The Total number of Lines in this file is : {len(c)}")
#                 v='aeiouAEIOU'
#                 a=0
#                 cw=0
#                 cv=0
#                 print("The content of this file is : ")
#                 for line in c:
#                     print(line.strip())
#                 for i in range(len(c)):
#                           l=c[i].split()
#                           cw+=len(l)
#                           for j in range(len(l)):
#                             for ch in l[j]:
#                                 if ch in v:
#                                     cv+=1
#                                 elif ch.isalpha():
#                                     a+=1
#                 print(f"The number of words in this file is : {cw}")
#                 print(f"The number of vowels in this files are : {cv}")
#                 print(f"The number of consenents in this files are : {a}")
#             break
#         else:
#             print("Enter valid number ! ")
#     else:
#         print("Enter valid name for file !")
# import string   
# while True:
#     fn=input("enter a file name : ").strip()
#     if fn=='':
#         print("file name cannot be blank ! ")
#     elif not fn.isdigit():
#         n=input("enter how many lines : ").strip()
#         if n.isdigit():
#             n=int(n)
#             with open(fn,'w') as f:
#                 for i in range(n):
#                     while True:
#                         f1=input(f"enter {i+1} line  : ").strip()
#                         if not f1=="":
#                                 f.write(f1+'\n')
#                                 break
#                         else:
#                             print("enter valid content ! ")
#             with open(fn,'r') as f:
#                 c=f.readlines()
#                 wf={}
#                 print("The content of this file is : ")
#                 for line in c:
#                     print(line.strip())
#                 for i in range(len(c)):
#                           l=c[i].split()
#                           for word in l:
#                               word=word.lower().strip(string.punctuation)
#                               if word in wf:
#                                   wf[word]+=1
#                               else:
#                                   wf[word]=1
#                 print("The frequency of  words in this file is " )
#                 for k,v in wf.items():
#                      print(f"{k:<10}: {v}")        
#             break
#         else:
#             print("Enter valid number ! ")
#     else:
#         print("Enter valid name for file !")
# import string   
# while True:
#     fn=input("enter a file name : ").strip()
#     if fn=='':
#         print("file name cannot be blank ! ")
#     elif not fn.isdigit():
#         n=input("enter how many lines : ").strip()
#         if n.isdigit():
#             n=int(n)
#             with open(fn,'w') as f:
#                 for i in range(n):
#                     while True:
#                         f1=input(f"enter {i+1} line  : ").strip()
#                         if not f1=="":
#                                 f.write(f1+'\n')
#                                 break
#                         else:
#                             print("enter valid content ! ")
#             with open(fn,'r') as f:
#                 c=f.readlines()
#                 wf={}
#                 sa={}
#                 print("The content of this file is : ")
#                 for line in c:
#                     print(line.strip())
#                 for i in range(len(c)):
#                           l=c[i].split()
#                           for word in l:
#                               word=word.lower().strip(string.punctuation)
#                               if word in wf:
#                                   wf[word]+=1
#                               else:
#                                   wf[word]=1
#                               sa[word[0]]=sa.get(word[0],0)+1
#                 print("The frequency of  words in this file is  " )
#                 sorted_word=sorted(wf.items(),key=lambda x:x[1],reverse=True)
#                 for k,v in sorted_word:
#                      print(f"{k:<10}: {v}")
#                 print("the most frequent words are :")
#                 count=0
#                 for k,v in sorted_word:
#                      print(f"{k:<10}: {v}")
#                      count+=1
#                      if count==3:
#                           break
#                 print("The word start letter count :")    
#                 for p,q in sa.items():
#                      print(f"{p:<10}: {q}") 
#                 print("the most frequent starting letters are :")
#                 sorted_letter=sorted(sa.items(),key=lambda x:x[1],reverse=True)
#                 count=0
#                 for u,v in sorted_letter:
#                      print(f"{u:<10}: {v}")
#                      count+=1
#                      if count==3:
#                           break 

#             break
#         else:
#             print("Enter valid number ! ")
#     else:
#         print("Enter valid name for file !")
# import string   
# while True:
#     fn=input("enter a file name : ").strip()
#     if fn=='':
#         print("file name cannot be blank ! ")
#     elif not fn.isdigit():
#         n=input("enter how many lines : ").strip()
#         if n.isdigit():
#             n=int(n)
#             with open(fn,'w') as f:
#                 for i in range(n):
#                     while True:
#                         f1=input(f"enter {i+1} line  : ").strip()
#                         if not f1=="":
#                                 f.write(f1.strip()+'\n')
#                                 break
#                         else:
#                             print("enter valid content ! ")
#             with open(fn,'r') as f:
#                 c=f.readlines()
#                 wf={}
#                 sa={}
#                 print("The content of this file is : ")
#                 for line in c:
#                     print(line.strip())
#                 for i in range(len(c)):
#                           l=c[i].split()
#                           for word in l:
#                               word=word.lower().strip(string.punctuation)
#                               if word=='':
#                                   continue
#                               elif word in wf:
#                                   wf[word]+=1
#                               else:
#                                   wf[word]=1
#                               sa[word[0]]=sa.get(word[0],0)+1
#                 print("The unique words in this file is  " )
#                 for k,v in wf.items():
#                      if v==1:
#                         print(f"{k:<10}")
#                 sorted_word=sorted(wf.items(),key=lambda x:x[0])
#                 print("Unique words in alphabetical order >> :")
#                 count=0
#                 for k,v in sorted_word:
#                      if v==1:
#                         count+=1
#                         print(f"{k:<10}: {v}")
#                 print(f"the number of unique words in this file is : {count}")
#             break
#         else:
#             print("Enter valid number ! ")
#     else:
#         print("Enter valid name for file !")
# import string 
# def get_file_content(filename):
#     with open(filename,'r') as f:
#                 c=f.readlines()
#                 return c
# def count_word_frequency(line):
#     wf={}
#     for l in line:
#         for word in l.split():
#             word=word.lower().strip(string.punctuation)
#             if word:
#                  wf[word]=wf.get(word,0)+1
#     return wf
# def count_starting_letter(line):
#      cs={}
#      for l in line:
#         for word in l.split():
#             word=word.lower().strip(string.punctuation)
#             if word:
#                  cs[word[0]]=cs.get(word[0],0)+1
#      return cs
# while True:
#     fn=input("enter a file name : ").strip()
#     if fn=='':
#         print("file name cannot be blank ! ")
#     elif not fn.isdigit():
#         n=input("enter how many lines : ").strip()
#         if n.isdigit():
#             n=int(n)
#             with open(fn,'w') as f:
#                 for i in range(n):
#                     while True:
#                         f1=input(f"enter {i+1} line  : ").strip()
#                         if not f1=="":
#                                 f.write(f1.strip()+'\n')
#                                 break
#                         else:
#                             print("enter valid content ! ")
#             c=get_file_content(fn)
#             print("The content of this file is ..")
#             for line in c:
#                  print(line.strip())    
#             wf=count_word_frequency(c)
#             sorted_word=sorted(wf.items(),key=lambda x:x[1],reverse=True)
#             print("The unique words in this file are") 
#             for k,v in sorted_word:
#                     if v==1:
#                         print(f"{k}")
#             print("The top most frequent 3 words are")
#             for k,v in sorted_word[:3]:
#                 print(f"{k:<10}: {v}")
#             print("Starting letter frequency ..")
#             s=count_starting_letter(c)
#             for p,q in s.items():
#                  print(f"{p:<10}: {q}")
#             break
#         else:
#             print("Enter valid number ! ")
#     else:
#         print("Enter valid name for file !")
# num=(3,4,5,2,1)
# # print(f"First no. {num[0]}")
# # print(f"Last no. {num[-1]}")  
# # print(f"Sum {sum(num)}")  
# # print("Is 10 in Tuple?",10 in num)
# set1=set(map(int,input("Enter 4 numbers ").split()))
# set2=set(map(int,input("Enter 4 numbers ").split()))
# print("Union :",set1|set2)
# print("Intersection :",set1&set2)
# print("Symmetric difference :",set1^set2)
# print("difference :",set1-set2) 
# t1=tuple(map(int,input("enter numbers (use space to seperate them) : ").split()))  
# unique=tuple(set(t1))
# print(unique)
# seen=set()   
# unique=[]
# for num in map(int,input("enter numbers (use space to seperate them) : ").split()):
#     if num not in seen:
#         seen.add(num)
#         unique.append(num)
# print(unique)
# a=[]
# t1=tuple(map(int,input("enter numbers (use space to seperate them) :").split()))
# for num in t1:
#     if num%2==0:
#         a.append(num*num)
# print(tuple(sorted(a)))
# club_A = {"Alice", "Bob", "Charlie"}
# club_B = {"Charlie", "David", "Eva"}
# print("The students in both clubs :",club_A&club_B)
# print("All students :",club_A|club_B)
# print("The students in A but not in B :",club_A-club_B)
# print("The students in B but not in A :",club_B-club_A)
# while True:
#     s1=input("Enter first sentence :").strip()
#     if s1=="":
#         print("Input is blank ! ")
#     s2=input("Enter second sentence :").strip()
#     if s2!="" or s1!="":
#         set1=set(s1.split())
#         set2=set(s2.split())
#         print("Unique words from both sentences are :",set1|set2)
#         print("Total number of unique words are : ",len(set1|set2))
#         break
#     else:
#         print("Both sentences cannot be blank ! ")
# try:
#     t1=tuple(map(float,input("Enter 2 numbers(space seperated) :").strip().split()))
#     print("The minimum number is :", min(t1))
#     print("The maximum number is :", max(t1))
#     print("The sum of numbers is :", sum(t1))
#     avg=sum(t1)/len(t1)
#     print(f"The saverage of the numbers is : {avg:.2f}")
# except ValueError:
#     print("Cannot be blank or alphabets")
# def prime(p):
#     if p<=1:
#         return "No"
#     else:
#         for i in range(2,int(p**0.5)+1):
#             if p%i==0:
#                 return 'No'
#         return 'Yes'
# def multiple(m):
#     if m%2==0 or m%3==0:
#         return 'Yes'
#     else:
#         return 'No'
# t1=tuple(map(int,input("Enter first sequence of numbers (space separated):").strip().split()))
# t2=tuple(map(int,input("Enter second sequence of numbers (space separated):").strip().split()))
# s1=set(t1)
# s2=set(t2)
# c=s1&s2
# if not c:
#         print("No common elements ! ")
# else:
#     print("Common numbers are : ",c)
#     print("Checking each common number >>")
#     for s in sorted(c):
#             print(f"{s} is a multiple of 2 or 3 :{multiple(s)}")
#             print(f"{s} is a prime number :{prime(s)}")
# s1=set(tuple(map(int,input("Enter first sequence of numbers (space separated):").strip().split())))
# s2=set(tuple(map(int,input("Enter second sequence of numbers (space separated):").strip().split())))
# print("Common numbers are : ",s1&s2)
# print("The count of common numbers are : ",len(s1&s2))
# print("The numbers that are only in 2nd set : ",s2-s1)
# print("The count of numbers that are only in 2nd set : ",len(s2-s1))
# print("The numbers that are only in 1st set : ",s1-s2)
# print("The count of numbers that are only in 1st set : ",len(s1-s2))
# print("The numbers that are in either set,but not both (symmetric difference) : ",s2^s1)
# print("The  count of numbers that are in either set,but not both (symmetric difference) : ",len(s2^s1))
# t1=tuple(sorted(s1^s2,reverse=True))
# print(f"The tuple with all the unique elements in both sets(no duplicates) : {t1}")
# def count_oddoreven(s2):
#     e=0
#     o=0
#     for n in s2:
#         if n%2==0:
#             e+=1
#         else:
#             o+=1
#     return e,o
# t1=tuple(map(int,input("Enter first sequence of numbers (space separated):").strip().split()))
# s1=sorted(set(t1))
# print (s1)
# print("The smallest number : ",min(s1))
# print("The Largest number : ",max(s1))
# even,odd=count_oddoreven(s1)
# print(f"The count of odd numbers : {odd} ")
# print(f"The count of even numbers : {even} ")
# avg=float(sum(s1)/len(s1))
# print(f"The average :  {avg:.2f}")
# def palindrome(pal):
#     p=[]
#     for word in pal:
#             a=word[::-1]
#             if a.replace(" ", "").lower()==word.replace(" ", "").lower():
#                 p.append(word)
#     return p
# sent1=set(input("Enter first sentence :").strip().split())
# sent2=set(input("Enter second sentence :").strip().split())
# print('The common words are : ',sent1&sent2)
# if sent1&sent2:
#     s1=palindrome(sent1&sent2)
#     if s1:
#         print("palindrome :",s1)
#     else:
#         print("no palindromes present ! ")
# else:
#          print("no palindromes present ! ")
# print('The words only in 1st sentence : ',sent1-sent2)
# if sent1-sent2:
#     s2=palindrome(sent1-sent2)
#     if s2:
#         print("palindrome :",s2)
#     else:
#         print("no palindromes present ! ")
# else:
#     print("no palindromes present ! ")

# print('The words only in 2nd sentence : ',sent2-sent1)
# if sent2-sent1:
#     s3=palindrome(sent2-sent1)
#     if s3:
#         print("palindrome :",s3)
#     else:
#         print("no palindromes present ! ")
# else:
#     print("no palindromes present ! ")
# print('Total count of unique words in both : ',len(sent1|sent2))
# if sent1|sent2:
#     s4=palindrome(sent1|sent2)
#     if s4:
#         print("palindrome in total unique words(both combined) :",s4)
#     else:
#         print("no palindromes present ! ")
# else:
#     print("no palindromes present ! ")
# def is_palindrome(word):
#     word.replace("" ," ").lower()
#     return word==word[::-1]
# def find_palindrome(wordsets):
#     return [word for word in wordsets if is_palindrome(word)]
# sent1=set(input("Enter first sentence :").strip().split())
# sent2=set(input("Enter second sentence :").strip().split())
# word_sets=[("common words",sent1&sent2),
#            ("Only in sentence 1",sent1-sent2),
#            ("Only in sentence 2",sent2-sent1),
#            ("All unique words",sent1|sent2)]
# for desc,words in word_sets:
#     print(f'\n {desc.capitalize()} : {words if words else 'None' }')
#     if words:
#         palindromes=find_palindrome(words)
#         if palindromes:
#             print(f"\n palindrome in {desc} : {palindromes}")
#         else:
#             print("No palindromes found ! ")
#     else:
#         print("No words to check i n this catogory ! ")
# t1=tuple(map(int,input("enter numbers (seperated by space) : ").split()))
# print(tuple((num,num*num) for num in t1 if num%2==0))
# t1=tuple(input("enter words (seperated by space) : ").split())
# v='aeiou'
# print("The words with more than 3 vowels " )
# for words in t1:
#     vc=tuple(w for w in words if w.lower() in v)
#     print(f"\n {words} : {vc if len(vc)>3 else 'not more than 3 vowels'}")

# t1=tuple(input("enter words (seperated by space) : ").split())
# if t1:
#     wd={}
#     for words in t1:
#             wd[words]=wd.get(words,0)+1
#     for w,v in sorted(wd.items(),key=lambda item:item[1],reverse=True):
#             print(f"{w:<10} : {v}")
# else:
#        print("No input given ! ")

# def merge(dict1,dict2):
#     merge={}
#     keys=set(dict1)|set(dict2)     
#     for key in keys:
#         if key in dict1 and key in dict2:
#             if isinstance(dict1[key],int) and isinstance(dict2[key],int):
#                 merge[key]=dict1[key]+dict2[key]
#             else:
#                 merge[key]=dict2[key]
#         elif key in dict1:
#             merge[key]=dict1[key]
#         else:
#             merge[key]=dict2[key]
#     return merge

# dict1={'amal':12,'aju':24,'ali':5,'abu':'10'}
# dict2={'arun':10,'ali':4,'abu':'learn'}        
# combine=merge(dict1,dict2)
# print(combine)

# def countkey(dictlist):
#     keyfrequency={}
#     for dict in dictlist:
#         for key in dict:
#             keyfrequency[key]=keyfrequency.get(key,0)+1
#     return keyfrequency


# dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5, 'c': 6, 'd': 7}]
# frequency=countkey(dicts)
# print(frequency) 

# def mark(student):
#     msum=0
#     topstudent=''
#     maxscience=0
#     avg={}
#     for name,subjects in student.items():
#         for subject,score in subjects.items():
#             msum+=score
#         avg[name]=msum/len(subjects)
#         msum=0
#         if subjects['science']>maxscience:
#             maxscience=subjects['science']
#             topstudent=name
#     return avg,{topstudent:maxscience}


# students = {
#     "Alice": {"math": 85, "science": 92},
#     "Bob": {"math": 78, "science": 81},
#     "Charlie": {"math": 95, "science": 89}
# }
# a,m=mark(students)
# print(a)
# print(m)

# def inventorycalc(inventory):
#     value={}
#     total_value=0
#     high_value=0
#     high_value_item=''
#     for material,detail in inventory.items():
#         for k,v in detail.items():
#                 value[material]= value.get(material,1)*detail[k]
#                 if value[material]>high_value:
#                      high_value=value[material]
#                      high_value_item=material
#         total_value+=value[material]
#     return value,total_value,{high_value_item:high_value}
        

# inventory = {
#     "pen": {"price": 5, "quantity": 20},
#     "notebook": {"price": 30, "quantity": 15},
#     "eraser": {"price": 3, "quantity": 50},
#     "pencil": {"price": 4, "quantity": 60}
# }
# v,tv,hv=inventorycalc(inventory)
# print(v)
# print(tv)
# print(hv)

# def inventorycalc(inventory):
#     value={}
#     total_value=0
#     high_value=0
#     high_value_item=''

#     for material,detail in inventory.items():
#                 item_value=detail['price']*detail['quantity']
#                 value[material]=item_value
#                 total_value+=value[material]

#                 if item_value>high_value:
#                      high_value=value[material]
#                      high_value_item=material

#     return value,total_value,{high_value_item:high_value}
        

# inventory = {
#     "pen": {"price": 5, "quantity": 20},
#     "notebook": {"price": 30, "quantity": 15},
#     "eraser": {"price": 3, "quantity": 50},
#     "pencil": {"price": 4, "quantity": 60}
# }
# v,tv,hv=inventorycalc(inventory)
# print(v)
# print(tv)
# print(hv)

# def common(student):
#     subject_sets=[]
#     for marks in student.values():
#         subject_sets.append(set(marks.keys()))
#     common_subject=subject_sets[0]
#     for i in subject_sets:
#         common_subject=common_subject&i
#     return common_subject

    
        

# students = {
#     "Alice": {"math": 85, "science": 92, "english": 88},
#     "Bob": {"math": 78, "science": 81, "english": 75},
#     "Charlie": {"math": 95, "science": 89, "english": 90}
# }


# print(common(students))


# from functools import reduce

# def common(student):
#     return reduce(lambda x,y:x&y,(set(m.keys())for m in student.values()))
    




# students = {
#       "Alice": {"math": 85, "science": 92, "english": 88},
#       "Bob": {"math": 78, "science": 81, "english": 75},
#       "Charlie": {"math": 95, "science": 89, "english": 90}
#         }

# print(common(students))













            



   





 
    


    





         
        


  


        
            
    

    

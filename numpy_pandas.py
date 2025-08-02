# import numpy as np
# print("Testing NumPy")
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# arr1=np.arange(10,21,2)
# arr2=np.array([[10,20,3],[2,56,73]])
# arr3=np.zeros((5,5))
# arr4=np.random.rand(5,6,2,2)
# arr5=np.ones((4,6))
# arr6=np.full((2,3),5)
# arr7=np.eye(4)
# arr8=np.linspace(1,2,4)
# arr2.shape=(3,)
# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)
# print(arr5)

# arr4=np.random.choice(['cat', 'dog', 'cow'],size=3,replace=True,p=[0.1,0.7,0.2])
# students = ['Aman', 'Neha', 'Ravi', 'Priya', 'Ali', 'Sara', 'Karan', 'Meena', 'John', 'Anjali']
# arr5=np.random.choice(students,size=3,replace=False)
# dice=np.random.choice([1,2,3,4,5,6],size=10,replace=True)
# players = ['Alice', 'Bob', 'Charlie', 'David']
# lottery=np.random.choice(players,size=1,p=[0.4, 0.3, 0.2, 0.1])
# chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
# password=np.random.choice(chars,size=8,replace=True)
# print(arr5)
# print(arr5.shape)
# print(arr5.ndim)
# print(arr5.dtype)
# print(arr5.size)
# print(dice)
# print(dice.shape)
# print(dice.ndim)
# print(dice.dtype)
# print(dice.size)
# print(lottery)
# print(lottery.shape)
# print(lottery.ndim)
# print(lottery.dtype)
# print(lottery.size)
# print(password)
# print(password.shape)
# print(password.ndim)
# print(password.dtype)
# print(password.size)
# arr5=np.array([['Student','Math','Physics','Chemistry'],['A',78,82,89],['B',92,88,79],['C',84,76,91],['D',67,90,85],['E',73,68,77]])
# print(arr5)
# print(f"Mark of student B :\n{arr5[0]}\n{arr5[2]}")
# print(arr5[][3])
# names=['A','B','C','D','E']
# subject=['Math','Physics','Chemistry']
# MARKS=np.array([[78,82,89],[92,88,79],[84,76,91],[67,90,85],[73,68,77]])
# print(names)
# print(MARKS)
# print(f"Mark of student B :{MARKS[1]}")
# print(f"Physics Marks : {MARKS[:,1]}")
# print(f"Average Marks per student")
# for i,avg in enumerate(MARKS.mean(axis=1)):
#         print(f"{names[i]} : {avg:.2f}")   
# print(f"Highest Chemistry mark : {(MARKS[:,2]).max()}")  
# print(f"Average Marks per subject")
# for i,avg in enumerate(MARKS.mean(axis=0)):
#         print(f"{subject[i]} : {avg:.2f}")  
# marksubject={}
# sm=0
# print(f"total Marks per student") 
# for i,s in enumerate(MARKS.sum(axis=1)):
#         print(f"{names[i]} : {s:.2f}")
# highest_total_student_index=np.argmax(MARKS.sum(axis=1))
# print(f"student with highest mark is : {names[highest_total_student_index]} - {(MARKS.sum(axis=1)).max()}")
# print("average marks for each subject")
# for i,avg in enumerate(MARKS.mean(axis=0)):
#         print(f"{subject[i]} : {avg:.2f}")
# average_subject_marks=MARKS.mean(axis=0)
# highest_average_subject_index=np.argmax(average_subject_marks)
# print(f"highest average subject \n{subject[highest_average_subject_index]} :  {average_subject_marks[highest_average_subject_index]}")
# normalized_marks=(MARKS-MARKS.min())/(MARKS.max()-MARKS.min())
# print(f"normalized marks : \n{normalized_marks}")


# normalized_l=[]
# sample=np.random.randint(1,101,(10,5))
# for i in range(5):
#         f_normalized=(sample[:,i]-sample[:,i].min())/(sample[:,i].max()-sample[:,i].min())
#         normalized_l.append(f_normalized)
# normalized_new=np.array(normalized_l)
# print(normalized_new)

# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# row_add = np.array([10, 20, 30])
# Add row_add to each row of arr using broadcasting
# new_arr=arr+row_add
# print(new_arr)
# marks = np.array([78, 92, 65, 88, 45, 99, 71])
# Extract all marks greater than 80
# Set all marks less than 50 to 50
# mark_greater_80=marks>80
# mark_less_50=marks<50
# print(mark_less_50)
# print(mark_greater_80)
# marks_new=marks[mark_greater_80]
# print(marks_new)
# marks[mark_less_50]=50
# print(marks)


# students = np.array(["A", "B", "C", "D", "E"])
# scores = np.array([70, 85, 60, 90, 75])
# Use an index list [3, 1, 4] to extract students' names and scores
# ind=[3,1,4]

# selected_students=students[ind]
# selected_score=scores[ind]
# for name,score in zip(selected_students,selected_score):
#     print(f"Student : {name} , Score : {score}")
# print(selected_students)
# print(scores)

# def max_sum_array(ar):
#     sum=0
#     for i in ar:
#         total+=i
#     return total
# def max_sum_arr(ar):
#     return sum(ar)
# a=(7,7)
# print(max_sum_array(a))

# def second_largest(arr):
#     unique_arr=sorted(set(arr))
#     if len(unique_arr)<2:
#         return None
#     else:
#         return unique_arr[-2]



# print(second_largest(a))

# np.array([[1], [2], [3]]) + np.array([10, 20, 30])
# arr1=np.arange(1,13)

# brr1=arr1.reshape(3,4)
# brr2=arr1.reshape(4,3)
# print(arr1)
# print(brr1)
# print(brr2)
# new_arr=brr1.ravel()
# new_arr2=brr1.flatten()
# new_brr2=brr2.ravel()
# new_brr=brr2.flatten()

# print(new_arr)
# print(new_arr2)
# print(new_brr2)
# print(new_brr)


# print(brr1)
# print(brr2)
# print(arr1)
# new_brr2[1]=200
# new_brr[0]=100

# print(new_brr2)
# print(new_brr)
# print(arr1)
# print("Is new_brr2 a view of brr2?", new_brr2.base is arr1)  # Should be True
# print("Is new_brr a view of brr2?", new_brr.base is arr1)    # Should be False


# a=np.array([[1,2,3],[56,7,3]])
# b=np.array([[4,5,6]])
# c=np.vstack((a,b))
# con1=np.concatenate((a,b),axis=0)
# print(c)
# print(con1)
# d=np.array([[1,2],[3,4]])
# print(d)
# e=np.array([[5,6,8],[7,8,9]])
# print(e)
# f=np.hstack((d,e))
# print(f)
# con2=np.concatenate((d,e),axis=1)
# print(con2)


# a = [[1,2,3],[4,5,6],[4,6,3]]
# b = [[7,8,9],[10,11,12],[4,6,3]]
# v=np.vstack((a,b))
# h=np.hstack((a,b))
# print(v)
# print(h)
# c1=np.concatenate((a,b),axis=0)
# c2=np.concatenate((a,b),axis=1)
# print(c1)
# print(c2)
# s1=np.stack((a,b),axis=0)
# s2=np.stack((a,b),axis=1)
# print(s1)
# print(s2)
# print(s1.shape)
# print(s2.shape)
# print(s1.ndim)
# print(s2.ndim)

# a=np.random.randint(1,10,(2,3,4,5))
# print(a)
# print(f"sum at axis 0 : {np.sum(a,axis=0)}")
# print(f"sum at axis 1 : {np.sum(a,axis=1)}")
# print(f"sum at axis 2 : {np.sum(a,axis=2)}")
# print(f"sum at axis 3 : {np.sum(a,axis=3)}")
# a = np.array([[1,2,3], 
#               [4,5,6]])
# b = np.array([[10,20,30],
#                [40,50,60]])
# stacked2 = np.stack((a, b), axis=2)
# stacked1 = np.stack((a, b), axis=1)
# stacked0= np.stack((a, b), axis=0)

# print(stacked2)
# print("Shape:", stacked2.shape)
# print(stacked1)
# print("Shape:", stacked1.shape)
# print(stacked0)
# print("Shape:", stacked0.shape)

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# s = np.stack((a, b), axis=1)  # Try changing to axis=0 too
# print(s)
# flat = s.flatten()
# print(flat)

# a=np.array([1,2,3])
# b=np.array([[10],[20]])
# result=a+b
# print(result)
# a = np.array([[1,2], [3,4]])
# b = np.array([[5,6], [7,8]])
# c = np.array([[9,10], [11,12]])
# d=np.vstack((a,b,c))
# e=np.hstack((a,b,c))
# f=np.concatenate((a,b,c),axis=1)
# print(d)
# print(e)
# print(f)
# Try vstack, hstack, concatenate(axis=0), concatenate(axis=1)
# import numpy as np

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])
# b = np.array([[7, 8, 9],
#               [10,11,12]])

# s0 = np.stack((a, b), axis=0)
# s1 = np.stack((a, b), axis=1)
# s2 = np.stack((a, b), axis=2)

# print("axis=0 →", s0.shape)
# print("axis=1 →", s1.shape)
# print("axis=2 →", s2.shape)

# print("stacked[0, 0] (axis=0):", s0[0, 0])
# print("stacked[0, 0, 0] (axis=2):", s2[0, 0, 0])

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[10, 20], [30, 40]])

# stacked = np.stack((a, b), axis=0)
# print("Stacked shape:", stacked.shape)

# # Try these:
# print("Sum along axis=0:\n", np.sum(stacked, axis=0))
# print("Sum along axis=1:\n", np.sum(stacked, axis=1))
# print("Sum along axis=2:\n", np.sum(stacked, axis=2))

# a = np.array([[10, 20, 30], [40, 50, 60]])
# b = np.array([[1, 2, 3], [4, 5, 6]])
# s0=np.stack((a,b),axis=0)
# s1=np.stack((a,b),axis=1)
# s2=np.stack((a,b),axis=2)
# print(f"Axis 0 ->{s0}")
# print(f"Axis 0 shape->{s0.shape}")
# print(f"Axis 1 ->{s1}")
# print(f"Axis 1 shape->{s1.shape}")
# print(f"Axis 2 ->{s2}")
# print(f"Axis 2 shape->{s2.shape}")
# import numpy as np

# img1=np.array([[[255, 0, 0],
#                  [0, 255, 0]],
#               [[0, 0, 255],
#                 [255, 255, 0]]])
# img2=np.array([[[0, 0, 0], 
#                 [127, 127, 127]],
#                  [[200, 100, 50], 
#                   [25, 75, 125]]])
# s0img1=np.stack((img1,img2),axis=0)
# s1img1=np.stack((img1,img2),axis=1)
# s2img1=np.stack((img1,img2),axis=2)
# s1img2=np.stack((img1,img2),axis=3)
# print(s1img1)
# print(s1img1.shape)
# print(s2img1)
# print(s2img1.shape)
# print(f"shape of s0img1 : {s0img1.shape}")
# print(s0img1)
# print(f"shape of s1img2 : {s1img2.shape}")
# print(s1img2)

# img1=np.random.randint(0, 255, (28,28))
# img2=np.random.randint(0,255,(28,28))
# img3=np.random.randint(0,255,(28,28))
# img4=np.random.randint(0,255,(28,28))
# batch4=np.stack((img1,img2,img3,img4),axis=0)
# batch_with_channel=np.expand_dims(batch4,axis=-1)
# batch_with_channel=np.stack((batch4,)*3,axis=-1)
# batch_with_channel=batch4[...,np.newaxis]
# batch_with_channel=batch4.reshape(4,28, 28, 1)  # Reshape to add channel dimension
# batch_with_channel=np.repeat(batch_with_channel,3,axis=-1)  # Adding 3 channels (RGB)
# print(batch4.shape)
# print(batch_with_channel.shape)
# print(batch_with_channel[0].shape)
# print(batch_with_channel[0][0].shape)  
# print(batch_with_channel[0][0][0].shape)
# import numpy as np
# arr=np.arange(1,13)
# print(arr)
# print(arr.reshape(3,4))
# print(arr.reshape(4,3))
# print(arr.reshape(2,6))
# print(arr.reshape(-1,2,3))  # Automatically determine the first dimension size
# print(arr)
# arr24=np.arange(0,24)
# re124=arr24.reshape(4,-1)
# re224=arr24.reshape(-1,6)
# print(re124)
# print(re224)
# rav=(re124.ravel())
# fla=(re124.flatten())
# rav[0]=299
# fla[0]=100
# print(rav)
# print(fla)
# print(re124)    


# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# b = np.array([[7, 8, 9],
#               [10, 11, 12]])
# g=np.row_stack((a,b))
# h=np.column_stack((a,b))
# print(h)
# print(g)

# c=np.hstack((a,b))
# d=np.vstack((a,b))
# e=np.concatenate((a,b),axis=0)
# f=np.concatenate((a,b),axis=1)
# print(c)
# print(d)
# print(e)
# print(f)

# import numpy as np

# arr = np.array([[10, 20, 30],
#                 [40, 50, 60],
#                 [70, 80, 90]])

# print(arr)
# print(f"mean : {np.mean(arr)}")
# print(f"mean row wise : {np.mean(arr,axis=1)}")
# print(f"mean column wise : {np.mean(arr,axis=0)}")

# print(f"standard deviation : {np.std(arr)}")
# print(f"variance : {np.var(arr)}")
# print(f"Percentile : {np.percentile(arr,25)}")

# print(f"standard deviation : {np.std(arr,axis=0)}")
# print(f"variance : {np.var(arr,axis=0)}")
# print(f"Percentile : {np.percentile(arr,50)}")

# print(f"standard deviation : {np.std(arr,axis=1)}")
# print(f"variance : {np.var(arr,axis=1)}")
# print(f"Percentile : {np.percentile(arr,75)}")


# print(f"median : {np.median(arr,axis=1)}")



# students=["Alice","Bob","Charlie"]

# subjects = ['Math', 'Science', 'History', 'English']

# marks = np.array([
#     [85, 92, 78, 90],   # Alice
#     [75, 80, 85, 88],   # Bob
#     [95, 88, 92, 96]    # Charlie
# ])

# totals=np.sum(marks,axis=1)
# averages=np.mean(marks,axis=1)

# def grade(avg):
#     if avg>=90:
#         return "A"
#     elif avg>=80:
#         return "B"
#     elif avg>=70:
#         return "C"
#     elif avg>=60:
#         return "D"
#     else:
#         return "FAIL"
    
# grades=[grade(avg) for avg in averages]
# print("Student Report Card")
# for i in range(len(students)):
#     print(f"\nReport for {students[i]}:")
#     for j in range(len(subjects)):
#         print(f"{subjects[j]} :{marks[i][j]}")
#     print(f"Total: {totals[i]}")
#     print(f"Average: {averages[i]:.2f}")
#     print(f"Grade: {grades[i]}")
# rank=np.argsort(-totals)
# print("Student Ranking")
# for rank,id in enumerate(rank,start=1):
#     print(f"{rank} . {students[id]} - Total : {totals[id]}")
# data=[]
# for i in range(len(students)):
#     student_data =[students[i]]+list(marks[i])+[totals[i],averages[i],grades[i]]
#     data.append(student_data)
# column=['name']+subjects+['Total','Average','Grade']
# df=pd.DataFrame(data,columns=column)
# print("generated report card")
# print(df)
# df.to_csv('student report card.csv',index=False)
# df.to_excel('student report card.xlsx',index=False)
# print("\n Report exported to 'student_report_card.xlsx'")
# print("\n Report exported to 'student_report_card.csv'")

# def isValid( s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
    
#     for char in s:
#         if char in mapping.values():
#             stack.append(char)
#         elif char in mapping.keys():
#             if not stack or stack[-1] != mapping[char]:
#                 return False
#             stack.pop()
    
#     return not stack
# isvalud=isValid("()[]{}")
# print(f"Is the string valid? {isvalud}")

# def isValid(s):
#     if not s or s is None:
#         return False
#     if len(s)%2!= 0:
#         return False
#     else:
#         stack=[]
#         for char in s:
#             if char=='(' or char=='{' or char=='[':
#                 stack.append(char)
#                 continue
#             if char==')':
#                 stack_char=stack.pop() if stack else None
#                 if stack_char=='(':
#                     continue
#                 else:
#                     return False
#             if char==']':
#                 stack_char=stack.pop() if stack else None
#                 if stack_char=='[':
#                     continue
#                 else:
#                     return False
#             if char=='}':
#                 stack_char=stack.pop() if stack else None
#                 if stack_char=='{':
#                     continue
#                 else:
#                     return False
#         return not stack
# isvalud=isValid("()[]{}")
# print(f"Is the string valid? {isvalud}")



# def isValid(s):
#     if not s or s is None:
#         return False
#     if len(s)%2!= 0:
#         return False
#     else:
#         stack=[]
#         v={')':'(',']':'[','}':'{'}
#         for char in s:
#             if char==v.values():
#                 stack.append(char)
#                 continue
#             if char==v.keys():
#                 if stack[-1]==v[char]:
#                     continue
#                 else:
#                     return False
#         return not stack
    
# isvalud=isValid("()[]{}")
# print(f"Is the string valid? {isvalud}")



# class Stack():
#     def __init__(self):
#             self.stack=[]
#             self.minstack=[]
#     def push(self,val):
#          self.stack.append(val)
#          val=min(val,self.minstack[-1] if self.minstack else val)
#          self.minstack.append(val)
#     def pop(self):
#          self.stack.pop()
#          self.minstack.pop()
#     def minofstack(self):
#          return self.minstack[-1]
#     def top(self):
#          return self.stack[-1]

import numpy as np
import pandas as pd

# arr1=np.array([[2,4,6],[5,6,2]])
# arr1+=5
# print(arr1)
# arr2=np.array([[2,4,6],
#                [5,6,2],
#                [5,6,2]])
# arr3=np.array([2,8,4])
# col = np.array([[1], [2], [3]])
# arrm=arr2*arr3
# print(arrm)
# print(arr2-col)

# arr = np.array([[1,2,3],
#                  [4,5,6], 
#                  [7,8,9]])
# row = np.array([10, 20, 30])
# # Your code here
# print(arr+row)

# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# col = np.array([[2],
#                 [3], 
#                 [4]])
# # Your code here
# print(arr*col)
# arr = np.arange(18).reshape(2, 3, 3)
# vec = np.array([1, 10, 100])
# print(arr)
# print(arr+vec)
# print(vec.shape)
# # Your code here

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# # Your code here
# print(10-arr)


# ar=np.arange(27).reshape(3,3,3)
# print(ar-vec)

# arr=np.array([[1],
#               [2],
#               [3]])
# arr2=np.array([10,20,30,40])
# result=arr*arr2
# print(result)
# print(result.shape)

# main=np.arange(24).reshape(2,3,4)
# arr3=np.array([[10],[20],[30]])
# print(main+arr3)


# arr5=np.arange(15).reshape(5,3)
# print(arr5)
# min_vals=np.min(arr5,axis=0)
# max_vals=np.max(arr5,axis=0)
# print(min_vals)
# print(max_vals)
# arr5normal=(arr5-min_vals)/(max_vals-min_vals)
# print(arr5normal)


# import numpy as np

# arr = np.array([[10, 20, 30],
#                 [5, 5, 100],
#                 [50, 70, 90],
#                 [0, 1, 2]])

# Step 1: Find row-wise min and max
# Your code here

# min_val=np.min(arr,axis=1,keepdims=True)
# max_val=np.max(arr,axis=1).reshape(-1,1)
# print(min_val)
# print(max_val)

# Step 2: Perform row-wise normalization using broadcasting
# Your code here
# arr_normal1=(arr[0]-min_val[0])/(max_val[0]-min_val[0])
# print(arr_normal1)
# arr_normal2=(arr[1]-min_val[1])/(max_val[1]-min_val[1])
# arr_normal3=(arr[2]-min_val[2])/(max_val[2]-min_val[2])
# arr_normal4=(arr[3]-min_val[3])/(max_val[3]-min_val[3])
# # Step 3: Print the normalized array
# # Your code here
# normal_arr=([arr_normal1,arr_normal2,arr_normal3,arr_normal4]).reshape(4,3)
# print(normal_arr)
# arr_normal=(arr-min_val)/(max_val-min_val)
# print(arr_normal)

# arr=np.arange(24).reshape(4,3,2)
# print(arr)
# arr2=np.array([2,4])
# print(arr-arr2)

# arr3=arr.reshape(2,3,4)
# print(arr3)
# min_val=np.min(arr3,axis=2,keepdims=True)
# max_val=np.max(arr3,axis=2,keepdims=True)
# print(min_val)
# print(max_val)
# normal_arr3=(arr3-min_val)/(max_val-min_val)
# print(normal_arr3)


# arr = np.arange(24).reshape(2, 3, 4)
# print("Original Array:\n", arr)


# min_val=np.min(arr)
# max_val=np.max(arr)
# normalized_arr=(arr-min_val)/(max_val-min_val)
# print(normalized_arr)



# arr = np.random.randint(10, 100, size=(3, 4, 2))
# print("Original:\n", arr)


# min_val=np.min(arr,axis=0,keepdims=True)
# max_val=np.max(arr,axis=0,keepdims=True)
# normalized_arr=(arr-min_val)/(max_val-min_val)
# print(normalized_arr)

# arr = np.array([[1, 2, 3], 
#                 [4, 5, 6], 
#                 [7, 8, 9]])
# mask = np.array([[0, 1, 0], 
#                  [1, 0, 1], 
#                  [0, 1, 0]])

# for i in range(3):
#     for j in range(3):
#         if mask[i][j]==1:
#             arr[i][j]=arr[i][j]*mask[i][j]
# print(arr)

# Multiply only where mask is 1
# Your code here



# arr=arr.astype(float)
# print(arr)

# for s in range(3):
#     for i in range(4):
#         for j in range(2):
#             if arr[s][i][j]>50:
#                 arr[s][i][j]=(arr[s][i][j]-min_val)/(max_val-min_val)
# print(arr)

# arr=np.random.randint(10,100,size=(3,4,2)).astype(float)
# min_val=np.min(arr)
# max_val=np.max(arr)
# mask=arr>50
# print(mask)
# arr[mask]=(arr[mask]-min_val)/(max_val-min_val)
# print(arr)


# arr = np.array([[12, 54, 63, 25],
#                 [42, 65, 77, 12],
#                 [90, 45, 32, 11]])

# mask = np.array([[1, 0, 1, 0],
#                  [0, 1, 1, 0],
#                  [1, 1, 0, 0]])
# arr=arr.astype(float)
# min_val=np.min(arr)
# print(min_val)

# max_val=np.max(arr)
# print(max_val)
# mask=mask==1
# print(mask)
# arr[mask]=(arr[mask]-min_val)/(max_val-min_val)
# print(arr)
np.set_printoptions(suppress=True)
# print(arr)
# Task:
# For each row, normalize only the values where mask == 1
# Other values (mask==0) should stay untouched
def reshape_axis_broadcast(selector,target_axis,target_shape):
    new=len(target_shape)
    if 0<=target_axis<new:
        if selector.ndim>2:
            print("selector has more than 2 dimensions, cannot reshape")
        else:
            new_shape=[1]*new
            size=selector.shape[-1] if selector.ndim==2 else selector.shape[0]
            if size!=target_shape[target_axis]:
                print("target axis doest not match with intended size")
            else:
                new_shape[target_axis]=size
                return new_shape


arr = np.random.randint(1, 10, size=(3, 4, 5))
print(arr)
selector = np.array([[1, 0, 1, 0]])
print(selector)
selector=selector==1
print(selector)
print(selector.shape)
shape=reshape_axis_broadcast(selector,1,arr.shape)
selector=selector.reshape(shape)
print(selector.shape)
print(selector)
# Add a new axis to match arr's shape
arr=arr*selector*10+arr*(~selector)

print(arr)


# Task:
# 1. Broadcast `selector` across arr axis 1
# 2. Multiply `arr` values only in the slices where selector == 1 by 10


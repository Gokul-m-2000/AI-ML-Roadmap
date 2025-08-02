import pandas as pd
import numpy as np
# a=[2,5,7,7,3]
# marks=pd.Series(a)
# marks.index=["maths","physics","chemistry","biology","english"]
# print(marks.index)
# print(marks.values)
# print(marks)
# print(marks["maths"])
# print(marks[:3])
# marks+=5
# print(marks)
# print(marks[marks>10])

# b={'arun':56,'amal':89,'ajal':45}
# s2=pd.Series(b)
# print(s2)
# c=np.arange(20).reshape(4,5)
# s3=pd.Series(c)
# print(s3)

# subject=["english","maths","science","social"]
# internal_marks=pd.Series([10,20,30,40],index=subject)
# external_marks=pd.Series([20,30,40,50],index=["english","maths","hindi","social"])
# n=internal_marks+external_marks
# print(internal_marks)
# print(external_marks)
# print(n)
# print(external_marks.get('malayalam'))


internal = pd.Series({"maths": 45, "science": 40, "english": 35, "hindi": 48})
external = pd.Series({"maths": 40, "science": 35, "english": 38, "social": 42})
total_marks = internal + external
print(total_marks)
total_marks=total_marks.fillna(0)
print(total_marks)
sorted_values=total_marks.sort_values(ascending=False)
print(sorted_values)
final=total_marks.apply(lambda x:"Excelent" if x>80 else "pass")
print(final)
print(total_marks[total_marks>80])
print(total_marks)
print(total_marks[sorted_values.values])
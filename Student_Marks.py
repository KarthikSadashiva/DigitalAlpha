import pandas as pd
import numpy as np

stu1 = [68,74,85,94]
stu2 = [78,98,78,84]
stu3 = [89,91,79,88]
stu4 = [68,86,86,95]

marks = np.array([stu1,stu2,stu3,stu4]).reshape(4,4)
Student_Marks = pd.DataFrame(marks,index=[np.arange(1,5)],columns=['sub1','sub2','sub3','sub4'])
print(Student_Marks)
print(Student_Marks.T.max())

Student_Marks['Total'] = Student_Marks['sub1']+Student_Marks['sub2']+Student_Marks['sub3']+Student_Marks['sub4']
print(Student_Marks)

print("The roll number of topper is",Student_Marks['Total'].idxmax()[0],"and his total marks is",Student_Marks['Total'].max())

print("student 1 sorted marks",sorted(stu1))
print("student 2 sorted marks",sorted(stu2))
print("student 3 sorted marks",sorted(stu3))
print("student 4 sorted marks",sorted(stu4))

Student_Marks.loc[5] = [79,75,82,94,sum([79,75,82,94])]
Student_Marks.loc[6] = [61,83,73,99,sum([61,83,73,99])]

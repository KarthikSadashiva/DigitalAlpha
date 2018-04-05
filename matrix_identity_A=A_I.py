import numpy
A = numpy.array([[3.0, 5.0, 6.0], [4.0, 8.0, 10.0], [2.0, 1.0, 8.0]])
I = numpy.identity(3)
A_dot_I = numpy.matmul(A,I)
a = numpy.size(A,0)*numpy.size(A,1)
for i in range(numpy.size(A,0)):
    for j in range(numpy.size(A,1)):
        if(A[i][j] == A_dot_I[i][j]):
            a = a-1
        else:
            a = a
if(a==0):
    print("A = A.I")
else:
    print("A not equal to A.I")

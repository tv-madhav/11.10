#(You are given a number N and find all the distinct factors of N.
#Input:
#First-line will contain the number N.
#Output:
#In the first line print number of distinct factors of N.
#In the second line print all distinct factors in ascending order separated by space.
#Constraints
#1≤N≤106
#Sample Input 1:
#4
#Sample Output 1:
#3
#1 2 4
#Sample Input 2:
#6
#Sample Output 2:
#4
#1 2 3 6

#Solution:
#python-tvm
N = int(input())
fac = []
ans = 0
for i in range(1,N+1):
    if N%i == 0:
        ans += 1
        fac.append(i)
print(ans)
for j in fac:
    print(j, end=" ")

#Problem
#Given an Integer N, write a program to reverse it.

#Input
#The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

#Output
#For each test case, display the reverse of the given number N, in a new line.

#(Constraints 1 ≤ T ≤ 1000 , 1 ≤ N ≤ 1000000) # Sample 1: Input Output
#(4 12345 31203 2123 2300 54321 30213 3212 32)

t = int(input())
for i in range(t):
    reverse = 0
    num = int(input())
    while(num):
        remainder = num%10
        reverse =reverse*10+remainder
        num = int(num/10)
    print(reverse)


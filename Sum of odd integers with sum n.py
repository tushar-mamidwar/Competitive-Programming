#Count of ways to generate Sequence of distinct consecutive odd integers with sum N
"""
Given an integer N,  the task is to find the total number of ways a sequence can be formed consisting of distinct consecutive odd integers that add up to N.

Examples:

Input: N = 45
Output: 3
Explanation: 3 ways to choose distinct consecutive odd numbers that add up to 45 are – 
{5, 7, 9, 11, 13}, {13, 15, 17} and {45}.

Input : N = 20
Output : 1
Explanation: 9 and 11 are the only consecutive odd numbers whose sum is 20
"""
import math
N=int(input())

#Naive Approach TC=O^2
print("Naive Approach:", end="")
i=1
count=0
while i<=N:
    sum=0
    j=i
    while sum<N:
        sum+=j
        j+=2
    if sum==N:
        count+=1
    i+=2
print(count)

#Better Approach TC=O√n
print("Better Approach:", end="")
count=0
i=1
nsqrt=math.sqrt(N)
while i<=nsqrt: #based on finding all the divisors of a number
    if N%i==0 and (N/i+i)%2==0: #N/i and i are the two divisors whose sum should be even
        count+=1
    i+=1
print(count)

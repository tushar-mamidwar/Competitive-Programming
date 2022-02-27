#Count of 3 sized Strings of all same or different characters using total X 0s, Y 1s and Z 2s
"""
Given three integers X, Y and Z denoting the frequencies of three different characters ‘0‘, ‘1‘, and ‘2’ respectively. the task is to find the maximum number of valid strings of length three that can be formed using the given frequencies such that in each string all the three characters are same or all are different.

Examples:

Input: X = 3, Y = 5, Z = 5
Output: 4
Explanation: Valid strings that can be obtained from the given frequencies: “102”, “012”, “111”, “222”.
Number of strings = 4.

Input: X = 8, Y = 8, Z = 9
Output: 8
"""
x,y,z=map(int,input().split())
count=0
for i in range(0,3):
    if x<i or y<i or z<i:
        break
    xremain,yremian,zremain=x-i,y-i,z-i
    count=max(count,i+xremain//3+yremian//3+zremain//3)
print(count)

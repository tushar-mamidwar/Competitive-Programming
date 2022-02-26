# Count of Subarrays whose first element is the minimum
"""
Given an array arr[] of size N, the task is to find the number of subarrays whose first element 
is not greater than other elements of the subarray.

Examples:

Input: arr = {1, 2, 1}
Output: 5
Explanation: All subarray are: {1}, {1, 2}, {1, 2, 1}, {2}, {2, 1}, {1}
From above subarray the following meets the condition: {1}, {1, 2}, {1, 2, 1}, {2}, {1}

Input: arr[] = {1, 3, 5, 2}
Output: 8
Explanation: We have the following subarrays which meet the condition:
{1}, {1, 3}, {1, 3, 5}, {1, 3, 5, 2}, {3}, {3, 5}, {5}, {2}
"""
count=0
arr=[1, 3, 5, 2]
for i in range(len(arr)):
    subarr=[]
    for j in range(i,len(arr)):
        subarr.append(arr[j])
        if min(subarr)==subarr[0]:
            count+=1
print(count)  

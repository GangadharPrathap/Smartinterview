/*
Find Duplicate Number in Array bookmark_borderFind a duplicate element in the given array of integers. There will be only a single duplicate element in the array.

Note: 
 Do not use any inbuilt functions / libraries for your main logic  Input Format
The first line of input contains the size of the array - N and the second line contains the elements of the array, there will be only a single duplicate element in the array.

Output Format
Print the duplicate element from the given array.

Constraints
2 <= N <= 100
0 <= ar[i] <= 109

Example
Input
8
5 4 10 9 21 10 3 10

Output
10

Explanation

Self Explanatory
*/

n=int(input())
num = list(map(int,input().split()))
dup=None
for i in range(n):
    for j in range(i+1,n):
        if num[i] == num[j]:
            dup = num[i]
            break
    if dup is not None:
        break
print(dup)                

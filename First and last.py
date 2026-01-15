/*
First and Last bookmark_borderYou are given an array A of size N, containing integers. Your task is to find the first and last occurrences of a given element X in the array A and print them.

Input Format
The input consists of three lines. The first line contains a single integer N - the size of the array. The second line contains N integers separated by a space, representing the elements of the array A. The third line contains a single integer X.

Output Format
Print the indexes of the first and last occurrences separated by a space.

Note
It is guaranteed that X is always present in the given array.

Constraints
1 <= N <= 103
1 <= A[i] <= 105
X ∈ A

Example
Input
10
1 3 5 7 9 11 3 13 15 3
3

Output
1 9

Explanation

Self Explanatory
*/
n=int(input())
arr = list(map(int,input().split()))
x= int(input())
findex = -1
lindex = -1

for i in range(n):
    if arr[i] == x:
        findex = i
        break
for i in range(n-1,-1,-1):
    if arr[i] == x:
        lindex = i 
        break
print(findex,lindex)                       

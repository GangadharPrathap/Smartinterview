Number Distribution 
Number Distribution bookmark_borderPrint the count of the occurrences of positive integers, negative integers, and zeroes in the given array.

Input Format
The first line of the input contains an integer N - size of the array, second line of input contains an array elements of the array.

Output Format
Print the frequencies of zeroes, positives elements and negative elements.

Constraints
1 <= N <= 104
-103 <= arr[i] <= 103

Example
Input
10
120 0 -9 89 68 -982 91 -54 -12 -139

Output
1 4 5

Explanation

n=int(input())
arr=list(map(int,input().split()))
z=0
p=0
n=0
for i in arr:
    if i == 0:
        z+=1
    elif i>0:
        p+=1
    else:
        n+=1

print(z,p,n)



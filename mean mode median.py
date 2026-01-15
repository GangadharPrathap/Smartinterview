/*
Mean Median Mode bookmark_borderGiven a sorted array A, containing N integers. Calculate and print their Mean, Median and Mode.

1. For both the Mean and Median, display the values with precision up to two decimal places.
2. Print the first Mode that you encounter from the left hand side.

Input Format
First line of input contains integer N - the size of the array. Second line of input contains N integers - elements of the array A.

Output Format
Print Mean, Median and Mode, separated by spaces.

Constraints
1 <= N <=104
0 <= A[i] <=100

Example
Input
8
1 2 3 4 5 5 6 6

Output
4.00 4.50 5

Explanation:

The Mean is 32 / 8 = 4.00 [rounded to 2 decimals]
The Median is (4+5) / 2 = 4.50
For the given example, {5, 6} represents the Mode of the array, we'll print 5 as it's the first Mode encountered.
*/

n=int(input())
arr=list(map(int,input().split()))
mean = sum(arr)/n

if n%2 == 0:
    median = (arr[n//2-1]+arr[n//2])/2
else:
    median = arr[n//2]

max_freq = 0
mode = arr[0]

cfreq = 1

for i in range(1,n):
    if arr[i] == arr[i-1]:
        cfreq +=1
    else:
        if cfreq > max_freq:
            max_freq = cfreq
            mode = arr[i-1]
        cfreq = 1
if cfreq > max_freq:
    mode = arr[n-1]
print(f"{mean:.2f}{median: .2f} {mode}")                     

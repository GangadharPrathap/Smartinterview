/*
Unique Elements bookmark_borderPrint unique elements of the array in the same order as they appear in the input.

Note: 
 Do not use any inbuilt functions / libraries for your main logic.  Input Format
The first line of input contains the size of the array - N and the second line contains the elements of the array.

Output Format
Print unique elements from the given array.

Constraints
1 <= N <= 100
0 <= ar[i] <= 109

Example
Input
7
5 4 10 9 21 4 10

Output
5 9 21

Explanation

Self Explanatory
*/# 1. Read the size of the array
n = int(input())

# 2. Read the elements as a list of integers
arr = list(map(int, input().split()))

# 3. Create a list to store the unique numbers found
unique_elements = []

# 4. Main Logic: Check every element
for i in range(n):
    current_val = arr[i]
    count = 0
    
    # Inner loop: count how many times current_val appears in the whole array
    for j in range(n):
        if arr[j] == current_val:
            count += 1
            
    # 5. If it appears exactly once, it is unique
    if count == 1:
        unique_elements.append(current_val)

# 6. Print the unique elements separated by a space
# We use * to unpack the list for clean printing
print(*unique_elements)

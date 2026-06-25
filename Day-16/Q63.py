# Write a program to Find pair with given sum

arr = [1, 4, 5, 6, 8, 2]        #Given array
s = 10                          #Here, s is the target sum


n = 0
for x in arr:
    n = n + 1

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == s:
            print(arr[i], arr[j])
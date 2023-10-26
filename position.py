def find_index(arr, n, K):
	for i in range(n):
		if arr[i] == K:
			return i
		elif arr[i] > K:
			return i
	return n
arr = [1, 3, 5, 6, 8, 10, 12, 15]
n = len(arr)
K =int(input("enter the value to find the position:"))
print(find_index(arr, n, K))

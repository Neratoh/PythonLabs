n = int(input("n = "))

print(f"Enter {n} array elements:")

arr = [int(input()) for _ in range(n)]
arr1 = arr[::-1]

print("Original array: ", arr1)

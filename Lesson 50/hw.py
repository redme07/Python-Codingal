n = int(input("Enter size: "))
arr = list(map(int, input("Enter elements: ").split()))

rot1 = arr[1:] + arr[:1]
rot2 = arr[2:] + arr[:2]

print("Rotate by 1:", rot1)
print("Rotate by 2:", rot2)
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
# Initialize an empty list to store the numbers
result = []
# Loop through numbers from start to end (inclusive)
for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 != 0:
        result.append(str(num))
print(','.join(result))
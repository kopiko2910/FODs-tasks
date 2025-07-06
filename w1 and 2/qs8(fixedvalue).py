result = []
# Loop through numbers from 2000 to 3200 (inclusive)
for num in range(2000, 3201):
    # Check if divisible by 7 and not divisible by 5
    if num % 7 == 0 and num % 5 != 0:
        result.append(str(num))
print(','.join(result))
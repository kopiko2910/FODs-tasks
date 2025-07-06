#this program prints all the prime numbers between the given two numbers and their sum
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
primes = []
total = 0
for num in range(start, end + 1):
    if num > 1: 
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            total += num
print("\nPrime numbers between", start, "and", end, "are:")
print(*primes)  # Print all primes separated by space
print("Sum of all prime numbers:", total)

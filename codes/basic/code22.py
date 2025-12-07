def PrimeCheck(n):
    if n <= 1:
        print(f"{n} is not a Prime Number")
        return

    isPrime = True

    # Check divisors up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            isPrime = False
            break

    if isPrime:
        print(f"{n} is a Prime Number!!!")
    else:
        print(f"{n} is not a Prime Number")

n = int(input("Enter a number: "))
PrimeCheck(n)

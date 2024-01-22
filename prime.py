def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return "not prime"
            break
    return "is prime"
n = int(input("Enter the number"))
r = prime(n)
print(r)
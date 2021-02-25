def prime_checker(number):
    is_prime = True
    for num in range(2, number-1):
        if number % num == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
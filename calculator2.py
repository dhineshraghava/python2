def check_prime(num):
    is_prime = False
    for i in range(num):
        if num%i == 0:
            return True
        else:
            return False

print(check_prime(99))
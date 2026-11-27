from math import isqrt
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập số: "))
print("Số nguyên tố" if is_prime(n) else "Không phải số nguyên tố")

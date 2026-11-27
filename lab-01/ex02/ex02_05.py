hours = float(input("Số giờ làm: "))
rate = float(input("Lương theo giờ: "))
salary = min(hours, 44) * rate + max(hours - 44, 0) * rate * 1.5
print("Tiền lương:", salary)

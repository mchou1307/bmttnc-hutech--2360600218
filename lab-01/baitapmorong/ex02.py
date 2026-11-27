import re
s = input("Nhập chuỗi: ")
numbers = [int(x) for x in re.findall(r"[+-]?[0-9]+", s)]
print("Giá trị dương:", sum(n for n in numbers if n > 0))
print("Giá trị âm:", sum(n for n in numbers if n < 0))

values = input("Nhập các số nhị phân 4 bit: ").split(",")
values = [v.strip() for v in values]
print(",".join(v for v in values if len(v) == 4 and set(v) <= {"0", "1"} and int(v, 2) % 5 == 0))

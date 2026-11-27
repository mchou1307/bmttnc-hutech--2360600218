a = list(map(int, input("Nhập danh sách số: ").split()))
print(sum(x for x in a if x % 2 == 0))

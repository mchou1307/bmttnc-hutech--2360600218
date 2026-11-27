a = input("Nhập danh sách: ").split()
counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1
print(counts)

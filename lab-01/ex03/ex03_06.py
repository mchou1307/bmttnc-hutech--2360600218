d = {"a": 1, "b": 2, "c": 3}
print(d)
key = input("Nhập key cần xóa: ")
if key in d:
    del d[key]
else:
    print("Không tìm thấy key")
print(d)

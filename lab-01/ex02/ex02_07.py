lines = []
while True:
    s = input("Nhập dòng (Enter để kết thúc): ")
    if not s:
        break
    lines.append(s.upper())
for line in lines:
    print(line)

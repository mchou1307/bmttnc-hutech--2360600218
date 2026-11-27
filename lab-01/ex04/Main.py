from QuanLySinhVien import QuanLySinhVien

def nhap_thong_tin():
    ten = input("Tên: ")
    gt = input("Giới tính: ")
    cn = input("Chuyên ngành: ")
    while True:
        try:
            diem = float(input("Điểm trung bình (0-10): "))
            if 0 <= diem <= 10:
                return ten, gt, cn, diem
        except ValueError:
            pass
        print("Điểm không hợp lệ")

def main():
    ql = QuanLySinhVien()
    while True:
        print("\n1. Thêm\n2. Cập nhật\n3. Xóa\n4. Tìm theo tên\n5. Sắp xếp theo điểm\n6. Sắp xếp theo chuyên ngành\n7. Hiển thị\n0. Thoát")
        choice = input("Chọn: ")
        try:
            if choice == "1":
                ql.them(*nhap_thong_tin())
            elif choice == "2":
                id = int(input("ID: "))
                if ql.tim_id(id):
                    ql.cap_nhat(id, *nhap_thong_tin())
                else:
                    print("Không tìm thấy sinh viên")
            elif choice == "3":
                print("Đã xóa" if ql.xoa(int(input("ID: "))) else "Không tìm thấy sinh viên")
            elif choice == "4":
                ql.hien_thi(ql.tim_ten(input("Tên cần tìm: ")))
            elif choice == "5":
                ql.sap_xep_diem()
                ql.hien_thi()
            elif choice == "6":
                ql.sap_xep_chuyen_nganh()
                ql.hien_thi()
            elif choice == "7":
                ql.hien_thi()
            elif choice == "0":
                break
            else:
                print("Lựa chọn không hợp lệ")
        except ValueError:
            print("Dữ liệu không hợp lệ")

if __name__ == "__main__":
    main()


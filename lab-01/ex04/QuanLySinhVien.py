from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.ds = []

    def them(self, ten, gioi_tinh, chuyen_nganh, diem_tb):
        self.ds.append(SinhVien(ten, gioi_tinh, chuyen_nganh, diem_tb))

    def tim_id(self, id):
        return next((sv for sv in self.ds if sv.id == id), None)

    def cap_nhat(self, id, ten, gioi_tinh, chuyen_nganh, diem_tb):
        sv = self.tim_id(id)
        if sv is None:
            return False
        sv.ten = ten
        sv.gioi_tinh = gioi_tinh
        sv.chuyen_nganh = chuyen_nganh
        sv.diem_tb = diem_tb
        return True

    def xoa(self, id):
        sv = self.tim_id(id)
        if sv is None:
            return False
        self.ds.remove(sv)
        return True

    def tim_ten(self, ten):
        return [sv for sv in self.ds if ten.casefold() in sv.ten.casefold()]

    def sap_xep_diem(self):
        self.ds.sort(key=lambda sv: sv.diem_tb, reverse=True)

    def sap_xep_chuyen_nganh(self):
        self.ds.sort(key=lambda sv: sv.chuyen_nganh.casefold())

    def hien_thi(self, ds=None):
        ds = self.ds if ds is None else ds
        if not ds:
            print("Danh sách rỗng")
        for sv in ds:
            print(sv)


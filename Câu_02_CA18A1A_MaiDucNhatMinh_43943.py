"""
Author: Mai Duc Nhat Minh
Date: 29/10/2021

    ....
"""


def Cau2():
    data = []
    n = 0

    class MaHang:
        def __init__(self, Ma, Ten, SoLuong, DonGia) -> None:
            self.Ma_Mat_Hang = Ma
            self.Ten_Mat_Hang = Ten
            self.So_Luong = SoLuong
            self.Don_Gia = DonGia

        @property
        def ThanhTien(self):
            return self.So_Luong * self.Don_Gia

    def cv23():
        f = open("Câu_2.3_CA18A1A_MaiDucNhatMinh_43943_inp_txt", mode="r", encoding="utf-8")
        n = int(f.readline())
        for i in range(n):
            row_data = f .readline().split("|")
            mat_hang = MaHang(row_data[0], row_data[1], int(row_data[2]),int(row_data[3]))
            data.append(mat_hang)
        f.close()
        print("=="*10)
        print("=> Hoan thanh nhap du lieu tu file: Câu_2.3_CA18A1A_MaiDucNhatMinh_43943_inp_txt")

    def cv24():
        print("=="*20)
        if len(data) == 0:
            print("Ban can nhap thong tin ve mat hang")
        else:
            print("\nIn thong tin cac mat hang:\n")
            for i in data:
                print("{:<5} {:<15} {:>5} {:>10} {:>10}"
                      .format(i.Ma_Mat_Hang, i.Ten_Mat_Hang, i.So_Luong, i.Don_Gia, i.Thanh_Tien))
        print("==" * 20)

    def cv25():
        """Hien thi mat hang co don gia cao nhat"""
        print("=Mat Hang Dat Nhat=")
        MatHangDatNhat = data[0]
        for i in data:
            if i.Don_Gia > MatHangDatNhat.Don_Gia:
                MatHangDatNhat = i
        MatHangDatNhat_str = MatHangDatNhat.Ma_Mat_Hang + "|" + MatHangDatNhat.Ten_Mat_Hang + "|" +\
                             str(MatHangDatNhat.So_Luong) + "|" + str(MatHangDatNhat.Don_Gia) + "|" +\
                             str(MatHangDatNhat.Thanh_Tien) + "\n"
        print(MatHangDatNhat_str)
        print("==" * 20)

    def cv26():
        if len(data) == 0:
            print("Ban can nhap thong tin ve mat hang")
        else:
            f = open("Câu_2.6_CA18A1A_MaiDucNhatMinh_43943_out_txt", mode="w", encoding="utf-8")
            f.write(str(len(data)) + "\n")
            for i in data:
                s = i.Ma_Mat_Hang + "|" + i.Ten_Mat_Hang + "|" + str(i.So_Luong) \
                    + "|" + str(i.Don_Gia) + "|" + str(i.Thanh_Tien) + "\n"
                f.write(s)
            f.close()
        print("Hoan thanh ghi ra file:Câu_2.6_CA18A1A_MaiDucNhatMinh_43943_out_txt")
        print("++"*20)

    while True:
        print(" Menu ")
        print("1. Nhap du lieu")
        print("2. In du lieu")
        print("3. In mat hang voi DonGia lon nhat")
        print("4. Ghi thong tin")
        cv = input("Ban chon cong viec, Bam K de thoat: ")
        if cv == "1":
            cv23()
        elif cv == "2":
            cv24()
        elif cv == "3":
            cv25()
        elif cv == "4":
            cv26()
        elif cv.upper() == "K":
            break


if __name__ == '__main__':
    Cau2()
name_patient = input("Nhập tên bệnh nhân:")
age_patient = int(input("Nhập tuổi bệnh nhân:"))


if age_patient > 150:
    print("Tuổi không hợp lệ!!")
elif age_patient >= 80:
    print("ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa.")
elif age_patient >= 6:
    print("KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.")
elif age_patient > 0:
    print("ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi.")
else:
    print("Tuổi không hợp lệ!!")
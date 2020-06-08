list_sv = {
      "A1": {"masv":"2017603001","name":"Hoàng Xuân Thái","lop":"CNTT3","khoa":"12","vt":'A1',"check":"0"},
      "A2": {"masv":"2017603002","name":"Trần Văn Sơn","lop":"CNTT3","khoa":"12","vt":'A2',"check":"0"},
      "A3": {"masv":"2017603003","name":"Đoàn Phùng Tú","lop":"CNTT3","khoa":"12","vt":'A3',"check":"0"},
      "A4": {"masv":"2017603004","name":"Trịnh Văn Quyền","lop":"CNTT3","khoa":"12","vt":'A4',"check":"0"},
      "A5": {"masv":"2017603005","name":"Nguyễn Duy Nghĩa","lop":"CNTT3","khoa":"12","vt":'A5',"check":"0"},
      "A6": {"masv":"2017603006","name":"Tạ Quang Trường","lop":"CNTT3","khoa":"12","vt":'A6',"check":"0"},
      "A7": {"masv":"2017603007","name":"Nguyễn Thanh Tùng","lop":"CNTT3","khoa":"12","vt":'A7',"check":"0"},
      "A8": {"masv":"2017603008","name":"Hoàng Thị Bích Ngọc","lop":"CNTT3","khoa":"12","vt":'A8',"check":"0"},
      "A9": {"masv":"2017603009","name":"Nguyễn Đưc Linh","lop":"CNTT3","khoa":"12","vt":'A9',"check":"0"},
      "A10": {"masv":"2017603010","name":"Lưu Quang Nghĩa","lop":"CNTT3","khoa":"12","vt":'A10',"check":"0"},
      "B1": {"masv":"2017603011","name":"Phan Thành Trung","lop":"CNTT3","khoa":"12","vt":'B1',"check":"0"},
      "B2": {"masv":"2017603012","name":"Nguyễn Trung Hải","lop":"CNTT3","khoa":"12","vt":'B2',"check":"0"},
      "B3": {"masv":"2017603013","name":"Phạm Thị Hải Yến","lop":"CNTT3","khoa":"12","vt":'B3',"check":"0"},
      "B4": {"masv":"2017603014","name":"Phạm Linh Linh","lop":"CNTT3","khoa":"12","vt":'B4',"check":"0"},
      "B5": {"masv":"2017603015","name":"Nguyễn Anh Tú","lop":"CNTT3","khoa":"12","vt":'B5',"check":"0"},
      "B6": {"masv":"2017603016","name":"Nguyễn Công Đông","lop":"CNTT3","khoa":"12","vt":'B6',"check":"0"},
      "B7": {"masv":"2017603017","name":"Hoàng Thu Trang","lop":"CNTT3","khoa":"12","vt":'B7',"check":"0"},
      "B8": {"masv":"2017603018","name":"Trần Hồng Phi","lop":"CNTT3","khoa":"12","vt":'B8',"check":"0"},
      "B9": {"masv":"2017603019","name":"Đào Thu Hoài","lop":"CNTT3","khoa":"12","vt":'B9',"check":"0"},
      "B10": {"masv":"2017603020","name":"Nguyễn Quốc Tuấn","lop":"CNTT3","khoa":"12","vt":'B10',"check":"0"},
      "C1": {"masv":"2017603021","name":"Đinh Trọng Luân","lop":"CNTT3","khoa":"12","vt":'C1',"check":"0"},
      "C2": {"masv":"2017603022","name":"Vũ Thị Nghĩa","lop":"CNTT3","khoa":"12","vt":'C2',"check":"0"},
      "C3": {"masv":"2017603023","name":"Hoàng Duy Mạnh","lop":"CNTT3","khoa":"12","vt":'C3',"check":"0"},
      "C4": {"masv":"2017603024","name":"Phạm Hồng Thái","lop":"CNTT3","khoa":"12","vt":'C4',"check":"0"},
      "C5": {"masv":"2017603025","name":"Nguyễn Thùy Lnh","lop":"CNTT3","khoa":"12","vt":'C5',"check":"0"},
      "C6": {"masv":"2017603026","name":"Phan Tuấn Minh","lop":"CNTT3","khoa":"12","vt":'C6',"check":"0"},
      "C7": {"masv":"2017603027","name":"Nguyễn Thị Thủy","lop":"CNTT3","khoa":"12","vt":'C7',"check":"0"},
      "C8": {"masv":"2017603028","name":"Khổng Thị Nhung","lop":"CNTT3","khoa":"12","vt":'C8',"check":"0"},
      "C9": {"masv":"2017603029","name":"Bùi Tất Trung","lop":"CNTT3","khoa":"12","vt":'C9',"check":"0"},
      "C10": {"masv":"2017603030","name":"Lê Văn Nam","lop":"CNTT3","khoa":"12","vt":'C10',"check":"0"}
}
def getlistsv():
    l = []
    for values in list_sv.values():
      l.append(values)
    return l
def getlistsv_train():
    return list_sv
def setlistsv(data={}):
    list_sv = data

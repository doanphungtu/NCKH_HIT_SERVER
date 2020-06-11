list_sv = {
      "A1": {"masv":"2017603001","name":"Hoang Xuan Thai","lop":"CNTT3","khoa":"12","vt":'A1',"check":"0"},
      "A2": {"masv":"2017603002","name":"Tran Van Son","lop":"CNTT3","khoa":"12","vt":'A2',"check":"0"},
      "A3": {"masv":"2017603003","name":"Doan Phung Tu","lop":"CNTT3","khoa":"12","vt":'A3',"check":"0"},
      "A4": {"masv":"2017603004","name":"Trinh Van Quyen","lop":"CNTT3","khoa":"12","vt":'A4',"check":"0"},
      "A5": {"masv":"2017603005","name":"Nguyen Duy Nghia","lop":"CNTT3","khoa":"12","vt":'A5',"check":"0"},
      "A6": {"masv":"2017603006","name":"Ta Quang Truong","lop":"CNTT3","khoa":"12","vt":'A6',"check":"0"},
      "A7": {"masv":"2017603007","name":"Nguyen Thanh Tung","lop":"CNTT3","khoa":"12","vt":'A7',"check":"0"},
      "A8": {"masv":"2017603008","name":"Hoang Thi Bich Ngoc","lop":"CNTT3","khoa":"12","vt":'A8',"check":"0"},
      "A9": {"masv":"2017603009","name":"Nguyen Đuc Linh","lop":"CNTT3","khoa":"12","vt":'A9',"check":"0"},
      "A10": {"masv":"2017603010","name":"Luu Quang Nghia","lop":"CNTT3","khoa":"12","vt":'A10',"check":"0"},
      "B1": {"masv":"2017603011","name":"Phan Thanh Trung","lop":"CNTT3","khoa":"12","vt":'B1',"check":"0"},
      "B2": {"masv":"2017603012","name":"Nguyen Trung Hai","lop":"CNTT3","khoa":"12","vt":'B2',"check":"0"},
      "B3": {"masv":"2017603013","name":"Pham Thi Hai Yen","lop":"CNTT3","khoa":"12","vt":'B3',"check":"0"},
      "B4": {"masv":"2017603014","name":"Pham Linh Linh","lop":"CNTT3","khoa":"12","vt":'B4',"check":"0"},
      "B5": {"masv":"2017603015","name":"Nguyen Anh Tu","lop":"CNTT3","khoa":"12","vt":'B5',"check":"0"},
      "B6": {"masv":"2017603016","name":"Nguyen Thanh Tung","lop":"CNTT3","khoa":"12","vt":'B6',"check":"0"},
      "B7": {"masv":"2017603017","name":"Hoang Thu Trang","lop":"CNTT3","khoa":"12","vt":'B7',"check":"0"},
      "B8": {"masv":"2017603018","name":"Tran Hong Phi","lop":"CNTT3","khoa":"12","vt":'B8',"check":"0"},
      "B9": {"masv":"2017603019","name":"Đao Thu Hoai","lop":"CNTT3","khoa":"12","vt":'B9',"check":"0"},
      "B10": {"masv":"2017603020","name":"Nguyen Quoc Tuan","lop":"CNTT3","khoa":"12","vt":'B10',"check":"0"},
      "C1": {"masv":"2017603021","name":"Dinh Trong Luan","lop":"CNTT3","khoa":"12","vt":'C1',"check":"0"},
      "C2": {"masv":"2017603022","name":"Vu Thi Nghia","lop":"CNTT3","khoa":"12","vt":'C2',"check":"0"},
      "C3": {"masv":"2017603023","name":"Hoang Duy Manh","lop":"CNTT3","khoa":"12","vt":'C3',"check":"0"},
      "C4": {"masv":"2017603024","name":"Pham Hong Thai","lop":"CNTT3","khoa":"12","vt":'C4',"check":"0"},
      "C5": {"masv":"2017603025","name":"Nguyen Thuy Linh","lop":"CNTT3","khoa":"12","vt":'C5',"check":"0"},
      "C6": {"masv":"2017603026","name":"Phan Tuan Minh","lop":"CNTT3","khoa":"12","vt":'C6',"check":"0"},
      "C7": {"masv":"2017603027","name":"Nguyen Thi Thuy","lop":"CNTT3","khoa":"12","vt":'C7',"check":"0"},
      "C8": {"masv":"2017603028","name":"Khong Thi Nhung","lop":"CNTT3","khoa":"12","vt":'C8',"check":"0"},
      "C9": {"masv":"2017603029","name":"Bui Tat Trung","lop":"CNTT3","khoa":"12","vt":'C9',"check":"0"},
      "C10": {"masv":"2017603030","name":"Le Van Nam","lop":"CNTT3","khoa":"12","vt":'C10',"check":"0"}
}
encoding = []
name =[]
def getlistsv():
    l = []
    for values in list_sv.values():
      l.append(values)
    return l
def getlistsv_train():
    return list_sv
def setlistsv(data={}):
    list_sv = data

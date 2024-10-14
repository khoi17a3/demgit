import json
du_lieu = {"Ten":"nam", "Tuoi":19, "Nganh":"Khoa hoc du lieu", "Truong Dai Hoc":"UNETI"}

chuoi_json= json.dumps(du_lieu, ensure_ascii= False, incent=4, sort_keys=True)
print(chuoi_json)

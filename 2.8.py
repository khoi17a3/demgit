import json
doi_tuong_python = {"ten":"Nam", "Tuoi":19 ,"Truong_dai_hoc":"UNETI"}

chuoi_json= json.dumps(doi_tuong_python,ensure_ascii=False)
print(chuoi_json)

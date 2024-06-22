from datetime import datetime
ngay1 = "1:1:20"
ngay2 = "2:2:10"

ngay_1 = datetime.strptime(ngay1, "%H:%M:%S")
ngay_2 = datetime.strptime(ngay2, "%H:%M:%S")
n = str(ngay_2-ngay_1)
print(n)

n = n.split(":")
print(n)
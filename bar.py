import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft JhengHei")
"""
    X軸為數字
        x=[3,4,1]
        height=[8,5,2]
"""
# plt.bar([3,4,1],[8,5,2])
# plt.show()
"""
    X軸為字串，調整寬度和顏色，加上標示
        x=["B","A","C"]
        height=[8,10,16]
"""
# plt.bar(["B","A","C"],[8,10,16],width=0.5,color="red")
# plt.xlabel("X標題")
# plt.ylabel("Y標題")
# plt.show()

# 從 CSV 格式的檔案載入資料，並繪製長條圖
import csv
file=open("bar-data.csv",encoding="utf-8")
reader=csv.reader(file)
header=next(reader)

x=[]    
height=[]
for row in reader:
    x.append(row[0])
    height.append(int(row[1]))
print(x)
print(height)
plt.bar(x,height,width=0.6,color="black")
plt.xlabel(header[0])
plt.ylabel(header[1])
plt.show()
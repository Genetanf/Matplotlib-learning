import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft JhengHei")

"""
    一組資料點
    (1,2), (2,4), (3,6)
"""

# plt.plot([1,2,3],[2,4,6])
# plt.show()

"""
    兩組資料點
        第一組 (1,2), (2,4), (3,6)
        第二組 (1,1), (2,2), (3,3)
"""

# plt.plot([1,2,3],[[2,1],[4,2],[6,3]], label=["第一組標籤","第二組標籤"])
# plt.legend()    # 產生圖例
# plt.xlabel("X軸文字說明")
# plt.ylabel("Y軸文字說明")
# plt.show()

# 從 CSV 格式的檔案載入資料，並繪製成折線圖
import csv
file=open("data.csv",encoding="utf-8")
reader=csv.reader(file)

header=next(reader) # 讀取第一列
print("標頭",header)

x=[]    # [2010,2011,2012]
y=[]    # [[40000,300000,[42000,60000],[45000,50000]]
for row in reader:
    # print("每列的資料",row)
    x.append(int(row[0]))
    y.append([int(row[1]),int(row[2])])
plt.plot(x,y,label=header[1:3])
plt.plot(x,y)
plt.xlabel(header[0])
plt.ylabel("薪資")
plt.show()

import matplotlib.pyplot as plt
# 設定字型為微軟正黑體
# plt.rc("font",family="Microsoft JhengHei")
# # 繪製一個資料點的圓餅圖，加上適當的百分比標示
# x=[10,15,25]
# total=sum(x)    # 計算列表中數值的總和 sum(列表)
# # labels=[str(100*data/total)+"%" for data in x]
# plt.pie(
#     x,
#     labels=[str(100*x[0]/total)+"%",str(100*x[1]/total)+"%",str(100*x[2]/total)+"%"],
#     labeldistance=0.5
# )
# plt.legend()
# plt.show()

# 載入 CSV 檔案格式的資料，繪製適當的圓餅圖加標示
import csv
file=open("pieChart-data.csv",encoding="utf-8")
reader=csv.reader(file)
next(reader)    # 讀取第一列

x=[]
labels=[]

for row in reader:
    labels.append(row[0]),
    x.append(row[1])
plt.pie(x,labels=labels,labeldistance=0.5)
plt.legend()
plt.title("瀏覽器市場占有率分布")
plt.show()
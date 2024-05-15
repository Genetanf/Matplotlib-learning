import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft JhengHei")

"""
    範例資料:
        日期    價格
        11/01   開盤 95, 收盤 80, 最高 100, 最低 75
        11/02   開盤 82, 收盤 75, 最高 83, 最低 65
        11/03   開盤 73, 收盤 85, 最高 90, 最低 70
"""

# 根據範例資料畫出基本的 K 線圖
# plt.bar("11/01",15,bottom=80,color="green",width=0.5)
# plt.bar("11/01",25,bottom=75,color="green",width=0.1)
# plt.bar("11/02",7,bottom=75,color="green",width=0.5)
# plt.bar("11/02",18,bottom=65,color="green",width=0.1)
# plt.bar("11/03",12,bottom=90,color="red",width=0.5)
# plt.bar("11/03",20,bottom=70,color="red",width=0.1)
# plt.show()

# 從 CSV 格式的檔案載入資料，並繪製 K 線圖
import csv
file=open("Kbar-data.csv",encoding="utf-8")
reader=csv.reader(file)
header=next(reader)
for row in reader:
    date=row[0]
    open_price=int(row[1])
    close_price=int(row[2])
    highest=int(row[3])
    lowest=int(row[4])
    # 決定陰線(下跌)或陽線(上漲)
    color="green"
    if close_price>open_price:
        color="red"
    
    plt.bar(date,abs(open_price-close_price),
            bottom=min(open_price,close_price),
            color=color,
            width=0.5)
    plt.bar(date,highest-lowest,
            bottom=lowest,
            color=color,
            width=0.1)
plt.xlabel("日期")
plt.ylabel("價格")
plt.title("個股價格走勢")
plt.show()





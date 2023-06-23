arr = [100000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.15, 0.03, 0.05, 0.075, 0.1]
i = int(input("请输入当月理论工资(元)："))
thisarr = 0
for j in range(len(arr)):
    if i > arr[j]:
        thisarr += (i - arr[j]*rat[j])
        i = arr[j]
print("应发放奖金总数(元)：%d"%thisarr)
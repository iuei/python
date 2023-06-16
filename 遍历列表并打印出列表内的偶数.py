list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
a = 0  # 定义初始值
# 设置循环条件：遍历的次数不能大于列表元素数量
while a < len(list1):
    if list1[a] % 2 == 0:
        list2.append(list1[a])
    a += 1

print(list2)





list1 = ['name', 'age', 'id']

a = 0  # 定义初始值
b = 1
# 设置循环条件：遍历的次数不能大于列表元素数量
while a < len(list1):

    # 通过list2取出对应的元素
    list2 = list1[a]
    print(f"列表{b}元素：{list2}")
    b += 1  # 充当计数器
    a += 1  # 每一次循环加1

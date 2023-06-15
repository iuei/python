# 定义一个列表
a_list = [21, 25, 21, 23, 22, 20]
# 追加数据
b_list = (31)
a_list.append(b_list)
print(f"追加数据后的列表：{a_list}")

# 追加新列表到尾部
c_list = [29, 33, 30]
a_list.extend(c_list)
print(f"追加新列表后的列表：{a_list}")

# 取出第一个元素
del a_list[0]
print(f'取出元素后的列表：{a_list}')

# 取出最后一个元素
del a_list[-1]
print(f'取出元素后的列表：{a_list}')

# 查找元素31，在下标中的位置
mylist = a_list.index(31)
print(f'元素31在列表中的下标为：{mylist}')
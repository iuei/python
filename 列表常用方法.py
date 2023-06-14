# 定义一个名为a_list的列表
a_list = ['name', 'age', 'id']

# 查找元素下标 语法：列表.index(元素)
mylist = a_list.index('name')
print(f"id的元素下标是：{mylist}")

# 修改特定位置的元素值 语法：列表[下标]=值
a_list[0] = '姓名'
print(f'name元素修改后：{a_list}')

# 插入元素 语法：列表.insert(下标, 元素); 在指定的下标位置，插入指定的元素
a_list.insert(1, 'hello')
print(f'插入元素后的列表内容为：{a_list}')

# 追加元素 语法：列表.append(元素); 将指定元素，追加到列表尾部
a_list.append('word')
print(f'追加后的列表内容为：{a_list}')

# 追加一批新元素 语法：列表.extend其他列表); 将其他数据列表的内容取出，依次追加到尾部
ba_list = [1, 2, 3]
a_list.extend(ba_list)
print(f'追加一批新元素后列表为：{a_list}')

# 删除元素 语法1：del 列表[下标] 语法2：列表.pop(下标)
del a_list[-1]
print(f'通过del关键字删除元素后的列表内容为：{a_list}')

a_list.pop(-1)
print(f'通过pop方法删除元素后的列表内容为：{a_list}')

# 删除某个元素在列表的第一个匹配项 语法：列表.remove
bb_list = [1, 1, 2, 2, 3, 3]
bb_list.remove(1)
print(f'删除列表的第一个匹配项后：{bb_list}')

# 清空列表 语法：列表.clear()
bb_list = [1, 1, 2, 2, 3, 3]
bb_list.clear()
print(f'清空列表：{bb_list}')

# 统计某一个元素在列表中的数量 语法：列表.count(元素)
bb_list = [1, 1, 2, 2, 3, 3]
bb_list = bb_list.count(1)
print(f'统计元素1的数量为：{bb_list}')

# 统计列表的全部元素 语法：len(列表)
bb_list = [1, 1, 2, 2, 3, 3]
bb_list = len(bb_list)
print(f'列表的全部元素：{bb_list}')

num1 = ('小白', 21, ['football', 'music'])
# 查询年龄所在的下标位置
age = num1.index(21, )
print(f'年龄所在的下标位置是：{age}')
# 查询学生姓名
name = num1[0]
print(f'学生的姓名是：{name}')

# 删除学生爱好中的football
num1_list = list(num1[2])   # 元组不能修改内容，所以先把要修改的内容转换为列表
num1_list.remove('football')    # 使用关键字remove删除内容
num1 = (num1[0], num1[1], num1_list)    # 转换回元组
print(f'删除football后的元组为：{num1}')

# 增加 "coding" 到列表中
num1_list.append("coding")
num1 = (num1[0], num1[1], num1_list)
print(f"添加coding后的元组为：{num1}")

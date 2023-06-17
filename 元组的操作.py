# 定义元组 如果只定义一个元素那么后面需要加上逗号：a1(1,); 元组内容不可修改(元组里面的list可以修改)元组定义要用：()
a1 = (1, 2, 3, 4, 5)

# 查找元组下标
index = a1.index(1,)
print(f"你查找的下标元素是：{index}")

a2 = ('age', 'name', 'age', 'age', 'id' )
# 统计元素一共有多少个
count = a2.count('age',)
print(f'你要统计的元素一共有{count}个')

a3 = (1, 2, 3, 4, 5, 'age', 'name', 'age', 'age', 'id')
# 统计元素总数量
len = len(a3)
print(f'该元组一共有{len}个元素')
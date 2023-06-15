list1 = ['name', 'age', 'id']

# 使用for循环将list1的值依次遍历到临时变量a
b = 0  # 定义临时变量b充当计数器每次循环+1
for a in list1:
    b += 1
    print(f"遍历第{b}个元素：{a}")

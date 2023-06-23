count = 0
print("1, 2, 3, 4可以组成的无重复三位数有：")
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if(x != y) and (x != z) and (y != z):
                print(x, y, z)
                count += 1
print("一共%d个数字。"%count)

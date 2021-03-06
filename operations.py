print(10 ** 3)  # 幂运算 1000
print(100 / 3)  # 精确除 33.3333
# 地板除  一正一负向下取整
print(100 // 3)  # 33
print(100 // -3)  # -34
print(-100 // 3)  # -34
# 取余数 = 被除数 - 除数 * 商
print(100 % 3)  # 1
print(100 % -3)  # -2 = 100 - (-3) * (-34)
print(-100 % 3)  # 2 = -100 - 3 * (-34)
print(100 % 7)
print(-100 % 7)  # -100-7*(-15)

a, b, c = 1, 2, 3
x = y = z = 10
print(a, b, c, x, y, z)

# 交换
a, b, c = c, b, a
print(a, b, c)

# ==, is, is not
print('a < b?', a < b)
print('a is b?', a is b)

a = True
string = 'Yingyao Lu'
list1 = [1, 2, 3]
list2 = [0, 5, 6, 7]

# and, or, not, in, not in
print('Lu' in string)  # T
print('y' not in string)  # F
print(a in list1)  # T
print((not 1) in list2)  # T
print((not a) in list2)  # T
print((not a) not in list1)  # T
print(a not in list2)  # T
print(not a)  # F

# 位运算 Bitwise operation & | >> <<
print(4 & 8)  # 0100 1000 -> 0000
print(4 | 8)  # 0100 1000 -> 1100
print(4 << 1)  # 0100 -> 1000 = 8 相当于 *2
print(4 >> 2)  # 0100 -> 0001 = 1 相当于 /4
print(4 >> 3)  # 0100 -> 0000 = 0



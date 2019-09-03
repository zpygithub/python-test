#!/usr/bin/env python
# coding:utf-8
# Time   2019/9/2 11:15
# Author zpy

# 除
print(10 / 3)
# 整除
print(10 // 3)
# 取余
print(10 % 3)
# 指数
print(4 ** 2)

# 多个变量赋不同值
num, str, float = 1, "q", 2.2
print(num, str, float)
# 多个变量赋相同值
a = b = 10
print(a, b)

# 复合赋值运算符 +=，-=，*=，/=，//=，%=，**=
a = 3
b = 2
c = 1
a **= b + 1
print(a)

# 比较运算符 ==，!=，<，>，<=，>=
a = "10"
b = 10
print(a == b)

# 数字的逻辑运算
# and 有一个为0，结果为0，否则结果为最后一个非0数字
a = 0
b = 1
c = 2
print(a and b)
print(c and b)
# or 所有值为0，结果为0，否则结果为第一个非0数字
print(a and b)
print(c and b)
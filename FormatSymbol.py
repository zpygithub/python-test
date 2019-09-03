#!/usr/bin/env python
# coding:utf-8
# Time   2019/9/2 10:55
# Author zpy

name = "haha"
age = 18
height = 1.7
num = 13

print("名字%s，明年%d岁，身高%.2f，号码%03d。" % (name, age + 1, height, num))
print("名字%s，明年%s岁，身高%s，号码%s。" % (name, age + 1, height, num))

# f'' since3.6
print(f'名字{name}，明年{age + 1}岁，身高{height}，号码{num}。')
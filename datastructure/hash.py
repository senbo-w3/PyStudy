#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# hash table 是一种数据集， 数据项的存储方式尤其利于将于快速查找定位
# 散列表中的每一个存储位置，称为槽 slot
# 实现数据项到存储槽名称的转换称为 "hash func"
# 常用的三列方法"求余数"，将数据项除以散列表的大小，得到的余数作为槽号
# h(items) = item % len(items)
# 负载因子 槽被数据项占据的比列
# 问题： 冲突!

# 完美散列函数
# 如果一个散列函数可以将每个数据项映射到不同的槽中，那么这个散列函数就被称为完美散列函数
# 1. 扩大散列表的容量， 难以实现，退而求其次：
# *2. 冲突最少，计算难度低，充分分散数据项

# 指纹函数：
# 1. 压缩性
# 2. 易计算性
# 3. 抗修改性
# 4. 抗冲突性

# eg.
# MD5, SHA系列函数
# Message Digest -> 128位， 16字节的摘要
# SHA-0/SHA-1 ->160位(20字节)，
# SHA-256/SHA-224
# SHA-512/SHA-384
import hashlib
md5 = hashlib.md5("hello world!".encode('utf-8')).hexdigest()
print(md5)
# 文件完整性校验
# 文件分享系统
# 加密形式保存密码
# 防止文件篡改
# 彩票投注应用

# 区块链， 分布式数据库
# 通过网络链接的节点， 每个节点都保存着整个数据库的所有数据，任何地点存入的数据都会完成同步
# 特征：
# 去中心化
# 散列函数设计

# 折叠法
# 将数据项按照位数分为若干段
# 再讲几段数字相加
# （隔数反转）
# 对散列表大小求余，得到散列值

# 平方取中法
# 平方取中间数再求余

# 冲突解决方案
# 再找一个开放的空槽来保存（开放地址，open addressing）
# 线性探测 linear probing.
# 查找没有时便向后顺序查找
# 缺点： 聚集趋势 （clustering）
# 冲突项越多则越影响其他数据的插入
# -> 跳跃式探测，改变+1 为+n
# -> 再散列 rehashing
# 二次探测 quadratic probing
# 数据项链 Chaining
# -> 将单个数据项的槽拓展为容纳数据项的集合

if __name__ == "__main__":
    pass
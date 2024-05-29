"""
    while 条件1：
        条件1满足时，做的事情1
        条件1满足时，做的事情2
        条件1满足时，做的事情3
        while 条件2：
            条件2满足时，做的事情1
            条件2满足时，做的事情2
            条件2满足时，做的事情3
    1.注意空格缩进：python基于空格缩进决定层次关系
    2.注意条件：避免出现无限循环
"""
# 外层循环：控制的是天数
i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白... ...")
    # 内嵌循环：控制送出玫瑰花数量
    j = 1
    while j <= 10:
        print(f"送给小妹第{j}支玫瑰花")
        j += 1
    print("小美，喜欢你")
    i += 1
print(f"坚持到第{i-1}天，表白成功")

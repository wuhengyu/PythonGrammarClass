# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 20:45
# @Author  : Walter
# @File    : 面向对象.py
# @License : (C)Copyright Walter
# @Desc    :
# 面向对象
# 对象就是'容器'，是用来存放数据和功能，数据和功能的集合体

# 英雄的容器
# 英雄的数据
def set_hero_speed(speed_plus):
    hero_name = '鲁班七号'
    hero_speed = 800
    hero_hp = 3000
    hero_atk = 100
    # 英雄的功能
    print(f'英雄属性：名字：{hero_name}')

# 玩家的容器
# 玩家的数据
user_name = '张大仙'
# 玩家的功能
print(f'英雄属性：名字：{user_name}')


# 使用list、tuple、dict作为容器
# 英雄对象
hero_obj = {
    'hero_name': '鲁班七号',
    'hero_speed': 450,
    'set_hero_speed': set_hero_speed
}

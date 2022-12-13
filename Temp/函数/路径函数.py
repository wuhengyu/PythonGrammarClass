# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 14:51
# @Author  : Walter
# @File    : 路径函数.py
# @License : (C)Copyright Walter
# @Desc    :
import os.path
from pathlib import Path

# 打印当前文件路径
print(Path(__file__))

# 打印项目路径
BASE_DIR = Path(__file__).parent.parent
print(BASE_DIR)

# 打印项目路径
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

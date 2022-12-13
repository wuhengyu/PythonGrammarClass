# str.find(sub[,start[,end]])
# 此格式中各参数的含义如下：
# str：表示原字符串；
# sub：表示要检索的目标字符串；
# start：表示开始检索的起始位置。如果不指定，则默认从头开始检索；
# end：表示结束检索的结束位置。如果不指定，则默认一直检索到结尾。
# 首次出现 “.” 的位置索引
str = "www.baidu.com"
print(str.find('.'))
print(str.find('.', 4))
print(str.find('.', 4, -4))  # 其不包含“.”，因此 find() 方法的返回值为 -1

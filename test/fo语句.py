""""
fruits =['banana','apple','mango']
for fruit in fruits:
    print(fruit)
"""
#range()函数默认从零开始循环，我们也可以为其设置起始位置和步长 。 例如，打印 1到 10 之间的奇数；
for i in range(1,50,2):
    print(i)
"""
数组用方括号（ ［］ ）表示 ， 里面的每一项用 逗号（， ） 隔开 。
python 允许在数组里面任 意地放置数字或字符串 。需要注意 的 是 ， 数组下标是从 0 开
始 的， 所以， lists[O]会输出数组中 的第一项。 append()函数可 以 向 数组末尾追加新 的 项。
"""
lists = [1,2,3,4,5,6,]
lists.append('c')
print (lists[6])
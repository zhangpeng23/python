print("Hello python") #打印aa
"""
虽然两次打印语句 一样，但由于定义的变量 name 两次赋值不同，所以打印出的结果也不完全相同 。 %s (string ) 只能打印字符串，如果想要打印数字，则需要使用 %d (data )
指定打印信息的类型 。
"""
name = "lisi"
print("hello %s,Nice to meet you!"%name)
age = 1234
print("heloo %d,Nice to meet you!"%age)
#可是，有时候我们并不知道自己要打印的是什么类型的信息，这时可以用%r 来表示
n = 100
print("you print is %r."%n)
"""
print ("ni ")
多行注释
多行注释
的语句分别对 a 和 b 赋值，通过 if 语句判断 a 与 b 的大小，如果 a 大于 b 则输出"a max!" , 否则输出 " b max!'' 。
"""
a = 2
b = 4
if a > b:
    print("a max!")
else:
    print("b max!")


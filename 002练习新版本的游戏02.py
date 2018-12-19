import random
secret = random.randint(1,100)
print('-------------------我是大鹏------------------')
temp = input ("猜错了请重新输入吧！")
guess = int(temp)
while guess != secret :
    temp = input ("你猜猜我心里想的是那个数字:")
    guess = int(temp)
    if guess == secret:
        print("你是我心里的蛔虫吗?!")
        print("哼，猜中了也没奖励!")
    else:
        if guess > secret:
             print ("嘿，大了大了~~")
        else:
            print("嘿，小了小了~~")
print("游戏结束,不玩了^_^")


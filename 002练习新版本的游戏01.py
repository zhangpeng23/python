print('-------------------我是小鱼------------------')
temp = input ("你猜猜我心里想的是那个数字:")
guess = int(temp)
if guess == 8 :
    print("你是我心里的蛔虫吗?!")
    print("哼，猜中了也没奖励!")
else:
    if guess > 8 :
         print ("嘿，大了大了~~")
    if guess < 8 :
        print("嘿，小了小了~~")
print("游戏结束,不玩了^_^")


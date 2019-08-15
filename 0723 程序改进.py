import random
secret=random.randint(1,10)
print("猜猜数字")
temp=input("猜一个数字")
guess=int(temp)
if guess==secret:
    print("猜对了，不玩了")
else:
    if guess>secret:
        print("大了")
    else:
        print("小了")
    while guess!=secret:
        #print("zai")
        temp=input("再猜一个数字吧")
        guess=int(temp)
        if guess==secret:
            print("猜对了")
        else:
            if guess>secret:
                print("大了")
            else:
                print("小了")
print("结束啦")


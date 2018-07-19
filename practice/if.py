number = 23
guess = int(input('Enter an integer :'))

if guess == number:
    # 新快从这里开始
    print('Congrattlations, you guessed it.')
    print('but you do not win any prizes!')
    # 新快在这里结束
elif guess < number:
    # 另一代码块
    print('NO, it is a little higher than that')
    # 你可以在此做任何你希望在该代码快内进行的事情
else:
    print('No, it is a little lower than that')
    # 你必须通过猜测一个大数设置的数字来到达这里

print('Done')

# 这最后一句将在
# if 语句执行完毕后执行

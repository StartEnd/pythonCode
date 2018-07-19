print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一对象的另一种名称
mylist = shoplist


# 我购买了第一个项目,所以我将其从列表中删除
del shoplist[0]


print('shoplist is ', shoplist)
print('mylist is ', mylist)
# 注意到shoplist 和mylist二者都
# 打印出了其中没有apple的同样的列表,以此我们确认
# 它们指向是同一个对象

print('Copy by making a full slice')
# 通过生成一份完成的切片制作一份列表的副本
mylist = shoplist[:]

# 删除第一个项目
del mylist[0]

print('shoplist is ', shoplist)
print('mylist is ', mylist)

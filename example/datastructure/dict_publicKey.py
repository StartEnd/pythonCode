'''如何快速找到多个字典中的公共键
球员进球统计
'''
import random
names = 'ABCDEF'

# 假设进行了10轮比赛
gameMaths = [{x: random.randint(1, 4) for x in random.sample(names,
    random.randint(3, 6))} for _ in range(6)]

print(gameMaths)

# 普通方法,依次迭代,存储在列表或集合中

game_per = list(gameMaths[0].keys())
print(game_per)
for game in gameMaths:
    for per in game_per:
        if per not in game:
            game_per.remove(per)

print(game_per)

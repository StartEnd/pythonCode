'''排列
对棋牌游戏的模拟需要混合一副牌，然后把它们发给玩家，并且不能多次使用同一张牌。
使用 choice() 会导致相同的牌被多次使用，因此可以使用 shuffle() 洗牌，然后在发牌的时候移除他们。

卡片表示为带有面值和数字。通过每次向四个列表中添加一张卡片，并且将其从牌桌上移除以使其无法再次使用而创建默认的 「hands」。
'''
import random
import itertools

FACE_CARDS = ['J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']


def new_deck():
    return [
        # 值总是用两个值,所以字符串具有
        '{:>2}{}'.format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS),
            SUITS,
        )
    ]


def show_duck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()


# 创建一副有序新牌
deck = new_deck()
print('Initial deck:')
show_duck(deck)

# 随机打乱牌的顺序
random.shuffle(deck)
print('\n shuffle duck:')
show_duck(deck)

# Deal 4 hands of 5 cards each
hands = [[], [], [], []]
for i in range(5):
    for h in hands:
        h.append(deck.pop())


# 展示手里的牌
print('\n Hands:')
for n, h in enumerate(hands):
    print('{}:'.format(n + 1), end=' ')
    for c in h:
        print(c, end=' ')
    print()


# 展示剩余的牌
print('\nRemaining deck: ')
show_duck(deck)

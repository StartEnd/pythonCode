'''保存状态
 random() 使用的伪随机数生成算法的内部状态可以被保存下来，然后用于控制子序列运行时生成的数字。
 在继续之前，从较早的输入恢复状态减少了生成重复值和序列的可能性。
 getstate() 函数可以返回随后用于 setstate() 的重新初始化随机数生成器的数据。

 getstate() 返回的数据是一个实现细节，所以这个例子使用 pickle  保存数据到文件，
 仅仅将它视作一个黑盒子。当程序开始的时候，如果该文件存在，它加载旧的状态然后继续。
 每次在保存状态前后运行生成了一些数字，去演示恢复状态导致生成器产生了再次产生了相同的值。
'''
import os
import pickle
import random

if os.path.exists('./state.dat'):
    print('Found exists state, initializating random model')
    with open('./state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    print('No esists state,seedind')
    random.seed(1)


# 生成随机数

for i in range(5):
    print('{:04.3f}'.format(random.random()), end=' ')

print()

# 为下次保存状态
with open('./state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)


# 生成更多随机数
print('\nAfter saveing state')

for i in range(5):
    print('{:04.3f}'.format(random.random()), end=' ')

print()

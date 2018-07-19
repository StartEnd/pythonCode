'''对英文文章的单词进行词频分析,找出出现次数最高的10个单词,他们出现的次数是多少'''

import re
import collections

# ./word.txt 以读的方式

with open('/Users/song/Code/python/example/datastructure/word.txt', 'r') as f:
    text = f.read()
    re_text = re.split('\W+', text)

print(re_text)

wordDic = collections.Counter(re_text)

print(wordDic.most_common(10))

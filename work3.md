# 文件操作练习之单词词频统计
# 题目:
## 小说《Walden》单词词频统计:Walden中文译名《瓦尔登湖》，是美国作家梭罗独居瓦尔登湖畔的记录，描绘了他两年多时间里的所见、所闻和所思。该书崇尚简朴生活，热爱大自然的风光，内容丰厚，意义深远，语言生动。请用Python统计小说Walden中各单词出现的频次，并按频次由高到低排序。
`示例：

lyric = 'The night begin to shine, the night begin to shine'

words = lyric.split()

print(words)

words.count(words[1])`

## step1
首先读取txt文本文件的内容
## step2
进行文本预处理，去掉符号再分割
## step3
### 1. 将特殊字符换成空格
 
	`re.sub用于替换字符串中的匹配项`

	`re.sub的函数原型为：re.sub(pattern, repl, string, count)`

	`其中第二个函数是替换后的字符串；本例中为'-'`

	`第四个参数指替换个数。默认为0，表示每个匹配项都替换。`

### 2. 替换单一的-，不是同一单词里的连字符
## step3
利用split()函数对字符串进行切片、分割，获得单词列表
## step4
获得单词频次字典

利用for循环遍历单词列表，用if条件语句判断、计数
## step5
对字典进行排序

Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。

### sorted()函数
sorted() 函数对所有可迭代的对象进行排序操作。

sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
#### sorted()方法语法：
`sorted(iterable, cmp=None, key=None, reverse=False)`
#### sorted()参数:
* iterable -- 可迭代对象。
* cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
* key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
* reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
## step6
显示字典前10项

items以列表形式返到字典键值对
# 代码
```python
import re

with open('Walden.txt') as file:

    lst=file.read()

\#print(lst)

word_text=re.sub(r'[?.!,;""/\[\]]',' ',lst) 

word_texts=re.sub(r"-",' ',word_text) 

word_list = word_texts.split()

\#print(word_list)

\#words.count(word_list[1])

word_dict={}

for word in word_list:

    if word not in word_dict:

        word_dict[word]=1 

    else:

        word_dict[word]=word_dict.get(word)+1 

dict_order=dict(sorted(word_dict.items(),key=lambda x:x[1],reverse=True)) 

print(list(dict_order.items())[:10])
```
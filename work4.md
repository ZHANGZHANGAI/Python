# Python函数
# 题目：
## 自定义求序列偶数个数的函数
## step1
将偶数提出来
## step2
计算存放偶数的列表长度，确定偶数个数
# 代码：
	def even_number(x):
    	list = []
    	for i in x:
        	if i%2 == 0:
            	list.append(i)
    	print('该序列偶数的个数是',len(list),'个')
	lst = eval(input('请输入列表list：'))
	result = even_number(lst)
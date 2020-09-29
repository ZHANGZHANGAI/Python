# 文件操作及字符串练习
# 题目：
## 编写一个程序demo.py，要求运行该程序后，生成demo_new.py文件，其中内容与demo.py一样，但需要在每一行的后面注释上行号（#1)，并且要求所有行的#垂直对齐。

`提示:
1. string.rstrip()，可以删除 string 字符串末尾的指定字符（默认为空格）；

2. string.ljust()， 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。`

## step1
读取demo.py的数据
用readlines得到列表lines，列表中的每个元素为文件中的每一行+换行符
## step2
获取最长行的长度
## step3
### enumerate() 函数
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
#### enumerate() 函数方法语法：
`enumerate(sequence, [start=0])`
#### enumerate() 函数参数：
* sequence -- 一个序列、迭代器或其他支持迭代对象。
* start -- 下标起始位置。

###过程：
for语句遍历所有行

↓

用string.rstrip()删除每行右侧的空白字符

↓

在每行固定位置添加行号

↓

（index从0开始，所以行号要从index+1开始）

↓

将添加过行号的行添加到lines中

## step4
将结果写入文件
# 代码：

	filename = 'demo.py'
	with open(filename, 'r',encoding= 'utf-8') as fp:
    	lines = fp.readlines()
	#print(lines)


	maxLength = len(max(lines,key=len))
	#print(maxLength)

	for index,line in enumerate(lines): 
    	newLine=line.rstrip()  
    	newLine=newLine+' '*(maxLength+5-len(newLine))  
    	newLine=newLine+'#'+str(index+1)+'\n'   
    	lines[index]=newLine 
	with open(filename[:-3]+'_new.py','w')as fp:    
     	fp.writelines(lines)
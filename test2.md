#题目：
## 编写一个列表处理程序，使用input（）函数接收一个列表，打印输出列表中所有不重复的元素
#思路：
## step1
刚开始的时候，要先接收一个列表，所以得使用input()函数
## step2
遍历列表中的每一元素，所以用for循环
## step3
将遍历到的元素与列表中的元素进行对比，进行判断，如果有重复值，就将重复值存在repeat列表中，如果没有，则将该元素存放在result列表中
## step4
最后将存放没有重复值的result列表输出
#代码：
	lst = eval(input('请输入列表lst：'))
	result = []
	repeat = []
	for i in lst:
	    if i in result:
	        repeat.append(i)
	    else:
	        result.append(i)
	print(result)
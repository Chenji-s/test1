print(21 + 456)
print(2+6)
'''
1.1 Python 代码单元
我们来看一个 Python 代码单元。选择下面的代码单元并运行它；
如果一切正常，你应该会看到代码单元下方显示结果。

'''
print('This is a Python code cell!')

'''
变量和数据类型
Python 支持多种数据类型，包括整数、浮点数、字符串、列表等。
你可以直接在代码单元中定义变量并输出它们的值。
'''
# 定义一个整数变量
a = 5
print(a)

# 定义一个字符串变量
b = "Hello, Python!"
print(b)

# 定义一个列表
c = [1, 2, 3, 4, 5]
print(c)
'''
Python 作为计算器

'''
print(2 + 3) 
print(2 - 3)
print(2 * 3)
print(2 / 3)  #除法
print(2 ** 3) # **表示幂运算，输出2的三次方

print(38 / 5)  #执行除法，输出浮点数，结果为7.6。
print(38 // 5) #执行地板除法，返回整除后的结果，输出7。
print(38 % 5)  #执行取余运算，返回38除以5后的余数，输出3。


'''
4 Variable Assignment（变量赋值）
在Python中，你可以将值赋给变量，这意味着你可以通过变量名来引用数据。
Python中的变量赋值不像数学中的等式，Python会按照顺序执行你定义的命令。

'''
x = 1
y = x
x = 2
print(y)


a = 8
a = a + 1
print(a)

'''
type()
该函数用于查看对象的类型。以下是代码示例：
'''
x = 2
y = 3.5
z = 'abc'

print(type(x), type(y), type(z))

#type(x) 返回 int，表示x是一个整数类型。
#type(y) 返回 float，表示y是一个浮点数类型。
#type(z) 返回 str，表示z是一个字符串类型。

'''
2 Strings
字符串对象是由一组文本字符组成的，可以用单引号或双引号来表示。
字符串类型用 str 表示。以下是代码示例：
'''

test_string = "Hello I am a string of letters!"
print(test_string)
print(type(test_string))

second_test_string = 'I am also a string'
print(second_test_string)

#test_string = 定义了一个字符串，内容为 "Hello I am a string of letters!"。
#print(test_string)：输出该字符串的内容。
#print(type(test_string))：输出 test_string 的类型，结果为 str，表示它是一个字符串。
#second_test_string = 'I am also a string'：同样可以使用单引号来定义字符串。

'''
3 Booleans
布尔类型 (Boolean) 是一种特殊的数据类型，它只有两个可能的取值：True 和 False。
在Python中，布尔类型是通过关键字 True 和 False 来表示的。
'''
print(3 > 2)
print(3 == 2)
print(3 != 2)


'''
3.2 布尔运算符（Boolean Operators）

在Python中，布尔运算符可以用于组合或操作布尔表达式。常见的布尔运算符包括：

and：当且仅当两个表达式都为True时，返回True。
or：只要有一个表达式为True，就返回True。
not：对布尔表达式取反，如果表达式为True，那么not将返回False，反之亦然。
'''

x = True
y = False

print(x and y)  # False，因为y是False
print(x or y)   # True，因为x是True
print(not x)    # False，因为x是True，取反后为False

'''
4. Integers（整数）
Python可以无限精度地表示整数(即，任意大，只要内存中有剩余空间来存储它们!)。
整数类型用int表示。我们可以用通常的方法对整数进行加、减、乘、除运算:
 '''
'''
5. Floating Point Numbers（浮点数）
浮点数（float）是用来表示带有小数点的数字。
它们可以表示非常大的或非常小的数字，并且可以包含小数部分。
'''
print(3.456 + 11.888)
print(99.9 / 0.1)
print(2.0 * 11.4)
print(1.5e-5 + 1.0e-6)
print(type(2.0 * 11.4))

'''

6. Type-casting（类型转换）
类型转换是指将一种数据类型转换为另一种数据类型。
Python提供了几个内置函数来进行显式类型转换，比如 int()、float() 和 str()
'''
#手动类型转换：有时，我们需要显式地改变对象的类型。
# 这可以通过内置函数如 int()、float() 或 str() 来完成。

i = 2566
print(type(i))        # 输出 <class 'int'>
print(float(i))       # 输出 2566.0，转换为浮点数
print(str(i))         # 输出 '2566'，转换为字符串

string_number = '273'
print(float(string_number))  # 输出 273.0，字符串转换为浮点数
print(int(string_number))    # 输出 273，字符串转换为整数
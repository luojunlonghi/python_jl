'''

1.先讲bug
Traceback (most recent call last):
❶   File "hello_world.py", line 2,(第二行) in <module>
❷     print(mesage)
❸ NameError: name 'mesage' is not defined

Traceback 这个出现，后面会说明在哪里有出错，mesage' is not defined没写变量(定义)

'''
#print(mesage)
'''
2.变量，赋给一个名字意义
变量命名格式:
①变量名只能包含字母、数字和下划线。不能以数字打头。
②变量名不能包含空格
③不要将Python关键字和函数名用作变量名
④变量名应既简短又具有描述性。例如，name比n 好，student_name比s_n好，name_length 比length_of_persons_name 好。
⑤慎用小写字母l 和大写字母O，因为它们可能被人错看成数字1 和0
'''
name_length=1
print(name_length)
'''
类型
字符串 用引号括起的

常用方法
①title():以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写
②name.upper()
③name.lower()
字符串改为全部大写或全部小写
'''
name='this is a string'
print(name.title())
print(name.upper())
print(name.lower())


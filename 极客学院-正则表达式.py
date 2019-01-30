# 正则表达式

import re

# re:regular expression 正则表达式英文字母缩写

#=======================findall的使用==========================================
content = '我的银行可密码是：1234567， QQ密码是：33445566， 微博密码是：8888888， Github密码是：12345，帮我记住他们'

password_list = re.findall('：(.*?)，', content)
# 括号把问号括起来，返回冒号后面的内容，但是也要写上冒号，这是content中的规律，密码前都有冒号
# findall 返回的是列表

name_list = re.findall('名字是(.*?)，', content)

# 注意中英文的冒号，逗号等，需要对应一致，且空格要一致，
# 如：后面不要多加空格，以免在findall中不一致报错
print('找到内容，返回: {}'.format(password_list))
print('未找到内容，返回: {}'.format(name_list))




# ==========包含多个括号的正则表达式，返回的仍是列表，只是列表中的元素变为元组=================

account_content = '我的银行卡账号是：Robert，密码是：1234567， QQ账号是：萝卜，密码是：33445566， 微博密码是：8888888， Github密码是：12345，帮我记住他们'

account_password = re.findall('账号是：(.*?)，密码是：(.*?)，', account_content)
print('包含多个括号的情况下，返回账号和密码：{}'.format(account_password))


# 加上可省略的flag的辅助作用，可实现忽略大小写，过滤掉换行符的影响等
big_string_mutil = '''
我是萝卜，我的微博密码是： 123
456789，
'''
password_findall_no_flag = re.findall('密码是：(.*?)，', big_string_mutil)
password_findall__flag = re.findall('密码是：(.*?)，', big_string_mutil, re.S)

print('不使用re.S的时候：{}'.format(password_findall_no_flag)) # 存在换行符，无法检测到字段
print('使用re.S的时候：{}'.format(password_findall__flag))










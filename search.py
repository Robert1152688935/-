# ===============re.search()==================================
# search() 与 findall() 相反，返回第一个满足要求的字符串后就停止
# 适用于超级大的文本里面只寻找第一个数据
import re

content = '我的银行可密码是：1234567， QQ密码是：33445566， 微博密码是：8888888， Github密码是：12345，帮我记住他们'

password_search = re.search('密码是：(.*?)，', content)
password_search_not_find = re.search('xxx：(.*?)，', content)

print(password_search)  # 若匹配不成功，显示None
print(password_search.group())  # 匹配成功后需要通过.group() 该方法来获取里面的值

print(password_search.group(0)) # 返回匹配值，即不仅仅是括号中的，为 密码是：1234567

print(password_search.group(1)) # 返回括号中的值，1表示第一个括号， 为 1234567
# group方法中的参数不可超过正则表达式里面括号的参数

print(password_search_not_find) # 如果在find后面再加上方法group则会报错



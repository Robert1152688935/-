
# .*: 表示匹配一段任意长度的字符串任意次
# .*?: 表示匹配一个能满足要求的最短字符串
import re

content = '我的银行可密码是：1234567， QQ密码是：33445566， 微博密码是：8888888， Github密码是：12345，帮我记住他们'

without_question_mark = re.findall('密码是：(.*)，', content)
with_question_mark = re.findall('密码是：(.*?)，', content)

print('不使用问号返回：{}'.format(without_question_mark))
# 只有一个元素的列表：长字符串

print('使用问号后返回：{}'.format(with_question_mark))
# 四个元素的列表，每个元素直接就是密码，直接


# 一句话总结：.*: 贪婪模式，获取最长的满足条件的字符串
           # .*?：非贪婪模式(易满足模式) 获取最短的能满足条件的字符串






















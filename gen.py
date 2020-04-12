import random

text_list = ['我好菜啊', '我菜爆了', '我是什么垃圾', '我好堕落','我好菜菜啊 再这样下去就没人要了 我就只能混吃等死了']

last_input = '123'
stop_signal = 'Bye'
while last_input != stop_signal:
    print('<- {}'.format(text_list[int(hash(last_input)) % len(text_list)]), end='\n')
    print('-> ', end='')
    last_input = input()


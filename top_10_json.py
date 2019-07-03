# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
#
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.

import json
# from pprint import pprint

def max_value_of_keys(dict):
    # функция для поиска ключа с максимальным значением
    index = 0
    key_ = None
    for key in dict.keys():
        if index < dict[key]:
            index = dict[key]
            key_ = key
            continue
    return key_

if __name__ == '__main__':
    pass

lst_news = list()

with open('newsafr.json') as data:
    dfile = json.load(data)
    for dict in dfile['rss']['channel']['items']:
        lst_news.extend(dict['description'].split())
        # title тоже включаем, т.к. заголовок новости тоже является частью новости и попадает под условия ДЗ
        lst_news.extend(dict['title'].split())

num = 0
dict = {}
for word in lst_news:
    if len(word) > 6:
        num = lst_news.count(word)
        dict.update({word: num})

lst_top = []
lst_top_num = []
# списки. не стал использовать словарь, т.к. словарь неупорядочен в отличии от списков.
index = 0
while index < 10:
    key = max_value_of_keys(dict)
    lst_top.append(key)
    lst_top_num.append(dict.pop(key))
    index += 1

print('ТОП-10 самых популярных слов в новостях:')
for index, top in enumerate(zip(lst_top, lst_top_num)):
    print(f'{" " * 3}{index+1}. {top[0]} - {top[1]} шт.')

import requests
from GDZ_PY import utils
from bs4 import BeautifulSoup as BS


def get_exercises(link='https://gdz.ru/class-1/matematika/moro-m-i-2011/'):
    # берем список элементов с ссылками на задания
    exercises_list = BS(requests.get(link).text, features="html.parser").find('div', class_='task-list folded')
    # редачим ссылку для удобства
    link = link.replace('https://gdz.ru', '')
    # выбираем все ссылки которые ведут на задания
    exercises = exercises_list.find_all('a', href=lambda href: link in href)
    # создаем список для вывода
    exercises_list_new = list()
    # перебираем каждое упражнение
    for exer in exercises:
        # здесь будем хранить инфу об задании
        exercise = dict()
        # получаем номерной список
        num_list = utils.parse(exer['href'].split('/')[-2])[0]
        # здесь записано количество аргументрв
        exercise['nums_len'] = num_list.__len__()
        # тут сами аргументы
        exercise['nums'] = num_list
        # тут шаблон для адреса
        exercise['pattern'] = utils.parse(exer['href'].split('/')[-2])[1]
        # для удобства определяем тип чисел
        if num_list.__len__() == 3:
            exercise['type'] = 'chast-str/les-num'
        elif num_list.__len__() == 2:
            exercise['type'] = 'chast-str/les'
        elif num_list.__len__() == 1:
            exercise['type'] = 'les/str'
        # варганим ссылку на упражнение
        exercise['link'] = 'https://gdz.ru' + link + exer['href'].split('/')[-2]
        # добавляем к выводу
        exercises_list_new.append(exercise)
    return exercises_list_new


if __name__ == '__main__':
    print(get_exercises())

import requests
from bs4 import BeautifulSoup as BS


def get_classes_links():
    link_str = BS(requests.get('https://gdz.ru').text, features="html.parser")  # получаем страницу
    # выбиваем инфу классов в список
    classes_books = list(BS.find(link_str, 'div', {'class': 'box-menu'}).div.children)[1:-1]
    # сюда будем сейвить инфу
    classes_list = dict()
    # в classes_list почему то через одну строку пустые строки которые все ломают, также последним элементом идут
    # видеорешения (они нам нах не нужны)
    for class_ in classes_books[:-1:2]:
        # здесь будут храниться предметы одного класса
        items = dict()
        # в этой переменной будем все классы в список помещать
        items2 = class_.find_all('li')
        # делаем ссылку на название предмета и сохраняем в словарь
        for item in items2[1:]:
            items[item.a.text] = 'https://gdz.ru' + item.a['href']
        # забираем название класса (№ класс)
        class_number = ' '.join((items2[0].text.replace('\n', '').strip()).split(' ')[:2])
        # сейваем в общий словарь
        classes_list[class_number] = items
    return classes_list


if __name__ == '__main__':
    classes = get_classes_links()
    print(classes)

import requests
from bs4 import BeautifulSoup as BS


# над этой херней конечно пришлось попариться
def get_school_textboks(link='https://gdz.ru/class-1/matematika/'):
    # получаем страницу
    link_str = BS(requests.get(link).text, features="html.parser")
    # берем главный раздел
    booklist_menu = list(BS.find(link_str, 'main',
                                 {'class': 'content box bg-w full-width'}).find_all('ul', {'class': 'book-list'}))
    # здесь будем хранить книги
    return_books = list()
    # какого то хрена книги хранятся в "комплектах" по 4 штуки. Надо перебирать "комплекты"
    for books_list in booklist_menu:
        # сохраняем книги в список
        books = books_list.find_all('li', {'class': 'book'})
        # перебираем книги в "комплекте"
        for book in books:
            # сюда будем сейвить инфу о книге
            info = dict()
            # тут у нас вся внешняя инфа о книге она тупо вычленяется и запихивается. Объяснять как не буду
            lots = book.find_all('p', {'class': 'book-description-sub'})
            for lot in lots:
                lot_name = ' '.join(lot.b.text.split()).replace(':', '').strip()
                lot_text = ' '.join(lot.text.split()).replace(lot_name, '').replace(':', '').strip()
                info[lot_name] = lot_text
            else:
                # Вычленяем название, узнаем премиум и получаем ссылку на страницу книги
                lots_name = book.find('p', {'class': 'book-description-main'})
                info['book_name'] = ' '.join(lots_name.text.split())
                lots_premium = book.find('p', {'class': 'book-description_premium'})
                info['premium'] = bool(lots_premium)
                lots_link = book.find('a', {'class': 'book book-regular text-undecorated'})
                info['link'] = 'https://gdz.ru' + lots_link['href']
            # добавляем книгу к пакету остальных
            return_books.append(info)
    return return_books


if __name__ == '__main__':
    print(get_school_textboks())

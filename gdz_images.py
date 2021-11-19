import requests
from bs4 import BeautifulSoup as BS
from GDZ_PY import utils


def get_gdz_images(link='https://gdz.ru/class-10/geometria/atanasyan-10-11/10-class-95/', error_type='None'):
    # берем страницу
    page_code = BS(requests.get(link).text, features="html.parser")
    # чекаем существует ли такая стрница
    if page_code.find('h1', text='Ошибка 404 -страница не найдена'):
        if error_type == 'None':
            return None
        else:
            return 404
    else:
        # берем блок с фотками ответов
        images_divs = page_code.find('figure').find_all('div', class_='with-overtask')
        # тут будем сейвать ссылки на фотки
        images_links = list()
        # перебираем все фотки в этом блоке
        for image_div in images_divs:
            # делаем вместо даунской ссылки адекватную
            images_links.append('https:' + image_div.img['src'])
        return images_links


if __name__ == '__main__':
    print(utils.link_creator('https://gdz.ru/class-10/geometria/atanasyan-10-11/', utils.parse('10-class-95')))
    print(get_gdz_images(utils.link_creator('https://gdz.ru/class-10/geometria/atanasyan-10-11/',
                                            utils.parse('10-class-95'))))

from GDZ_PY import classes, school_textbooks, exercises, gdz_images, utils


def get_classes_links():
    return classes.get_classes_links()


def get_school_textboks(link):
    return school_textbooks.get_school_textboks(link)


def get_exercises(link):
    return exercises.get_exercises(link)


def get_gdz_images(link):
    return gdz_images.get_gdz_images(link)


if __name__ == '__main__':
    print(get_classes_links())
    print(get_school_textboks(get_classes_links()['10 класс']['Геометрия'])[0]['link'])
    print(get_exercises(get_school_textboks(get_classes_links()['10 класс']['Геометрия'])[0]['link']))
    print(get_gdz_images(get_exercises(get_school_textboks(get_classes_links()['10 класс']['Геометрия'])[0]['link'])[0]
                         ['link']))

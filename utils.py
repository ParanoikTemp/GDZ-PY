def parse(text):
    new_text = ''
    new_text2 = ''
    for char in text:
        if char.isdigit():
            new_text += char
            new_text2 += ' '
        else:
            new_text += ' '
            new_text2 += char
    return new_text.split(), new_text2.split()


def address_constructor(args, patterns):
    if not args:
        return None
    if not patterns:
        return ''.join(list(args))
    if patterns and args:
        link = ''
        for i, el in enumerate(args[:-1]):
            link += el + patterns[i]
        link += args[-1]
        return link


def link_creator(link, args):
    if 'https://gdz.ru' in link:
        return link + address_constructor(args[0], args[1])
    else:
        return 'https://gdz.ru' + link + address_constructor(args[0], args[1])


if __name__ == '__main__':
    nums, pattern = parse('12-4-prt-212')
    print(nums, pattern)
    print(address_constructor(nums, pattern))

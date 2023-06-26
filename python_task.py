import re

SOURCE_LIST = [
    'Андрей 9',
    'Василий 11',
    'Роман 7',
    'X Æ A-12 45',
    'Иван Петров 3',
    'Андрей 6',
    'Роман 11',
]

if __name__ == "__main__":
    result = dict()
    for row in SOURCE_LIST:
        if not re.match(r'^[a-zA-Zа-яА-Я0-9\s]+ \d+$', row):
            continue

        row_array = row.split(' ')

        name = ' '.join(row_array[:-1])
        hours = row_array[-1]
        if not result.get(name):
            result[name] = []

        result[name].append(int(hours))

    for name, hours_list in result.items():
        print(f'{name}: {", ".join(map(str, hours_list))}; sum: {sum(hours_list)}')

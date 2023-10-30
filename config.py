from configparser import ConfigParser
import os

# список id компаний
# Яндекс, Билайн, МТС, Kaspersky, Tinkoff, Озон, СБЕР, Альфа-банк, Аэрофлот, РЖД
employer_ids = [1740, 4934, 3776, 1057, 78638, 2180, 3529, 80, 1373, 23427]

JSON_DATA_DIR = os.path.join('data')
JSON_FILE_NAME = 'data.json'


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()

    parser.read(filename)
    if parser.has_section(section):
        params = parser.items(section)
        db = dict(params)
    else:
        raise Exception("Раздел не найден")
    return db
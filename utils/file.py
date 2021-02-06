import re
import os


def get_extension(file_name):
    '''
        Возвращаем расширение имени файла
        name.jpg -> .jpg
    '''
    return re.findall(r'^.*(\.\w{2,4})$', str(file_name))[0]


def get_name_file(file_name):
    '''
        Возвращаем имя файла без разрешения
        name.jpg -> name
    '''
    return re.findall(r'^(.*)\.\w{2,4}$', str(file_name))[0]


def get_extension_and_filename(file_name):
    '''
        Возвращаем имя файла и его расширение
        name.jpg -> return name, .jpg
    '''
    return re.findall(r'^(.*)\.\w{2,4}$', str(file_name))[0], re.findall(r'^.*(\.\w{2,4})$', str(file_name))[0]


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)

import os
import time

def file_data(directory):
    all_data_files = {}  # Создание словаря данных обо всех файлах.
    for roots, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(roots, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)

            # Строка данных об одном файле:
            line_data_file = (f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
                              f'Время последнего изменения: {formatted_time}, Родительская директория: {parent_dir}')

            all_data_files[file] = line_data_file # Присвоение ключу all_data_files значения line_data_file.
    return all_data_files

# Пример 1 работы функции file_data(directory):
# print()
# K = file_data(r'D:\Учёба\Urban Univ\Ph.Разраб_Модуль 7\UU_DZ_7_2')
# K_values = list(K.values()) # Создание списка значений словаря K.
# for i in range(len(K_values)):
#     print(K_values[i])

# Пример 2 работы функции file_data(directory):
# print()
# T = file_data(".")
# T_values = list(T.values()) # Создание списка значений словаря T.
# for i in range(len(T_values)):
#     print(T_values[i])
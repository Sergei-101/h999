# Напишите функцию, которая получает на вход директорию и рекурсивно обходит
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию. Для каждого объекта укажите файл
# это или директория. Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.
# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# }


import os
import json
import pickle
import csv

if __name__ == '__main__':
    def directory_traversal(directory_address: str, name_file: str):
        """Функция, которая получает на вход директорию
           и рекурсивно обходит её и все вложенные директории
        """
        test_list = []
        for roots, dirs, files in os.walk(directory_address):
            for file in files:
                test_dict = {}
                file_patch = os.path.join(roots, file)
                test_dict["name"] = file
                test_dict["parent"] = str(*roots.rsplit("\\")[-1:])
                test_dict["type"] = "file"
                test_dict["size"] = os.path.getsize(file_patch)
                test_list.append(test_dict)


        with open(name_file + '.json', 'w', encoding='utf-8') as f:
            json.dump(test_list, f, indent=4)

        with open(name_file + '.picle', 'wb') as f:
            pickle.dump(test_list, f)


        with open(name_file + '.csv', 'w', encoding='utf-8', newline="") as f:
            fieldnames = ["name", "type", "parent", "size"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(test_list)

    directory_traversal("dir_f", "test2")

from os import path, walk


def show_tree():
    for folder_path, folders, files in walk("./root_Folder/"):
        
        print('-----')
        print('Путь - ', folder_path)

        if folders:
            print('Папки - ', folders)

        if files:
            print('Файлы - ', files)


show_tree() 
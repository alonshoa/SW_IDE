import pytest
import os
import shutil


class FileExplorer:
    def __init__(self, path):
        self.path = path

    def get_files(self):
        return os.listdir(self.path)

    def get_file_size(self, file_name):
        return os.path.getsize(os.path.join(self.path, file_name))

    def get_file_content(self, file_name):
        with open(os.path.join(self.path, file_name), 'r') as f:
            return f.read()

    def create_file(self, file_name):
        with open(os.path.join(self.path, file_name), 'w') as f:
            f.write('')

    def delete_file(self, file_name):
        os.remove(os.path.join(self.path, file_name))

    def create_folder(self, folder_name):
        os.mkdir(os.path.join(self.path, folder_name))

    def delete_folder(self, folder_name):
        shutil.rmtree(os.path.join(self.path, folder_name))


def test_get_files():
    file_explorer = FileExplorer('.')
    file_explorer.create_file('test_file.txt')
    file_explorer.create_file('file.py')
    assert set(['file.py', 'test_file.txt']).issubset(file_explorer.get_files())
    file_explorer.delete_file('test_file.txt')
    file_explorer.delete_file('file.py')


def test_get_file_size():
    file_explorer = FileExplorer('.')
    file_explorer.create_file('file.py')
    assert file_explorer.get_file_size('file.py') == 0
    file_explorer.delete_file('file.py')


def test_get_file_content():
    file_explorer = FileExplorer('.')
    with open("file.py",'w') as f:
        f.write("import pytest")
    assert file_explorer.get_file_content('file.py') == 'import pytest'
    file_explorer.delete_file('file.py')

def test_create_file():
    file_explorer = FileExplorer('.')
    file_explorer.create_file('test_file.txt')
    assert 'test_file.txt' in file_explorer.get_files()
    file_explorer.delete_file('test_file.txt')


def test_delete_file():
    file_explorer = FileExplorer('.')
    file_explorer.create_file('test_file.txt')
    file_explorer.delete_file('test_file.txt')
    assert 'test_file.txt' not in file_explorer.get_files()


def test_create_folder():
    file_explorer = FileExplorer('.')
    file_explorer.create_folder('test_folder')
    assert 'test_folder' in file_explorer.get_files()
    file_explorer.delete_folder('test_folder')


def test_delete_folder():
    file_explorer = FileExplorer('.')
    file_explorer.create_folder('test_folder')
    file_explorer.delete_folder('test_folder')
    assert 'test_folder' not in file_explorer.get_files()

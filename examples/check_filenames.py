import os
import shutil
import sys
import re

def check_class_name(file_name, class_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        cc = 0
        for line in lines:
            if 'class' in line:
                cc+=1
                if class_name in line:
                    return True

    return cc == 0


def print_err_file_names(file_names):
    for file_name in file_names:
        print(file_name)

def check_file_name(file_name):
    if '_' not in file_name:
        return False
    return True

def get_class_name(file_name):
    class_name = file_name.split('.')[0]
    class_name = re.sub('_', ' ', class_name)
    class_name = class_name.title()
    class_name = re.sub(' ', '', class_name)
    return class_name

def main(path=sys.argv[1]):
    file_names = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                if not check_file_name(file):
                    file_names.append(os.path.join(root, file))
                class_name = get_class_name(file)
                if not check_class_name(os.path.join(root, file), class_name):
                    file_names.append(os.path.join(root, file))
    print_err_file_names(file_names)

if __name__ == '__main__':
    # path = sys.argv[1]
    path = "../src/utils"
    main(path)



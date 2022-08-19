import re
import os


def parse(file_name):
    res_flag = False
    regex = re.compile(r'Error #1:')
    with open(r"{}".format(file_name)) as file:
        for line in file:
            match = regex.match(line)
            if match:
                res_flag = True
                break
    return res_flag


if __name__ == '__main__':
    with open('filename.txt') as file:
        for line in file:
            real_path = re.search("restest\\\\DrMemory-.*\\\\results.txt", line).group()
            if parse(real_path):
                os.system('echo "There are memory leaks in the code."')
                os.system(f'type {real_path}')

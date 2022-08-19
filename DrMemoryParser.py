import re
import os


def parse(file_name):
    regex = re.compile(r'Error #1:')
    with open(r"{}".format(file_name)) as error_file:
        for file_line in error_file:
            match = regex.match(file_line)
            if match:
                return True
    return False


if __name__ == '__main__':
    if parse("results.txt"):
        os.system('echo There are memory leaks in the code')  # keyword for an error in teamcity
        os.system(f'type results.txt')  # dr memory log to log
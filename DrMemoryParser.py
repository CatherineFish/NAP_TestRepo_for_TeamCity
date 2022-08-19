import re
import os


def parse(file_name):
    res_flag = False
    regex = re.compile(r'Error #1:')
    with open(file_name) as file:
        for line in file:
            match = regex.match(line)
            if match:
                res_flag = True
                break
    return res_flag


if __name__ == '__main__':
with open('restest\file_name.txt') as file:
	for line in file:
		if parse(line):
			os.system('echo "There are memory leaks in the code."')
			os.system(f'type {line}')

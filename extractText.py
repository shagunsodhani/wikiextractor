import json
import os
import re
from glob import glob

TEXT = "text"
NEWLINE = "\n"
base_path = "<add the path of the directory where the json files are extracted>"
file_name = ""


def get_file_iterator(base_path):
    '''Method to get the iterator of all the files under a given base path'''
    file_dir_iterator = (y for x in os.walk(base_path) for y in glob(os.path.join(x[0], '*')))
    file_iterator = filter(lambda file_name: os.path.isfile(file_name), file_dir_iterator)
    return file_iterator


def parse_line(line):
    '''Method to parse a given json line'''
    data = json.loads(line)
    return '\n'.join(
        map(lambda para: re.sub('\s+', ' ', para).strip(),
            filter(lambda text: text.strip(), data[TEXT].split(NEWLINE))
            )).strip()


def parse_file(file_name):
    '''Method to parse a file given its name'''
    with open(file_name) as f:
        for line in f:
            yield parse_line(line)


def parse_dir(base_path):
    '''Method to parse all the files in a base directory'''
    for file_name in get_file_iterator(base_path):
        for line in parse_file(file_name):
            print(line)


parse_dir(base_path=base_path)

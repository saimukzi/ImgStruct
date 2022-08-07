import argparse

parser = argparse.ArgumentParser()
parser.add_argument('test_id_list', nargs='*')
args = parser.parse_args()

import os
import re
import sys

MY_PATH = os.path.realpath(__file__)
PROJECT_PATH = os.path.dirname(os.path.dirname(MY_PATH))
SRC_PATH = os.path.join(PROJECT_PATH, 'src')
TESTCASE_PATH = os.path.join(PROJECT_PATH, 'testcase')
# print(SRC_PATH)

sys.path.append(SRC_PATH)

import img_struct.img_struct

test_id_list = args.test_id_list
if len(test_id_list) == 0:
    test_id_list = os.listdir(TESTCASE_PATH)
    test_id_list = filter(lambda i: re.match('\d+-.+',i), test_id_list)
    test_id_list = filter(lambda i: os.path.isdir(os.path.join(TESTCASE_PATH,i)), test_id_list)
    test_id_list = list(test_id_list)

for test_id in test_id_list:
    img_struct.img_struct.main(
        os.path.join(TESTCASE_PATH, test_id, 'input.json'),
        os.path.join(TESTCASE_PATH, test_id, 'output.png'),
    )

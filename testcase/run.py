import os
import sys

MY_PATH = os.path.realpath(__file__)
PROJECT_PATH = os.path.dirname(os.path.dirname(MY_PATH))
SRC_PATH = os.path.join(PROJECT_PATH, 'src')
print(SRC_PATH)

sys.path.append(SRC_PATH)

import img_struct.img_struct

img_struct.img_struct.main()

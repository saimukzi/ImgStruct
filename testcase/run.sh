#!/bin/bash -e

PROJECT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; cd .. ; pwd -P )"
TMP_PATH="/tmp/ImgStructTest"

cd ${PROJECT_PATH}/testcase

rm -rf ${TMP_PATH}
mkdir -p ${TMP_PATH}

python3 -m venv ${TMP_PATH}/venv
. ${TMP_PATH}/venv/bin/activate
pip install --upgrade pip wheel
pip install futsu

export PYTHONPATH=${PYTHONPATH}:${PROJECT_PATH}/src
# echo PYTHONPATH=${PYTHONPATH}

python3 -m img_struct.img_struct 000-empty/input.json 000-empty/output.json
python3 -m img_struct.img_struct 001-rect/input.json  001-rect/output.json

#!/bin/bash

pip install -U -r requirements.txt
python setup.py develop
pyinstaller -r file_a.so,dll,file_a.so -r file_b.so,dll,file_b.so -F ./bin/hello

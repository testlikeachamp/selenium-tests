#!/usr/bin/env bash

# create new dir
mkdir selenium-tests

cd selenium-tests/

# create python virtual env
python3 -m venv venv

# activate virtual env
source venv/bin/activate

# update setuptools
pip install -U setuptools

# create new top-requirements.txt file with just names of libraries you will import in your code
# install your top level requirements
pip install -r top-requirements.txt

# freeze dependencies into a requirements.txt file
pip freeze > requirements.txt

# add new dependencies to top-requirements.txt and
# repeat: pip install -r top-requirements && pip freeze > requirements


# https://docs.python.org/3/library/venv.html
# Steps Mac/linux
# Path can be relative path too. If target directory doesn't exist Python will create it.
python3 -m venv /path/to/new/virtual/environment

# activate venv
source /path/to/new/virtual/environment/bin/activate  # Mac
# now run pip install or python - it will use your venv!

# deactivate when done
deactivate

#########################################
# Steps Windows
python -m venv c:\path\to\myenv  # this can be relative path too (directory doesn't need to exist, python will create it
# activate venv
<venv>\Scripts\activate.bat
# now run pip install or python - it will use your venv!

deactivate.bat  # when finished
##########################################

# for Mac
unzip /Users/${USER}/Downloads/chromedriver_mac64.zip -d /usr/local/bin/
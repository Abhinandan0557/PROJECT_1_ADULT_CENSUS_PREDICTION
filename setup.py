
'''this file looks for all requirements and dependencies and install them.
find_packages() - is used to find which folder conatin __init__.py file and consider these folder as packages
'''

from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."  #this -e . is required in requirements.txt to trigger setupe.py file at start.

#creating list of requirement libraries
def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

#-e . is not a library so we have to remove it
if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name="ADULT_CEBNSUS_PREDICTION",
    version="0.0.1",
    author="ABHINANDAN CHOUGULE",
    author_email="abhi.c0557@gmail.com",
    packages= find_packages(),    #it will consider folder as python package which contain __init__.py file
    install_requires= get_requirements(),

)
from setuptools import find_packages,setup

setup(
    name="ADULT_CEBNSUS_PREDICTION",
    version="0.0.1",
    author="ABHINANDAN CHOUGULE",
    author_email="abhi.c0557@gmail.com",
    packages= find_packages(),    #it will consider folder as python package which contain __init__.py file
    install_requires= get_requirements(),

)
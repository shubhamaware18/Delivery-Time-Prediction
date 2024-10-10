from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'delivery_time_prediction'
VERSION = '1.0.0'
AUTHOR_NAME = 'Shubham Aware'
AUTHOR_EMAIL = 'imawareshubh18@gmail.com'


# open requirements.txt and read it

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."
def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list

setup(
    name=PROJECT_NAME,  
    version=VERSION,  
    author=AUTHOR_NAME,  
    author_email=AUTHOR_EMAIL,  
    description='A project for predicting delivery time using machine learning',  
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    url='https://github.com/shubhamaware18/delivery_time_prediction',  
    packages=find_packages(),  
    install_requires= get_requirements_list()
)

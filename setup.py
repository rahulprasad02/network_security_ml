'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

# find_packages => finds __init__.py in every folder and considers the parent folder as a package

# function to fetch requirements from requirements.txt
def get_requirements()-> List[str]:
    
    requirements_lst : List[str] = []

    try:
        with open('requirements.txt','r') as file:
            # read lines from requirements
            lines = file.readlines()
            # process lines
            for line in lines:
                requirement = line.strip()
                # ignore "-e ." and empty lines
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        return "requirements.txt file not found"
    
    return requirements_lst
    

# print(get_requirements())


# building meta-info
setup(
    name="NetworkSecurityDetails",
    version="0.0.1",
    author="Rahul Prasad",
    author_email="prasadrahul2002@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

# working ->
# when we hit pip install -r requirements.txt (given this file have -e .), -e . redirects to setup.py and a folder with above details is created. This is usually done in the end.


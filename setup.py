from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e . '
def get_requiremetns(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requiremetns=[]
    with open(file_path) as file_obj:
        requiremetns = file_obj.readlines()
        requiremetns = [ req.replace("\n","") for req in requiremetns]

        if HYPEN_E_DOT in requiremetns:
            requiremetns.remove(HYPEN_E_DOT)


setup(
name='MLPorject',
version='0.1',
author='Ashfaq Shaikh',
author_email='Ashfaq664236@gmail.com',
packages=find_packages(),
install_requires = get_requiremetns('requirements.txt')

)
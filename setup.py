from setuptools import find_packages, setup
from typing import List

hypen_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if hypen_dot in requirements:
            requirements.remove(hypen_dot)

setup(
    name='mlproject',
    vesrion='0.0.1',
    author='mingma',
    author_email='mingmarlepcha2000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
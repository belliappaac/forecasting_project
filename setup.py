from setuptools import setup, find_packages
from typing import List

hpen_dot = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements file and returns a list of packages.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hpen_dot in requirements:
            requirements.remove(hpen_dot)


    return requirements

setup(
    name="forecasting_project_1",
    version="0.0.1",
    description="Demand Forecasting Project",
    author="Belliappa A C",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
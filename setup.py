from setuptools import find_packages,setup
from typing import List

HYPE_E_DOT ="-e ." 

def get_requirements(file_path:str):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)
    
    return requirements

setup(
    name="mlprojec",
    version="0.0.1",
    author="Satyam",
    author_email="satyambhalerao24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)




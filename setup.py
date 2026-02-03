from setuptools import setup,find_packages
hyphen_e='-e .'

from src.logger import logging

def get_packages(filepath):
    with open(filepath) as f:
        content=f.readlines()
        require= [pack.strip() for pack in content if pack!=hyphen_e]
    logging.info("Installing.... ",require)
    return require
    
# print(get_packages("requirements.txt"))



setup(
    name="End-to-End",
    version="0.01",
    description="This is End - to - end learning package",
    author="Abhishek",
    packages=find_packages(),
    install_requires=get_packages("requirements.txt")
    )

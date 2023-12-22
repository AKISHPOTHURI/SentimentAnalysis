from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='Sentiment_Analysis_Project',
    version='0.0.1',
    author='Akish',
    author_email='akishpothuri@gmail.com',
    description="A python package for Sentiment Analysis app",
    github_directory='https://github.com/AKISHPOTHURI/SentimentAnalysis',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
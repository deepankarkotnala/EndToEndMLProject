from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."   ## this needs to be ignored while reading packages in requirements.txt file 

def get_requirements(file_path:str)->List[str]:
    ''' 
    This function will return the list of requirements.
    It will read the package/library requirements from the file_path --> which would be the requirements file 
    --> requirements.txt 
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  ## read line by line, remove '\n' 
        ## list comprehension to remove '\n' 
        requirements = [req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
    
    
setup(
    name = 'mlproject',
    version='0.0.1',
    author='Deepankar',
    author_email='dkotnala5@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)
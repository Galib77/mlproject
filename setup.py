# Import necessary functions from setuptools
from setuptools import find_packages, setup
# Import typing module for type hints
from typing import List

# Define a constant string '-e .'
HYPEN_E_DOT='-e .'

# Define a function to get requirements from a file
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    # Initialize an empty list to store requirements
    requirements=[]
    # Open the requirements file
    with open(file_path) as file_obj:
        # Read lines from the file
        requirements=file_obj.readlines()
        # Remove newline characters from each line and store them in a list
        requirements=[req.replace("\n","") for req in requirements]
        
        # Check if '-e .' exists in requirements list
        if HYPEN_E_DOT in requirements:
            # If it exists, remove it from the list
            requirements.remove(HYPEN_E_DOT)
    
    # Return the list of requirements
    return requirements

# Setup function to define the distribution
setup(
    name='mlproject',  # Name of the distribution
    version='0.0.1',   # Version number
    author='Galib',    # Author's name
    author_email='razagalib7@gmail.com',  # Author's email
    packages=find_packages(),  # Find all packages in the current directory
    install_requires=get_requirements('requirements.txt')  # Get requirements from requirements.txt file
)


'''
Purpose of get_requirements function:--
This function is commonly used in Python projects to dynamically retrieve dependencies listed in a requirements.
txt file and pass them to the install_requires parameter of the setup() function when using tools like setuptools 
for packaging and distribution.

Parameters:-
file_path: This parameter specifies the path to the file containing the requirements.

Functionality:-
The function opens the specified file (file_path).
It reads the lines of the file, which typically contain the names of Python packages or modules required for the project.
It removes any newline characters (\n) from each line.
If the constant HYPEN_E_DOT (often used in editable installations) is found in the list of requirements, it removes it.
Finally, it returns the list of requirements.

'''
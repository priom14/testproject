from setuptools import find_packages,setup


def get_requirements(file_path):
    
    requirements = []
    
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
    if '-e .' in requirements:
        requirements.remove('-e .')
    
    return requirements


setup (
    name = "testproject",
    version = '0.0.1',
    author= 'Priom Pal',
    author_email= 'priompalnfs@yahoo.com',
    packages= find_packages(),
    install_requires = get_requirements('requirments.txt')
)
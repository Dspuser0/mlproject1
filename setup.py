from setuptools import find_packages,setup
from typing import List

HYPEN_DONT='-e .'
def  get_requirements( file_path:str)->List[str]:
    
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[r.replace("\n","") for r in req]
        print(req)
        if HYPEN_DONT in req:
            req.remove(HYPEN_DONT)
        print(req)
        return req
       

setup(
    name='mlproject',
    version='0.0.1',
    author='Dev',
    author_email='devisriprasad948@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements( 'requirements.txt' )
)
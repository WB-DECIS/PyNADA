# PyNADA
A Python client for NADA API

## Setup
This library is currently under development. A pip installation is available through Test PyPI using:
 ```sh
pip install -i https://test.pypi.org/simple/ pynada
 ```

## Examples
Jupyter Notebooks under examples folder show some use cases utilizing PyNADA. The examples are grouped into three categories:
* Search Catalog: codes for finding specific datasets
    - search by partial id, partial title, ...
    - list all datasets
    
* Create Dataset: codes for adding datasets to the catalog
    - add survey, document, ... 
    
* Manage Catalog: codes for managing existing datasets and resources
    - delete dataset
    - upload thumbnail
    - ...
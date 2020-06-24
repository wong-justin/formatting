# formatting

Script to add docstrings to python files.

## Setup
- download `formatting.py`
- change AUTHOR var to your name
- create file called `.pth` in the site-packages dir, 
found by running `python -m site --user-site`
- add the dir containing this file to the .pth file

## Usage
`python -m formatting myfile.py` 

will create a new file `myfile_formatted.py` with docstrings inserted.
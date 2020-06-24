'''Script to add docstrings to python files.

Setup:
- create file called ".pth" in the site-packages dir, 
found by running "python -m site --user-site"
- add dir containing this file to the .pth file
Usage:
- run "python -m formatting myfile.py" and a new file will be created,
myfile_formatted.py with docstrings inserted.

Justin Wong
2020-06-23
'''

from datetime import datetime
import sys

INDENT_SIZE = 4
INDENT = ' ' * INDENT_SIZE
AUTHOR = 'Justin Wong'

def format_python(pyfile):
    '''Main method reads lines and creates docstrings for functions, classes.
    
    Params:
        pyfile - filepath of python file
    '''
    
    last = pyfile.rfind('.')
    newpath = pyfile[:last] + '_formatted' + pyfile[last:]
    with open(pyfile, 'r') as oldfile:
        with open(newpath, 'w') as newfile:
            
            newfile.write(top_doc())
            for line in oldfile.readlines():
                result_content = handle_new_line(line)  
                newfile.write(result_content)
    
def handle_new_line(line):
    '''Returns line(s) to write to new file, 
    adding docstrings if containing function or class.
    
    Params:
        line - line read from original file
    '''
    
    result = line

    first = line.lstrip().split(' ')[0]
                
    if first == 'def':
        result += function_doc(line)
    elif first == 'class':
        result += class_doc(line)
        
    return result
            
def top_doc():
    '''Docstring for top of module.'''
    
    today = datetime.now().strftime('%Y-%m-%d')
    s = f"""'''#TODO

{AUTHOR}
{today}
'''

"""
    return s

def function_doc(line):
    '''Docstring for a function. Short if no params. 
    
    Params:
        line - line containing function header.
    '''
    
    docstring = """'''#TODO'''
"""    
    args = get_args(line)
    if len(args) > 0:
        
        maxlen = len(max(args, key=lambda x: len(x))) + 1
        argstr = ''
        for a in args:
            numspaces = maxlen - len(a)
            argstr += INDENT + a + ' '*numspaces + '- \n' 
        
        docstring = f"""'''#TODO

Params:
{argstr}'''
"""
    docstring = indent(docstring, indent_depth(line) + 1)
    return docstring
    
def class_doc(line):
    '''Docstring for a class. Short.
    
    Params:
        line - line containing class header/definition.
    '''
    
    s = """'''#TODO'''
"""
    num_indents = indent_depth(line) + 1
    docstring = ''
    for result_line in s.split('\n'):
        docstring += INDENT * num_indents + result_line + '\n'
    return docstring

def get_args(line):
    '''Get args from function header.
    Ignores any default values and excludes 'self' param for class functions.
 
    Params:
        line - line containing function header
    '''
    
    argstr = line[line.index('(') + 1:
                  line.rindex(')')]
    chunks = argstr.split(',')
    args = []
    for a in chunks:
        if '=' in a:
            a = a[:a.index('=')]
        a = a.strip()    # in case spaces between comma separated args
        if len(a) > 0 and not a == 'self':
            args.append(a)
    return args

def indent(content, depth):
    '''Returns content indented by specified depth. 
    
    Params:
        content - text to indent; usually multiline
        depth   - num indents to prepend to each line
    '''
    
    indented = ''
    for line in content.split('\n'):
        indented += INDENT * depth + line + '\n'
    return indented

def indent_depth(line):
    '''Returns number of indents that a line starts with.
    INDENT_SIZE and corresdonding INDENT of spaces initialized at start of program.
    
    Params:
        line - any line
    '''
    
    depth = 0

    while line[:INDENT_SIZE] == INDENT:
        line = line[INDENT_SIZE:]
        depth += 1
    return depth

def rund_from_cmd_line():
    '''Runs main method, getting filepath from command line args.'''
    
    filepath = sys.argv[1]
    if filepath[-3:] == '.py':
        format_python(filepath)
    else:
        print('Error: not a .py file')
        
if __name__ == '__main__':
    rund_from_cmd_line()
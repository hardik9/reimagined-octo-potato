'''
creates folder for each filetype in current folder and moves files into their respective extension folder.
for example, all .doc files in folder will be moved in 'doc' subfolder. if 'doc' folder does not exist, it will be created.
'''

import os, glob

for file in glob.iglob('*.*'):
    name, ext = os.path.splitext(file)
    ext = str(ext)[1:]

    if file != __file__:
        if os.path.isdir(ext):
            pass
        else:
            os.mkdir(ext)
        
        os.rename(f'{file}', f'{ext}/{file}')

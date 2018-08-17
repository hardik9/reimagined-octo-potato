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

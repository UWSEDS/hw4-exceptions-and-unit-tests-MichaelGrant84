import os

def remove_data(URL):
    filename = URL.split('/')[-1]
    if os.path.exists(filename):
        os.remove(filename)
        return('File removed.')
    else:
        return('This file does not exist.')

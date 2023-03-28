import api

import zipfile

import os

TEMP_DIR = os.getenv('TEMP')
print(TEMP_DIR)

def download(name, parent_dir):
    zipname = TEMP_DIR + '\\' + name + '.zip'
    folder_path = parent_dir + '\\' + name
    api.download(release['zipball_url'], zipname)
    with zipfile.ZipFile(zipname, 'r') as zip_ref:
        zip_ref.extractall(folder_path)
    os.remove(zipname)
    
    sub_folder = os.listdir(folder_path)[0]
    for file in os.listdir(folder_path + '\\' + sub_folder):
        os.rename(folder_path + '\\' + sub_folder + '\\' + file, folder_path + '\\' + file)
    os.rmdir(folder_path + '\\' + sub_folder)




r = api.get_libs()
if r is not None:
    for lib in r:
        release = api.get_release(lib['name'])
        if release is not None:
            print(release['zipball_url'])
            download(lib['name'], 'D:\\clib-storage\\libraries\\installer\\test')
        else:
            print('Error: Could not get release for %s' % lib['name'])
else:
    print('Error: Could not get list of libraries')
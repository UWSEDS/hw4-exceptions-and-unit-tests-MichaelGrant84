import urllib3
import os
import certifi

def get_data(URL):
    filename = URL.split('/')[-1]
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED')

    if os.path.exists(filename):
        file_exist = True
        return('Looks like this file already exist.')
    else:
        try:
            r = http.request('GET', URL, preload_content = False)
            if r.status == 200:
                with open(filename, 'wb') as file:
                    file.write(r.data)
                    cwd = os.getcwd()
                    return('File downloaded.')
            else:
                return('Page or file does not exist.')
        except:
            return('Page or file does not exist.')
    http.clear()

# import
import os
import sys
import platform
import time
import shutil
import zipfile
import requests
import urllib3
import json
import wget

# define func
def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    for names in zip_file.namelist():
        zip_file.extract(names, 'update/')
    zip_file.close()

# initialize session
s = requests.session()
s.headers = {
    'Accept': 'application/vnd.github.v3+json'
}
urllib3.disable_warnings()

# initialize consts
github_release_api_url1 = 'https://api.github.com/repos/qhy040404/DLUT-library-auto-reservation/releases/latest'
github_release_api_url2 = 'https://api.github.com/repos/qhy040404/Library-reservation-configGenerator/releases/latest'
github_release_api_url3 = 'https://api.github.com/repos/qhy040404/Library-reservation-updater/releases/latest'

# delete old files
if os.path.exists('update'):
    shutil.rmtree('update')

# read config.json
with open("config.json","r") as conf:
    updateConf = json.load(conf)
    conf.close()

mainver = updateConf.get('main')
configGeneratorver = updateConf.get('configGenerator')
Updaterver = updateConf.get('Updater')

response1 = s.get(github_release_api_url1, verify = False).text.strip('[]')
remoteVer1 = json.loads(response1).get('tag_name')

response2 = s.get(github_release_api_url2, verify = False).text.strip('[]')
remoteVer2 = json.loads(response2).get('tag_name')

response3 = s.get(github_release_api_url3, verify = False).text.strip('[]')
remoteVer3 = json.loads(response3).get('tag_name')

# compare local and remote
if remoteVer1 == mainver and remoteVer2 == configGeneratorver and remoteVer3 == Updaterver:
    print('You have the latest release.')
    time.sleep(2)
    sys.exit()
else:
    print('One or more modules\' newer version has been released.')
    print()
    if remoteVer1 != mainver:
        print('New: main: ' + remoteVer1)
        print(json.loads(response1).get('body'))
        print('Usually the following updates are included in main update.')
        print()
    if remoteVer2 != configGeneratorver:
        print('New: configGenerator: ' + remoteVer2)
        print(json.loads(response2).get('body'))
        print()
    if remoteVer3 != Updaterver:
        print('New: Updater: ' + remoteVer3)
        print(json.loads(response3).get('body'))
        print()

    updateChoice = input('Update?(Y/N)')
    if updateChoice == 'Y' or updateChoice == 'y':
        os.mkdir('update')
        if updateConf.has_key('channel'):
            updateConf.pop('channel')
        updateConf.update(main = remoteVer1, configGenerator = remoteVer2, Updater = remoteVer3)
    else:
        sys.exit()

    if platform.system() == 'Windows':
        sysType = 'win'
    elif platform.system() == 'Linux':
        sysType = 'linux'
    elif platform.system() == 'Darwin':
        sysType = 'osx'
    else:
        print('Unknown system')

    if remoteVer1 != mainver:
        download_url = 'https://github.com/qhy040404/DLUT-library-auto-reservation/releases/download/' + remoteVer1 + '/Library-' + sysType + '.zip'
        path = 'temp.zip'
        try:
            wget.download(download_url, path)
        except Exception as e:
            print('Error')
            print(e)
            sys.exit()
    else:
        if remoteVer2 != configGeneratorver:
            download_url = 'https://github.com/qhy040404/Library-reservation-configGenerator/releases/download/' + remoteVer2 + '/ConfigGenerator-' + sysType + '.zip'
            path = 'temp.zip'
            try:
                wget.download(download_url, path)
            except Exception as e:
                print('Error')
                print(e)
                sys.exit()
        if remoteVer3 != Updaterver:
            download_url = 'https://github.com/qhy040404/Library-reservation-updater/releases/download/' + remoteVer3 + '/Updater-' + sysType + '.zip'
            path = 'temp.zip'
            try:
                wget.download(download_url, path)
            except Exception as e:
                print('Error')
                print(e)
                sys.exit()


    un_zip('temp.zip')
    if os.path.exists('update/config.conf'):
        os.remove('update/config.conf')
    if os.path.exists('update/config.json'):
        os.remove('update/config.json')
    with open("update/config.json","w") as conf:
        json.dump(updateConf, conf)

    print()

    if sysType == 'win':
        os.system('start update.bat')
    elif sysType == 'linux' or sysType == 'osx':
        os.system('sh update.sh')
    sys.exit()
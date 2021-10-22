#!/usr/bin/env python3

import requests

url = input('paste your music url: ')

music_name = url.rsplit('/', 1)[-1]
print('name:', music_name)

dl_link = f'https://host2.rj-mw1.com/media/mp3/mp3-256/{music_name}.mp3'
print(dl_link)

try:
    r = requests.get(dl_link)

    with open(music_name + '.mp3','wb') as output_file:
        output_file.write(r.content)
        
    print('Download Completed.')
except:
    print('something crash in the way!!!')
#change url endpoint to '.zip' to download zip
#extract it to folder named 'channel', read 'readme.txt'

import os
import zipfile

start = '90052'
archive = zipfile.ZipFile('channel.zip','r')
files = []

while True:
    try:
        with open('channel\\'+start+'.txt','rt') as f:
            data = f.read()
    except:
        break
    files.append(start)
    start = data.split()[-1]

#collect comments.

for file in files:
    cmt = archive.getinfo(f'{file}.txt').comment.decode('utf-8')
    print(cmt,end="")
#Look closer and you`ll get 'oxygen'
#answer = oxygen

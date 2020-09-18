#the strings given in source code are compressed strings with bz2
#click on the image, get redirected to login field, enter username and password.

import bz2

str1 = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
str2 = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

username = bz2.decompress(str1).decode('utf-8')
password = bz2.decompress(str2).decode('utf-8')

print(f'username: {username}')
print(f'password: {password}')

#answer is 'huge' and and 'file'
#link to next problem: http://www.pythonchallenge.com/pc/return/good.html

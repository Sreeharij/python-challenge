#get cookies by developer_tools>applications>cookies
#it asks us to follow busynothing.
#go back to challenge number 4 and follow chain with 'busynothing'
#link:- http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345

import requests
import pickle
import bz2
from urllib.parse import unquote_plus,unquote_to_bytes
string=""

end = '12345'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='

while True:
    response = requests.get(url+end)
    print(response.text,end=" ")
    cookie = response.cookies['info']
    string += cookie
    end = response.text.split()[-1]
    print(cookie,flush=True)
    try:
        int(end)
    except:
        break

#The cookies string would contain a "+"

string = string.replace("+","%20")
new = unquote_to_bytes(string)
print(bz2.decompress(new))

#26th is related to Mozart`s Bday. His father is being referred.
#call his father ('Leopold') using xmlrpc from previous question.(you will be redirected to violin.php)
#http://www.pythonchallenge.com/pc/stuff/violin.php
#send over the data as cookies.

data = "the flowers are on their way"
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
body = {'info':data}
print(requests.post(url,cookies=body).text)

#answer is 'balloons'
#link to next problem: http://www.pythonchallenge.com/pc/return/balloons.html




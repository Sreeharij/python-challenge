import requests

end = '12345'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

#run once. divide by 2. set end=value//2. run again.

while True:
    obj = requests.get(url+end).text
    end = obj.split()[-1]
    print(obj,end,flush=True)
    try:
        int(end)
    except e:
        break

#answer = peak

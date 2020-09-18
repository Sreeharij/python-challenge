#there are 4 pictures which we need to intuitively get from the server.
#evil1.jpg evil2.jpg evil3.jpg evil4.jpg
#if you cannot dont see anything in evil4.jpg, open command prompt and type
#'curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg'
#and it would display 'bert is evil, go back.'
#evil2.jpg tells us to change extension to '.gfx' and obtain another file

import numpy as np

with open('evil2.gfx','rb') as f:
    data = f.read()

#A person is seen dealing cards to 5 stacks. Open evil2.gfx. the length of the
#data will be multiple of 5. we need to split each byte and create 5 new images out of it.

for i in range(5):
    with open(f'ans{i+1}.jpg','wb') as f:
        f.write(data[i::5])

#combining answers from the 5 newly created images.
#answer is disproportional

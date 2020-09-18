#phonebook.php tells us that an xml error occured
#that means,we need to interact with that php file
#we require xmlrpc module to do this

import xmlrpc.client
server = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(server.system.listMethods())

#we need to call the phone() method and pass 'Bert' to it since 'Bert is evil'(from a previous level)
print(server.phone('Bert'))

#Anser = Italy

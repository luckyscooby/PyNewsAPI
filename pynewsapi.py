# PyNewsAPI
# Michael Leocádio @ 2023
# This is a very simple demontration on the use of NewsAPI use in Python.
# It receives a query as user input and then presents 3 results (if found).


import requests
import json
import os
from termcolor import cprint

url = ('https://newsapi.org/v2/')
endpoint = 'everything'
sortBy = 'popularity'
apiKey = '6fdd5b8513484c14bd2709d61a3d4969'

if os.name == 'posix':
	os.system('clear')
else:
	os.system('cls')
     
cprint('The NewsAPI Times', 'blue', 'on_yellow', attrs=['bold'])
query = input('Search for article(s): ')
cprint('Please, wait...', 'light_grey')

response = json.loads(requests.get(url + endpoint + '?q=' + query + '&sortBy=' + sortBy + '&apiKey=' + apiKey).text)

if response['status'] == 'ok':
    if response['totalResults'] > 0:
        cprint('Showing 3 of ' + str(response['totalResults']) + ' results:\n', 'green')
        i = 0
        for article in response['articles']:
            if i > 2:
                break
            i += 1
            cprint(article['title'], 'blue', attrs=['underline'])
            cprint(article['description'])
            cprint('\t' + article['author'] + '\n', 'yellow')
    else:
        cprint('No results found.', 'yellow')
else:
    cprint('Error; Check our connection and try again.', 'red')
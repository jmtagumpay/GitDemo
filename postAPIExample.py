import requests
import json
from payLoad import *
import configparser
from utilities.configurations import *
from utilities.resources import *

# original code
# addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php', json=addBookPayload("random"),
#                                  headers={"Content-Type": "application/json"}, )

# when using configparser
# import configparser
# config = configparser.ConfigParser()
# config.read('utilities/properties.ini')
# addBook_response = requests.post(config['API']['endpoint']+'/Library/Addbook.php', json=addBookPayload("random"),
#                                  headers={"Content-Type": "application/json"}, )

# using configparser from def function
# from utilities.configurations import *
# addBook_response = requests.post(getConfig()['API']['endpoint'] + '/Library/Addbook.php',
#           json=addBookPayload("random"), headers={"Content-Type": "application/json"}, )

# using class for resources
# from utilities.resources import *
urladd = getConfig()['API']['endpoint'] + ApiResources.addBook
header = {"Content-Type": "application/json"}
addBook_response = requests.post(urladd, json=addBookPayload("random"), headers=header, )

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)

# Delete Book

# original code
# response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
#
#     "ID": bookId
# }, headers={"Content-Type": "application/json"}, )
#
# assert response_deleteBook.status_code == 200
# res_json = response_deleteBook.json()
#
# print(res_json["msg"])
#
# assert res_json["msg"] == "book is successfully deleted"


urldel = getConfig()['API']['endpoint'] + ApiResources.deleteBook
# header is called at the top
response_deleteBook = requests.post(urldel, json={"ID": bookId}, headers=header, )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])

assert res_json["msg"] == "book is successfully deleted"

# Authentication
# url = "https://api.github.com/user"
# github_response = requests.get(url, headers= {'Authorization':'Bearer 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'})
# # since github has new implementation that requires tokens, instead of username and passwords
# print(github_response.json())
# print(github_response.status_code)

# nasa video ni rahul shetty
url = "https://api.github.com/user"
github_response = requests.get(url, auth=('jmtagumpay', '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'))
print(github_response.json())
print(github_response.status_code)

# Session Manager - use of auth function on requests library to remove redundancy on code
se = requests.session()
se.auth = auth = ('jmtagumpay', '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')

url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response.json())
print(response.status_code)

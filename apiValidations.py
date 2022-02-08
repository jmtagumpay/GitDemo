import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName':'Miggy'},)

# get response in str format via .text, convert str to list via json.loads, then get value of isbn in list
print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(type(dict_response))
# print(dict_response[0]['isbn'])

# shortcut to get response in str format to list via response.json()
json_response = response.json()
# print(type(json_response))
# print(json_response[0]['isbn'])
# print(response.status_code)
# assert response.status_code == 200
# print(response.headers)
# assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve the book details with ISBN RGHCC
for actualBook in json_response:
    if actualBook['aisle'] == '6969':
        print(actualBook)
        # print(type(actualBook))
        # actualBook_comp = actualBook
        break
print(json_response)
print(actualBook)


# expectedBook = {'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '99755'}
# print(type(expectedBook))
#
# assert actualBook == expectedBook
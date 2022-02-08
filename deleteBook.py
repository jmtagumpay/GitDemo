import requests
import json

response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php',
                                    json={"ID":"qwerty6969"},
                                    headers={"Content-Type":"application/json"},)
print(response_deleteBook.json())
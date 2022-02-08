# Implementing Hooks

import requests


def after_scenario(context, scenario):
    if 'library' in scenario.tags:  # execute only when scenario is tagged as 'library', lesson 58
        response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

            "ID": context.bookid
        }, headers={"Content-Type": "application/json"}, )

        assert response_deleteBook.status_code == 200
        res_json = response_deleteBook.json()

        print(res_json["msg"])

        assert res_json["msg"] == "book is successfully deleted"

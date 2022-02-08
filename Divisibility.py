
# i = 1000000
# while i != 1000000000:
#     i += 1
#     if (i % 17) == 0:
#         print(i)

def step_impl(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()
    print(type(response_json))
    bookId = response_json['ID']
    print(bookId)
    assert response_json['Msg'] == "successfully added"

import json

courses = '{"name": "RahulShetty", "languages":["Java","Python"]}'

dict_courses = json.loads(courses)
print(type(dict_courses))           #dict
print(dict_courses)                 #{"name":"RahulShetty", "languages"["Java","Python"]}
print(dict_courses['name'])         #RahulShetty


# list_language = dict_courses['languages']   #["Java","Python"]
# print(type(list_language))          #list
# print(list_language[0])             #Java
#
print(dict_courses['languages'][0]) #Java
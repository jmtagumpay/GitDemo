import requests

# http://rahulshettyacademy.com
# 'visit-month' - cookie

# Session Manager on using cookies
cookie = {'visit-month': 'February'}
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)
# 301 - response before redirection, 200 - final status code
print(response.history)
print(response.status_code)

se = requests.session()
se.cookies.update({'visit-month': 'February'}) # needs to have 'update' text after cookies

# if there's no cookies here, cookies on the 'se.cookies.update' will be shown only
res = se.get('https://httpbin.org/cookies',cookies={'visit-year': '2022'})
print(res.text)


# Attachments
url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
files = {'file': open('/Users/joset/Documents/TestProject Files/Heart Button Screenshot/likebutton.jpg', 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)



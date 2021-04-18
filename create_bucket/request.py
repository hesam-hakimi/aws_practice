import requests

# get request
payload = {'page': 2, 'count': 25}
r = requests.get("https://httpbin.org/get", params=payload)
print(r.ok)
print(r.status_code)
print(r.headers)
print(r.text)
print(r.url)

# post request
payload = {'username': 'hesam', 'password': 'test'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.ok)
print(r.status_code)
print(r.headers)
print(r.text)
print(r.url)
print(r.json()['form '])


r = requests.get("https://httpbin.org/basic-auth/corey/testing",
                 auth=('corey', 'testing'))
print(r.ok)
print(r.status_code)

print(r.headers)
print(r.text)
print(r.url)
print(r.json()['form '])


param = {"username": "corey", "password": "testing"}
r = requests.post("https://httpbin.org/post/", data=param)

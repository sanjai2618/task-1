import requests

a=str(input('paste the url here:'))
response = requests.get(a)
i=response.status_code

if i==200:
    print("")
    print("")
    print('connection made successfully')
    print("")
    print("")
    c= response.text
    print(c)
    print("")
    print("")
    print("")
    print("")
    g=response.headers
    print(g)
    
else:
    print('unsuccessful connection')
    

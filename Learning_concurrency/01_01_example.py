import requests

resonse = requests.get('https://www.example.com')

items = resonse.headers.items()

header = [f'{key} : {header}' for key, header in items]

formatted_header = '\n'.join(header)

print(formatted_header)

with open('header.txt','w') as file:
    file.write(formatted_header)
import requests
from bs4 import BeautifulSoup

url = r'https://www.bbc.co.uk/news'
r   = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
results = [i.text for i in soup.find_all('title')]
title = results[0]
print(title)

# build a new project dir
# git init 
# build a new github repo
# hook up travis to your git repo
# git remote add origin url_goes_here!!!
# .gitignore with venv
# pip freeze to build a requirements.txt
# build the dockerfile
# build the .travis.yml file
# git push etc
# test it - see travis build succeed 
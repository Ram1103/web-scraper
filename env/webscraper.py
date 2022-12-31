import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


driver =  webdriver.Chrome(executable_path="C:/Users/Ram/OneDrive/Desktop/webscraper/env/chromedriver.exe")
driver.get('https://medium.com/')

results = []
content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
driver.quit()

for element in soup.findAll(attrs='mu mv mw mx my mz s na'):
    name=element.find('h2')
    if name not in results:
        results.append(name.text)
print(results)        
df = pd.DataFrame({'Names':results})
df.to_csv('names.csv',index=False,encoding='utf-8')


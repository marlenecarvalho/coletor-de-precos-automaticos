# entrar no site 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

# abrir o navegador
driver = webdriver.Chrome()
driver.get('https://praso.com.br/departments/Latic%C3%ADnios%20Secos')
sleep(5)

# pegar os produtos
produtos = driver.find_elements(By.XPATH, '//*[@class="line-clamp-3 text-sm text-gray-950"]')

preços = driver.find_elements(By.XPATH, '//*[@class="font-semibold text-green-800 text-sm"]')

# salvar os produtos e preços em arquivo csv    
for produto, preço in zip(produtos, preços):
    with open('produtos.csv', 'a' , encoding='utf-8') as arquivo:
        arquivo.write(f'{produto.text},{preço.text}{os.linesep}')

             
input('')
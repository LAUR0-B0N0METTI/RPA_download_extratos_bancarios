import time
import calendar
from time import sleep
import datetime as dtm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pyautogui as pg
import pandas as pd
import os 

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--start-maximized')
options.add_argument('--start-fullscreen')
options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("disable-infobars")
options.add_experimental_option("detach", True)


driver = webdriver.Chrome("chromedriver", options=options)

driver.get('https://www.itau.com.br')


driver.find_element(By.ID, "open_modal").click()

pg.hotkey('tab')
pg.hotkey('down')
pg.hotkey('tab')
pg.hotkey('enter')

driver.implicitly_wait(1)
pg.write("**********")
pg.hotkey('enter')
driver.implicitly_wait(1)

driver.implicitly_wait(10)

senha = driver.find_element(By.PARTIAL_LINK_TEXT, "X" or "ou X" or "X ou")
senha.click()

driver.implicitly_wait(1.5)
senha = driver.find_element(By.PARTIAL_LINK_TEXT, "X" or "ou X" or "X ou")
senha.click()

driver.implicitly_wait(1.5)
senha = driver.find_element(By.PARTIAL_LINK_TEXT, "X" or "ou X" or "X ou")
senha.click()

driver.implicitly_wait(1.5)
senha = driver.find_element(By.PARTIAL_LINK_TEXT, "X" or "ou X" or "X ou")
senha.click()

driver.implicitly_wait(1.5)
senha = driver.find_element(By.PARTIAL_LINK_TEXT, "X" or "ou X" or "X ou")
senha.click()

driver.implicitly_wait(1.5)
senha = driver.find_element(By.PARTIAL_LINK_TEXT, "X" or "ou X" or "X ou")
senha.click()

driver.implicitly_wait(1.5)
senha = driver.find_element(By.PARTIAL_LINK_TEXT, "acessar")
senha.click()

driver.implicitly_wait(500)
acessoBasico = driver.find_element(By.ID, "rdBasico")
time.sleep(2)
acessoBasico.click()
acessoBasico = driver.find_element(By.ID, "btn-continuar")
acessoBasico.click()
time.sleep(10)
pg.hotkey('tab')
pg.hotkey('enter')


lendoExcel = pd.read_excel('C:\\Users\\robo.rpa\02 - Processos\\ID-0001\\04 - Insumos\\Banco de Dados Conciliacao\\base.xlsx', converters={'conta': str})
baseDeDados = lendoExcel[['conta']]


for contaBancaria in baseDeDados['conta'][0:]:    
    
    if contaBancaria == pd.isnull(contaBancaria):
        time.sleep(1)
        
    else:
    
        pg.moveTo(1000, 30)
        pg.click()

        time.sleep(1)
        pg.click()
        pg.hotkey('tab')
        pg.hotkey('tab')    
        time.sleep(0.5)
        pg.write(contaBancaria)

        time.sleep(2)
        driver.implicitly_wait(5)
        clickConta = driver.find_element(By.TAG_NAME, "td")
        clickConta.click()

        time.sleep(6)
        driver.find_element(By.ID, "botao-buscar-ni").click()

        time.sleep(1.5)
        pg.write("Extrato por periodo")
        time.sleep(1)
        pg.hotkey('enter')

        time.sleep(3)
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Extrato por período da conta corrente').click()
        
        data = dtm.datetime.now()
        mes = str(int(data.month))
        ano = str(data.year)
        

        if mes == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            mes = str(int(data.month))
        else:
            if mes == 10 or 11 or 12:
                mes = str(int(data.month))

        time.sleep(4)
        pg.click('clickData.PNG')
        driver.implicitly_wait(50)
        pg.hotkey('tab')
        pg.write('01')

        time.sleep(1)
        
        pg.write(mes)

        pg.write(ano)

        for i  in range(6):
            pg.hotkey('tab')
        pg.hotkey('enter')
            
        time.sleep(4)
        pg.hotkey('end')
        
        if not os.path.exists('C:\\Users\\robo.rpa\\RPA SALVAR EXTRATOS\\ITAU\\'+ ano +'\\' + mes):
            os.makedirs('C:\\Users\\robo.rpa\\RPA SALVAR EXTRATOS\\ITAU\\'+ ano +'\\' + mes)
        
            pg.click('salvarExcel.PNG')
            time.sleep(2)
            driver.implicitly_wait(60)
            pg.write('C:\\Users\\robo.rpa\\RPA SALVAR EXTRATOS\\'+ ano +'\\ITAU\\' + mes + '\\' + contaBancaria)
            pg.hotkey('enter')
            
            time.sleep(0.5)
            pg.moveTo(60, 600)
            pg.click()
            pg.hotkey('left')
            pg.hotkey('enter')
            
            time.sleep(1)
            pg.moveTo(40, 110)
            pg.click()
            
            time.sleep(4)
            
        else:
            
            pg.click('salvarExcel.PNG')
            time.sleep(2)
            driver.implicitly_wait(60)
            pg.write('C:\\Users\\robo.rpa\\RPA SALVAR EXTRATOS\\ITAU\\'+ ano +'\\' + mes + '\\' + contaBancaria)
            pg.hotkey('enter')
            
            time.sleep(0.5)
            pg.moveTo(60, 600)
            pg.click()
            pg.hotkey('left')
            pg.hotkey('enter')
            
            time.sleep(1)
            pg.moveTo(40, 110)
            pg.click()
            
            time.sleep(4)

driver.close()
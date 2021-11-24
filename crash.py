drop database crash;
create database crash;
use crash;

create table preco(
valor float
);

SELECT * FROM preco;



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


import pymysql
import time
from datetime import datetime

def setValor(valor, tempo):
    global conexao
    global cursor
    cursor.execute("INSERT INTO preco VALUES (" + str(valor) + ")")
    conexao.commit()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://blaze.com/pt/games/crash')
conexao = pymysql.connect(db='crash', user='root', passwd='root')
cursor = conexao.cursor()
aux = None
r = None
time.sleep(5)



def db():
    global driver
    global aux
    while True:
        try:
            valor = []
            for k in driver.find_element_by_class_name("crash-previous").find_elements_by_tag_name("span"):
                try:
                    valor.append(float(k.text.split("X")[0]))
                except:
                    continue
            tempo = datetime.now()
            if(len(valor) > 0 and aux != valor[0]):
                aux = valor[0]
                setValor(valor[0],tempo)
        except:
            print(valor)
            print("Error!")
            conexao = pymysql.connect(db='crash', user='root', passwd='root')
            cursor = conexao.cursor()

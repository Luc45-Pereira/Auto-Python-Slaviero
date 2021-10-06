#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Parte para entrar na aba perguntas

#imprta slenium para abrir navegador
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#possiveis perg
posi = ['serve', 'funciona', 'funcionaria', 'encaixa']

#abre navegador
navegador = webdriver.Chrome()

#vai no site do mercado livre
navegador.get("https://www.mercadolivre.com/jms/mlb/lgz/msl/login/H4sIAAAAAAAEAzXOwQrDIBAE0H-ZsyR3j_2RsDGrkWqVdVNbQv692NLjwPBmTqQS4mPRd2VY8Kum6KLCoCZSXyQvcYNFTjBoUfkf11EhoczK0mDPAQXebuyLDErlYBjQofviU-mwvykYhAKLXbU2O8-99ymzONpKik_hyZU8rTLDQDjEpiw8Hny9y8BT00WF3B3WU2p8fQC9dzgpxAAAAA/user")

#espera 5min
navegador.implicitly_wait(300)

#clica no menu
navegador.find_element_by_xpath('//*[@id="nav-header-menu"]/div').click()

#entra em perguntas
navegador.find_element_by_xpath('//*[@id="nav-header-menu"]/div/nav/div[1]/div[2]/a[2]').click()
navegador.find_element_by_xpath('//*[@id="root-app"]/div/div/div[1]/nav/div/div/div[1]/section[2]/div[1]/span/div/label').click()
navegador.find_element_by_xpath('//*[@id="seller_questions"]').click()

#pega quantas pergutas tem
name = navegador.find_element_by_xpath('//*[@id="page"]/div[4]/div[3]/div').text
n = re.sub('[^0-9]', '', name)
print(name)
navegador.find_element_by_xpath('/html/body/div[9]/div[1]/div/div[2]/button').click()

#verifica se existem perguntas
for perg in range(int(name)):
    f = perg + 1
    
    #cria variavel num
    num = 0
    
    #pega o codigo da peca
    cod = navegador.find_element_by_xpath('//*[@id="page"]/div[5]/div/div[1]/div/div[1]/div[2]/div[1]/a').text
    cod = cod.split()
    
    #verifica se perg é maior que 0
    if(perg > 0):
        
        #concatena elemento XPATH
        per1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["
        
        per2 = "]/div[3]/div[2]"
        
        abrir = per1 + str(f) + per2
        
        print(abrir)
        
        ab = navegador.find_element(By.XPATH, abrir)
        
        navegador.execute_script("arguments[0].click();", ab)

    #concatena elemento XPATH
    per1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["
    
    per2 = "]/div[3]/div[1]/div[2]/span[2]/span[1]"
    
    pergunta = per1+str(f)+per2
    
    print(pergunta)
    
    #pega a pergunta
    n = navegador.find_element_by_xpath(pergunta).text
    print("pegou pergunta")
    
    #converte string em lista
    n = n.split()
    print(n)
    
    #variavel para saber se encontrou o chassi
    cha = "n"
    
    #loop enquanto tiver elementos na lista
    for i in range(len(n)):
        
        print("procurando chassi")
        
        #se per[i] for igual a "chassi"
        if(n[i]=="chassi" or n[i]=="Chassi"):
            
            #variavel para saber se encontrou o chassi
            cha = "achei"
            
            #coloca i+1 na variavel num
            num = i+1
            print(n[i+1])
            
            #abre nova janela com o catalogo
            nav = webdriver.Chrome()
            nav.get("https://fordcatalog.com/")
            
            #espera até que carregue por completo
            WebDriverWait(nav, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content1")))
            
            #seleciona o frame da tela
            frame = nav.find_element(By.CSS_SELECTOR, '#content1')
            
            #entra no frame
            nav.switch_to_frame(frame)
            nav.implicitly_wait(20)
            
            #encontra a barra de usuario e digita o usuario
            nav.find_element(By.CSS_SELECTOR, '#edtUsuario').send_keys("1289_lucas")
            
            #encontra a barra de senha e digita a senha
            nav.implicitly_wait(20)
            nav.find_element(By.CSS_SELECTOR, '#edtSenha').send_keys("0481b29")
            
            #clica em entrar
            nav.implicitly_wait(20)
            nav.find_element(By.CSS_SELECTOR, '#btLogin_text').click()
            
            #volta para o frame inicial
            nav.switch_to.parent_frame()
            
            #aguarda 20 seg
            nav.implicitly_wait(20)
            
            #busca proximo frame
            WebDriverWait(nav, 21).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content2")))
            
            #seleciona o frame da tela
            frame = nav.find_element(By.CSS_SELECTOR, '#content2')
            
            #entra no frame
            nav.switch_to_frame(frame)
            
            #digita o chassi do veiculo
            nav.find_element(By.CSS_SELECTOR, '#editChassi').send_keys(n[num])
            
            #clica em pesquisar
            nav.find_element(By.CSS_SELECTOR, '#btChassi_text').click()
            
            #volta para o frame inicial
            nav.switch_to.parent_frame()
            
            #busca proximo frame
            WebDriverWait(nav, 21).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#popContentFrame0")))
            
            #seleciona o frame da tela
            frame = nav.find_element(By.CSS_SELECTOR, '#popContentFrame0')
            
            #entra no frame
            nav.switch_to_frame(frame)
            
            #clica em navegar com VIN
            nav.find_element(By.CSS_SELECTOR, '#btAvancarPesq_text').click()
            
            #volta para o frame inicial
            nav.switch_to.parent_frame()
            
            #busca proximo frame
            WebDriverWait(nav, 21).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content3")))
            
            #seleciona o frame da tela
            frame = nav.find_element(By.CSS_SELECTOR, '#content3')
            
            #entra no frame
            nav.switch_to_frame(frame)
            
            #pesquisa codigo da peca
            nav.find_element(By.XPATH, '//*[@id="editBusca"]').send_keys(cod[1])
            
            #clica em pesquisar
            nav.find_element(By.XPATH, '//*[@id="btBuscar_text"]').click()
            
            ser = nav.find_element(By.XPATH, '//*[@id="titResultados_text"]').text
            ser = re.sub('[^0-9]', '', name)
            
            #verifica se a peca serve no carro
            if(int(ser)>0):
                #Reponde o Cliente
                navegador.find_element(By.XPATH, '//*[@id="page"]/div[5]/div/div[2]/ul/li[2]/div[3]/div[2]/div[1]/label/div[1]/textarea').send_keys("Olá, Serve sim, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                navegador.find_element(By.XPATH, '//*[@id="page"]/div[5]/div/div[2]/ul/li[2]/div[3]/div[2]/div[2]/button').click()
            else:
                #Reponde o Cliente
                navegador.find_element(By.XPATH, '//*[@id="page"]/div[5]/div/div[2]/ul/li[2]/div[3]/div[2]/div[1]/label/div[1]/textarea').send_keys("Olá, infelismente não serve, dê mais uma olhada em nossa loja tenho certeza que encontrará o que procura, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                navegador.find_element(By.XPATH, '//*[@id="page"]/div[5]/div/div[2]/ul/li[2]/div[3]/div[2]/div[2]/button').click()
    
    #verifica se foi encontrado a palavra chassi
    if(cha == "achei"):
        
        #se não foi encontrado inicia loop enquanto tiver elementos na lista
        for i in range(len(n)):
            
            #verifica se existe as palavras contidas na lista posi
            if (n[i] == posi[n] or n[i] == posi[n+1] or n[i] == posi[n+2] or n[i] == posi[n+3]):
                
                #Reponde o Cliente
                navegador.find_element(By.XPATH, '//*[@id="page"]/div[5]/div/div[2]/ul/li[2]/div[3]/div[2]/div[1]/label/div[1]/textarea').send_keys("Olá, poderi me enviar o chassi de seu veículo da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                navegador.find_element(By.XPATH, '//*[@id="page"]/div[5]/div/div[2]/ul/li[2]/div[3]/div[2]/div[2]/button').click()
            
    
    



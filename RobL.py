# Dev: Lucas Pereira de Lima
# Data de desenvolvimento: outubro de 2021
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sistema de automação de respostas do mercado livre para a empresa Ford Slaviero

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNÇÕES:
def PegaPergunta(numerodapergunta, quantidade, respondido, aux_code):
    try:
        if(numerodapergunta >= 1 and quantidade > 0):

            if(numerodapergunta > 1 and quantidade > 1):

                #--------------------------------------------------------------------------------------------------------------------------------------------
                    try:

                        #concatenates XPATH element so that it takes an element from the question list
                        xpath1 = "//*[@id='page']/div[5]/div["
                        xpath2 = str(xpath1) + str(aux_code) + ']/div[2]/ul/li['

                        xpath1 = "]/div[3]/div[2]"

                        xpath_full = xpath2 + str(numerodapergunta) + xpath1

                        #select element
                        aux = browser1.find_element(By.XPATH, xpath_full)

                        #click in element
                        browser1.execute_script("arguments[0].click();", aux)

                    except:
                        print('Não foi possível selecionar a pergunta ' + aux3)

            elif(numerodapergunta == 1 and respondido == True):

                #--------------------------------------------------------------------------------------------------------------------------------------------
                    try:

                        #concatenates XPATH element so that it takes an element from the question list
                        xpath1 = "//*[@id='page']/div[5]/div["
                        xpath2 = str(xpath1) + str(aux_code) + ']/div[2]/ul/li['

                        xpath1 = "]/div[3]/div[2]"

                        xpath_full = xpath2 + str(numerodapergunta) + xpath1

                        #select element
                        aux = browser1.find_element(By.XPATH, xpath_full)

                        #click in element
                        browser1.execute_script("arguments[0].click();", aux)
                    except:

                        print('Não foi possível selecionar a pergunta ' + aux3)

            if(quantidade == 1 and numerodapergunta == 1):
                #concatenates XPATH element so that it takes an element from the question list
                xpath1 = "//*[@id='page']/div[5]/div[1]/div[2]/ul/li"

                xpath2 = "/div[3]/div[1]/div[2]/span[2]/span[1]"

                xpath_full = xpath1 + xpath2

            elif(quantidade > 1 and numerodapergunta >= 1):
                #concatenates XPATH element so that it takes an element from the question list
                xpath1 = "//*[@id='page']/div[5]/div["
                xpath2 = str(xpath1) + str(aux_code) + ']/div[2]/ul/li['

                xpath1 = "]/div[3]/div[1]/div[2]/span[2]/span[1]"

                xpath_full = xpath2 + str(numerodapergunta) + xpath1

            #--------------------------------------------------------------------------------------------------------------------------------------------
            try:
                #get question
                aux_question = browser1.find_element_by_xpath(xpath_full).text
                return(aux_question)

            except:
                erro = 'Não foi possível pegar a pergunta'
                return(erro)

            #--------------------------------------------------------------------------------------------------------------------------------------------
        else:
            return(False)
    except:
        return('erro')

    
def Resposta(pergunta, numerodapergunta, qtd, code, aux_code):
    questions = "serve funciona funcionaria encaixa"
    questions = questions.split()
    for i in range(len(pergunta)):
        
        #check if aux_question like chassi
        if(pergunta[i] == "chassi" or pergunta[i] == "Chassi"):
            #variable to know if it found the chassi
            chassi = 'yes'

            #insert i+1 in num
            num = i+1
            #----------------------------------------------------------------------------------------------------------
            try:
                #enter the catalog
                browser2.get("https://fordcatalog.com/")

                #wait new frame
                WebDriverWait(browser2, 10000).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content1')))

                #select frame in window
                frame = browser2.find_element(By.CSS_SELECTOR, '#content1')

                #into the frame
                browser2.switch_to.frame(frame)
                browser2.implicitly_wait(20)


                #select input usuario and insert user
                browser2.find_element(By.CSS_SELECTOR, '#edtUsuario').send_keys("1289_lucas")

                #select input senha and insert pass
                browser2.find_element(By.CSS_SELECTOR, '#edtSenha').click()
                browser2.implicitly_wait(21)
                browser2.find_element(By.CSS_SELECTOR, '#edtSenha').send_keys("0481b29")

                #click in button
                browser2.implicitly_wait(20)
                browser2.find_element(By.CSS_SELECTOR, '#edtSenha').send_keys(Keys.ENTER)

                browser2.implicitly_wait(20)
                #return for frame principal
                browser2.switch_to.parent_frame()

            except:
                print('Atenção: Ocorreu um erro ao fazer login no catálogo.')
            #----------------------------------------------------------------------------------------------------------

            #----------------------------------------------------------------------------------------------------------
            try:
                #wait 20 seg
                browser2.implicitly_wait(20)

                #wait new frame
                WebDriverWait(browser2, 10000).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content2')))

                #select frame
                frame = browser2.find_element(By.CSS_SELECTOR, '#content2')

                #into the frame
                browser2.switch_to.frame(frame)

                #search chassi
                browser2.find_element(By.CSS_SELECTOR, '#editChassi').send_keys(pergunta[num])
                browser2.implicitly_wait(10)

                #click in pesquisar
                browser2.find_element(By.CSS_SELECTOR, '#editChassi').send_keys(Keys.ENTER)

                #return for frame principal
                browser2.switch_to.parent_frame()
            except:
                print('Atenção: ocorreu um erro ao tentar pesquisar o chassi')
            #----------------------------------------------------------------------------------------------------------

            #----------------------------------------------------------------------------------------------------------
            try:
                #wait 10 seg
                browser2.implicitly_wait(10)

                #wait new frame
                WebDriverWait(browser2, 10000).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#popContentFrame0')))

                #select frame
                frame = browser2.find_element(By.CSS_SELECTOR, '#popContentFrame0')

                #into the frame
                browser2.switch_to.frame(frame)

                #click in browse with VIN
                browser2.find_element(By.CSS_SELECTOR, '#btAvancarPesq_text').click()

                #return for frame principal
                browser2.switch_to.parent_frame()
            except:

                if(int(qtd) == 1):

                    #concatenates element XPATHS
                    xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li"

                    xpath2 = "/div[3]/div[2]/div[1]/label/div[1]/textarea"

                    xpath_full = xpath1 + xpath2

                    btn1 = "//*[@id='page']/div[5]/div["
                    btn2 = str(btn1) + str(aux_code) + ']/div[2]/ul/li['

                    btn1 = "]/div[3]/div[2]/div[2]/button"

                    full_xpathBtn = btn2 + btn1

                    #----------------------------------------------------------------------------------------------------------
                    #answers the client
                    browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, não foi possível verificar com este chassi, poderia nos enviar o chassi de seu veículo novamente da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")

                    aux = browser1.find_element(By.XPATH, full_xpathBtn)

                    browser1.execute_script("arguments[0].click();", aux)
                    aux1 = 0
                    print("1-Olá, poderia me enviar o chassi de seu veículo da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                    browser2.refresh()
                    respondido = True
                    return(respondido)

                    #----------------------------------------------------------------------------------------------------------

                else:

                    #concatenates element XPATHS
                    xpath1 = "//*[@id='page']/div[5]/div["
                    xpath2 = str(xpath1) + str(aux_code) + ']/div[2]/ul/li['

                    xpath1 = "]/div[3]/div[2]/div[1]/label/div[1]/textarea"

                    xpath_full = xpath2 + str(numerodapergunta) + xpath1

                    btn1 = "//*[@id='page']/div[5]/div["
                    btn2 = str(btn1) + str(aux_code) + ']/div[2]/ul/li['

                    btn1 = "]/div[3]/div[2]/div[2]/button"

                    full_xpathBtn = btn2 + str(numerodapergunta) + btn1

                    #----------------------------------------------------------------------------------------------------------
                    #answers the client
                    browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, não foi possível verificar com este chassi, poderia nos enviar o chassi de seu veículo novamente da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")

                    aux = browser1.find_element(By.XPATH, full_xpathBtn)

                    browser1.execute_script("arguments[0].click();", aux)

                    aux1 = 0
                    aux2 = 'res'
                    print("1-Olá, não foi possível verificar com este chassi, poderia nos enviar o chassi de seu veículo novamente da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                    browser2.refresh()
                    respondido = True
                    return(respondido)
                    #----------------------------------------------------------------------------------------------------------
            #----------------------------------------------------------------------------------------------------------

            #----------------------------------------------------------------------------------------------------------
            try:
                #wait new frame
                WebDriverWait(browser2, 10000).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content3')))

                #select frame
                frame = browser2.find_element(By.CSS_SELECTOR, '#content3')

                #into the frame
                browser2.switch_to.frame(frame)

                #part code search
                browser2.find_element(By.XPATH, '//*[@id="editBusca"]').send_keys(code)

                #click in search
                browser2.find_element(By.XPATH, '//*[@id="editBusca"]').send_keys(Keys.ENTER)
                #return for frame principal
                browser2.switch_to.parent_frame()
            except:
                print('Ocorreu um erro ao tentar pesquisar peça')
            #----------------------------------------------------------------------------------------------------------

            #wait new frame
            WebDriverWait(browser2, 21).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content3')))

            #select frame
            frame = browser2.find_element(By.CSS_SELECTOR, '#content3')

            #into the frame
            browser2.switch_to.frame(frame)

            browser2.implicitly_wait(10)
            result = ''
            while (result == ''):
                #get result
                result = browser2.find_element(By.XPATH, '//*[@id="titResultados_text"]').text
                result = re.sub('[^0-9]', '', result)

            #return for frame principal
            browser2.switch_to.parent_frame()

            browser2.refresh()
            #check if there is a result
            if(int(result) > 0):
                #concatenates element XPATHS
                xpath1 = "//*[@id='page']/div[5]/div["
                xpath2 = str(xpath1) + str(aux_code) + ']/div[2]/ul/li['

                xpath1 = "]/div[3]/div[2]/div[1]/label/div[1]/textarea"

                xpath_full = xpath2 + str(numerodapergunta) + xpath1

                btn1 = "//*[@id='page']/div[5]/div["
                btn2 = str(btn1) + str(aux_code) + ']/div[2]/ul/li['

                btn1 = "]/div[3]/div[2]/div[2]/button"

                full_xpathBtn = btn2 + str(numerodapergunta) + btn1
                

                #----------------------------------------------------------------------------------------------------------
                #answers the client
                browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, Serve sim, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                aux = browser1.find_element(By.XPATH, full_xpathBtn)
                browser1.execute_script("arguments[0].click();", aux)
                aux1 = 0
                print("Olá, Serve sim, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                respondido = True
                return(respondido)
                #----------------------------------------------------------------------------------------------------------
            else:
                #concatenates element XPATHS
                xpath1 = "//*[@id='page']/div[5]/div["
                xpath2 = str(xpath1) + str(aux_code) + ']/div[2]/ul/li['

                xpath1 = "]/div[3]/div[2]/div[1]/label/div[1]/textarea"

                xpath_full = xpath2 + str(numerodapergunta) + xpath1

                btn1 = "//*[@id='page']/div[5]/div["
                btn2 = str(btn1) + str(aux_code) + ']/div[2]/ul/li['

                btn1 = "]/div[3]/div[2]/div[2]/button"

                full_xpathBtn = btn2 + str(numerodapergunta) + btn1

                #----------------------------------------------------------------------------------------------------------
                #answers the client
                browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, infelismente não serve, dê mais uma olhada em nossa loja tenho certeza que encontrará o que procura, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                aux = browser1.find_element(By.XPATH, full_xpathBtn)
                browser1.execute_script("arguments[0].click();", aux)
                aux1 = 0
                print("Olá, infelismente não serve, dê mais uma olhada em nossa loja tenho certeza que encontrará o que procura, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                respondido = True
                return(respondido)
                #----------------------------------------------------------------------------------------------------------

            #back to catalog homepage
            browser2.get("https://fordcatalog.com/")

            #check if the word chassis was found
            if(chassi == "no"):
                #if not found start loop while have elements in list
                for i in range(len(pergunta)):
                    aux1 = 0
                    aux1 += 1
                    #check for the words contained in the posi list
                    if(pergunta[i] == questions[aux1] or pergunta[i] == questions[aux1 + 1] or pergunta[i] == questions[aux1 + 2] or pergunta[i] == questions[aux1 + 3] and i < len(pergunta)):
                        aux1 = 0
                        if(int(qtd) == 1):
                            #concatenates element XPATHS
                            xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li"

                            xpath2 = "/div[3]/div[2]/div[1]/label/div[1]/textarea"

                            xpath_full = xpath1 + xpath2

                            btn1 = "//*[@id='page']/div[5]/div/div[2]/ul/li"

                            btn2 = "/div[3]/div[2]/div[2]/button"

                            full_xpathBtn = btn1 + btn2

                            #----------------------------------------------------------------------------------------------------------
                            #answers the client
                            browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, poderia me enviar o chassi de seu veículo da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                            aux = browser1.find_element(By.XPATH, full_xpathBtn)
                            browser1.execute_script("arguments[0].click();", aux)
                            aux1 = 0
                            print("Olá, poderia me enviar o chassi de seu veículo da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.2")
                            respondido = True
                            return(respondido)
                            #----------------------------------------------------------------------------------------------------------
                        else:
                            #concatenates element XPATHS
                            xpath1 = "//*[@id='page']/div[5]/div["
                            xpath2 = str(xpath1) + str(aux_code) + ']/div[2]/ul/li['

                            xpath1 = "]/div[3]/div[2]/div[1]/label/div[1]/textarea"

                            xpath_full = xpath2 + str(numerodapergunta) + xpath1

                            btn1 = "//*[@id='page']/div[5]/div["
                            btn2 = str(btn1) + str(aux_code) + ']/div[2]/ul/li['

                            btn1 = "]/div[3]/div[2]/div[2]/button"

                            full_xpathBtn = btn2 + str(numerodapergunta) + btn1

                            #----------------------------------------------------------------------------------------------------------
                            #answers the client
                            browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, poderia me enviar o chassi de seu veículo da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                            aux = browser1.find_element(By.XPATH, full_xpathBtn)
                            browser1.execute_script("arguments[0].click();", aux)
                            aux1 = 0
                            aux2 = 'res'
                            print("Olá, poderia me enviar o chassi de seu veículo da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.2")
                            respondido = True
                            return(respondido)
                            #----------------------------------------------------------------------------------------------------------
    return(False)

def PularQuestion(numero, aux_code):
    aux= '//*[@id="page"]/div[5]/div['
    aux1 = str(aux) + str(aux_code) + ']/div[2]/ul/li['
    aux= str(aux1) + str(numero) 
    aux= str(aux) + ']/div[3]/div[2]'
    cli = browser1.find_element(By.XPATH, aux)
    browser1.execute_script("arguments[0].click();", cli)
    
#Part code conversion function
def convercao(codigo):
    codi = ''
    aux = len(codigo)
    print('ini')
    #10 charatere
    if(aux == 10):
        for i in range(aux):
            
            if(codigo[i]=='/'):
                return(codigo)
        print('nao achei')
        aux1 = codigo
        aux = 11
        a = aux
        for i in range(aux):
            cont = i
            print(a)
            print(cont)
            if(i < 4):
                
                codi += aux1[i]
                aux += 1
            elif(i == 4 or i == 9):
                codi += '/'
            if (i > 4 and cont < aux):
                cont = cont - 1
                
                codi += aux1[cont]

                aux += 1
            if (i > aux or cont > aux):
                break
        return(codi)
    
    if (aux > 11 and aux < 19):
        for i in range(aux):
            if(codigo[i]=='/'):
                return(codigo)

        for i in range(11):
            cont = i
            if (i < 4):
                codi += codigo[i]
            elif(i == 4):
                codi += '/'
            if (i > 4 and cont < aux):
                cont = cont - 1
                
                codi += codigo[cont]

                aux += 1
        return(codi)
    
    if (aux == 11):
        for i in range(aux):
            
            if(codigo[i]=='/'):
                return(codigo)
        print('nao achei')
        aux1 = codigo
        aux = 12
        a = aux
        for i in range(aux):
            cont = i
            print(a)
            print(cont)
            if(i < 4):
                
                codi += aux1[i]
                aux += 1
            elif(i == 4 or i == 10):
                codi += '/'
            if (i > 4 and cont < aux):
                cont = cont - 1
                
                codi += aux1[cont]

                aux += 1
            if (i > aux or cont > aux):
                break
    if (aux > 19):
        for i in range(9):
            cont = i
            if (i < 4):
                codi += codigo[i]
            elif(i==4):
                codi += '/'
            if(i > 4):
                cont = cont - 1
                codi += codigo[cont]
        return(codi)
    
    
def ProximaPagina(qtd, total, contador, aux_code):   
    
    if(qtd > total and contador == total):
        try:
            aux_code = 0
            contador = 0
            try:

                try:

                    browser1.find_element(By.XPATH, '//*[@id="page"]/ul[2]/li[3]/a').click()

                except:

                    aux = browser1.find_element(By.XPATH, '//*[@id="page"]/ul[2]/li[3]/a')
                    browser1.execute_script("arguments[0].click();", aux) 

            except:

                try:

                    browser1.find_element(By.XPATH, '//*[@id="page"]/ul[2]/li[4]/a/span[1]').click()

                except:

                    aux = browser1.find_element(By.XPATH, '//*[@id="page"]/ul[2]/li[4]/a/span[1]')
                    browser1.execute_script("arguments[0].click();", aux) 
        except:

            print('error: 201.1')
    
def Codigo(code):
    try:
        if(int(number_questions) > 1):
            #concatenates XPATH element so that it takes an element from the question list
            xpath1 = "//*[@id='page']/div[5]/div["

            xpath2 = "]/div[1]/div/div[1]/div[2]/div[1]/a"

            xpath_full = xpath1 + str(code) + xpath2
        else:
            #concatenates XPATH element so that it takes an element from the question list
            xpath1 = "//*[@id='page']/div[5]/div"

            xpath2 = "/div[1]/div/div[1]/div[2]/div[1]/a"

            xpath_full = xpath1 + xpath2
        #get the part code of the ad
        cod = browser1.find_element_by_xpath(xpath_full).text

        #turn into list
        cod = cod.split()
        code = convercao(cod[1])
        return(code)
    except:
        return('erro')
        print('Não foi possível encontrar código da peça')
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Importing libraries
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#variable bool
loop = True

#question types
questions = "serve funciona funcionaria encaixa"
questions = questions.split()

#open browser
browser1 = webdriver.Chrome()

#enter the Mercado Livre
browser1.get("https://www.mercadolivre.com/jms/mlb/lgz/msl/login/H4sIAAAAAAAEAzXOwQrDIBAE0H-ZsyR3j_2RsDGrkWqVdVNbQv692NLjwPBmTqQS4mPRd2VY8Kum6KLCoCZSXyQvcYNFTjBoUfkf11EhoczK0mDPAQXebuyLDErlYBjQofviU-mwvykYhAKLXbU2O8-99ymzONpKik_hyZU8rTLDQDjEpiw8Hny9y8BT00WF3B3WU2p8fQC9dzgpxAAAAA/user")

#open the new browser for catalogo
browser2 = webdriver.Chrome()


#-----------------------------------------------------------------------------------------------------------------------------------------------
while (loop == True):
    try:
        loop = False
        #click in menu
        browser1.find_element_by_xpath('//*[@id="nav-header-menu"]/div/label/a').click()
        print('cliquei')
        
        browser1.get('https://www.mercadolivre.com.br/perguntas/vendedor')
        
    except:
        loop = True
        print('erro')
#--------------------------------------------------------------------------------------------------------------------------------------------------
#wait 10seg
browser1.implicitly_wait(10)

#--------------------------------------------------------------------------------------------------------------------------------------------------
try:
    #Get number of questions
    number_questions = browser1.find_element_by_xpath('//*[@id="page"]/div[4]/div[3]/div').text

    #remove all text and leave only numbers
    number_questions = re.sub('[^0-9]', '', number_questions)

except:
    #close info window
    aux = browser1.find_element_by_xpath('/html/body/div[9]/div[1]/div/div[2]/button')
    browser1.execute_script("arguments[0].click();", aux)
     #Get number of questions
    number_questions = browser1.find_element_by_xpath('//*[@id="page"]/div[4]/div[3]/div').text

    #remove all text and leave only numbers
    number_questions = re.sub('[^0-9]', '', number_questions)
    
    print('Ocorreu um erro na pagina de perguntas')
#--------------------------------------------------------------------------------------------------------------------------------------------------

#show number in console
print(number_questions)

#start new auxiliary variable
aux_code = 0
aux1 = 0
aux2 = ''
erro = True
contador = 0
total = 50
numeronaorespondido = 0

while (erro == True):
    aux_code = aux_code + 1
    contador = 0
    code = Codigo(aux_code)
    
    for qtd in range(int(number_questions)):
        respondido = False
        contador = contador + 1
        print('numero não respondido' + str(numeronaorespondido))
        
        question = PegaPergunta(contador, int(number_questions), respondido, aux_code)
        
     
        if(numeronaorespondido >= total):
            print('proxima pagina')
            ProximaPagina(int(number_questions), total, numeronaorespondido, aux_code)
            numeronaorespondido = 0
            contador = 0
            aux_code = 0
            
            break
            
        if(question == 'erro'):
            print('erro')
            contador = 0
            code = Codigo(aux_code)
            break
            
        if(question != ''):
            question = question.split()
            for palavra in range(len(question)):
                
                if(question[palavra] == 'Chassi' or question[palavra] == 'chassi' or question[palavra] == 'Aplica' or question[palavra] == 'aplica'
                  or question[palavra] == 'encaixa' or question[palavra] == 'Encaixa' or question[palavra] == 'serve' or question[palavra] == 'Serve'):

                    respondido = Resposta(question, contador, number_questions, code, aux_code)
                
            if(respondido == False):
                print('false')
                numeronaorespondido = numeronaorespondido + 1
                PularQuestion(contador, aux_code)
            
            if(respondido == True):
                
                contador = contador - 1

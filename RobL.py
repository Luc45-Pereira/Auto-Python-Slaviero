
# Dev: Lucas Pereira de Lima
# Data de desenvolvimento: outubro de 2021
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sistema de automação de respostas do mercado livre para a empresa Ford Slaviero

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Importing libraries
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#question types
questions = "serve funciona funcionaria encaixa"
questions = questions.split()

#open browser
browser1 = webdriver.Chrome()

#enter the Mercado Livre
browser1.get("https://www.mercadolivre.com/jms/mlb/lgz/msl/login/H4sIAAAAAAAEAzXOwQrDIBAE0H-ZsyR3j_2RsDGrkWqVdVNbQv692NLjwPBmTqQS4mPRd2VY8Kum6KLCoCZSXyQvcYNFTjBoUfkf11EhoczK0mDPAQXebuyLDErlYBjQofviU-mwvykYhAKLXbU2O8-99ymzONpKik_hyZU8rTLDQDjEpiw8Hny9y8BT00WF3B3WU2p8fQC9dzgpxAAAAA/user")

#open the new browser for catalogo
browser2 = webdriver.Chrome()
browser2.get("https://fordcatalog.com/")

#wait until it loads completely
WebDriverWait(browser2, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content1")))

#Wait 5 minutes
browser1.implicitly_wait(300)

#click in menu
browser1.find_element_by_xpath('//*[@id="nav-header-menu"]/div').click()

#open option questions in browser1 using an auxiliary variable
aux = browser1.find_element_by_xpath('/html/body/div[9]/div[1]/div/div[2]/button')
browser1.execute_script("arguments[0].click();", aux)

aux = browser1.find_element_by_xpath('//*[@id="root-app"]/div/div/div[1]/nav/div/div/div[1]/section[2]/div[1]/span/div/label')
browser1.execute_script("arguments[0].click();", aux)

aux = browser1.find_element_by_xpath('//*[@id="seller_questions"]')
browser1.execute_script("arguments[0].click();", aux)

#wait 10seg
browser1.implicitly_wait(10)

#close info window
aux = browser1.find_element_by_xpath('/html/body/div[9]/div[1]/div/div[2]/button')
browser1.execute_script("arguments[0].click();", aux)

#Get number of questions
number_questions = browser1.find_element_by_xpath('//*[@id="page"]/div[4]/div[3]/div').text

#remove all text and leave only numbers
number_questions = re.sub('[^0-9]', '', number_questions)

#show number in console
print(number_questions)

#start new auxiliary variable
aux1 = 0

#start loop until there are no more questions
for i in range(int(number_questions)):
    #check auxiliary variable 2 to reset auxiliary variable 1
    if(aux2 == 'res'):
        aux1 = 0
        a = ''
    
    #Get number of questions
    number_questions = browser1.find_element_by_xpath('//*[@id="page"]/div[4]/div[3]/div').text

    #remove all text and leave only numbers
    number_questions = re.sub('[^0-9]', '', number_questions)
 
    #auxiliary variable
    aux3 = aux1 + 1

    #new variable num
    num = 0

    #get the part code of the ad
    cod = browser1.find_element_by_xpath('//*[@id="page"]/div[5]/div/div[1]/div/div[1]/div[2]/div[1]/a').text

    #turn into list
    cod = cod.split()

    #check i is greater than 0
    if(i > 0):
        #concatenates XPATH element so that it takes an element from the question list
        xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["

        xpath2 = "]/div[3]/div[2]"

        xpath_full = xpath1 + str(aux3) + xpath2

        #select element
        aux = browser1.find_element(By.XPATH, xpath_full)
        
        #click in element
        browser1.execute_script("arguments[0].click();", aux)
    
    #check i is greater or like 0
    if(i >= 0):
        #concatenates XPATH element so that it takes an element from the question list
        xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["

        xpath2 = "]/div[3]/div[2]"

        xpath_full = xpath1 + str(aux3) + xpath2
    
    #check if number_questions is like 1 and i greater 0
    if(int(number_questions) == 1 and i > 0):
        #concatenate XPATH element so that it takes an element from the question list
        xpath_full = '//*[@id="page"]/div[5]/div/div[2]/ul/li/div[3]/div[2]'

        #click in element
        aux = browser1.find_element(By.XPATH, xpath_full)
        browser1.execute_script("arguments[0].click();", aux)

        #concatenates the xpath element
        xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li"

        xpath2 = "/div[3]/div[1]/div[2]/span[2]/span[1]"

        xpath_full = xpath1 + xpath2

    else:
        #concatenates element XPATH
        xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li"

        xpath2 = "/div[3]/div[1]/div[2]/span[2]/span[1]"

        xpath_full = xpath1 + xpath2
    
    #get question
    aux_question = browser1.find_element_by_xpath(xpath_full).text

    #turn into list
    aux_question = aux.split()

    #variable to know if it found the chassi
    chassi = "no"

    #loop while there are elements in the list
    for i in range(len(aux_question)):
        
        #check if aux_question like chassi
        if(aux_question == "chassi" or aux_question == "Chassi"):
            #variable to know if it found the chassi
            chassi = 'yes'

            #insert i+1 in num
            num = i+1

            #select frame in window
            frame = browser2.find_element(By.CSS_SELECTOR, '#content1')

            #into the frame
            browser2.switch_to_frame(frame)
            browser2.implicitly_wait(20)

            #select input usuario and insert user
            browser2.find_element(By.CSS_SELECTOR, '#edtUsuario').send_keys("1289_lucas")

            #select input senha and insert pass
            browser2.implicitly_wait(20)
            browser2.find_element(By.CSS_SELECTOR, '#edtSenha').send_keys("0481b29")

            #click in button
            browser2.implicitly_wait(20)
            browser2.find_element(By.CSS_SELECTOR, '#btLogin_text').click()

            #return for frame principal
            browser2.switch_to.parent_frame()

            #wait 20 seg
            browser2.implicitly_wait(20)

            #wait new frame
            WebDriverWait(browser2, 21).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content2')))

            #select frame
            frame = browser2.find_element(By.CSS_SELECTOR, '#content2')

            #into the frame
            browser2.switch_to_frame(frame)

            #search chassi
            browser2.find_element(By.CSS_SELECTOR, '#editChassi').send_keys(n[num])

            #click in pesquisar
            browser2.find_element(By.CSS_SELECTOR, '#btChassi_text').click()

            #return for frame principal
            browser2.switch_to.parent_frame()

            #wait 10 seg
            browser2.implicitly_wait(10)

            #wait new frame
            WebDriverWait(browser2, 21).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#popContentFrame0')))

            #select frame
            frame = browser2.find_element(By.CSS_SELECTOR, '#popContentFrame0')

            #into the frame
            browser2.switch_to_frame(frame)

            #click in browse with VIN
            browser2.find_element(By.CSS_SELECTOR, '#btAvancarPesq_text').click()

            #return for frame principal
            browser2.switch_to.parent_frame()

             #wait new frame
            WebDriverWait(browser2, 21).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content3')))

            #select frame
            frame = browser2.find_element(By.CSS_SELECTOR, '#content3')

            #into the frame
            browser2.switch_to_frame(frame)

            #part code search
            browser2.find_element(By.XPATH, '//*[@id="editBusca"]').send_keys(cod[1])

            #click in search
            browser2.find_element(By.XPATH, '//*[@id="btBuscar_text"]').click()

            #get result
            result = browser2.find_element(By.XPATH, '//*[@id="titResultados_text"]').text
            result = re.sub('[^0-9]', '', result)

            #return for frame principal
            browser2.switch_to.parent_frame()

            #check if there is a result
            if(int(result) > 0):
                #concatenates element XPATHS
                xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["

                xpath2 = "]/div[3]/div[2]/div[1]/label/div[1]/textarea"

                xpath_full = xpath1 + str(aux3) + xpath2

                btn1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["

                btn2 = "]/div[3]/div[2]/div[2]/button"

                full_xpathBtn = btn1 + str(aux3) + btn2

                #answers the client
                browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, Serve sim, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                aux = browser1.find_element(By.XPATH, full_xpathBtn)
                browser1.execute_script("arguments[0].click();", aux)
                aux1 = 0
            else:
                #concatenates element XPATHS
                xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["

                xpath2 = "]/div[3]/div[2]/div[1]/label/div[1]/textarea"

                xpath_full = xpath1 + str(aux3) + xpath2

                btn1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["

                btn2 = "]/div[3]/div[2]/div[2]/button"

                full_xpathBtn = btn1 + str(aux3) + btn2

                #answers the client
                browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, infelismente não serve, dê mais uma olhada em nossa loja tenho certeza que encontrará o que procura, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                aux = browser1.find_element(By.XPATH, full_xpathBtn)
                browser1.execute_script("arguments[0].click();", aux)
                aux1 = 0

            #back to catalog homepage
            browser2.get("https://fordcatalog.com/")
    
    #check if the word chassis was found
    if(chassi == "no"):

        #if not found start loop while have elements in list
        for i in range(len(aux_question)):
            aux0 = 0
            aux1 += 1
            #check for the words contained in the posi list
            if(aux_question[i] == questions[aux0] or aux_question[i] == questions[aux0 + 1] or aux_question[i] == questions[aux0 + 2] or aux_question[i] == questions[aux0 + 3]):
                aux1 = 0
                if(int(number_questions) == 1):
                      #concatenates element XPATHS
                    xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li"

                    xpath2 = "/div[3]/div[2]/div[1]/label/div[1]/textarea"

                    xpath_full = xpath1 + xpath2

                    btn1 = "//*[@id='page']/div[5]/div/div[2]/ul/li"

                    btn2 = "/div[3]/div[2]/div[2]/button"

                    full_xpathBtn = btn1 + btn2

                    #answers the client
                    browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, poderia me enviar o chassi de seu veículo da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                    aux = browser1.find_element(By.XPATH, full_xpathBtn)
                    browser1.execute_script("arguments[0].click();", aux)
                    aux1 = 0
                else:
                    #concatenates element XPATHS
                    xpath1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["

                    xpath2 = "]/div[3]/div[2]/div[1]/label/div[1]/textarea"

                    xpath_full = xpath1 + str(aux3) + xpath2

                    btn1 = "//*[@id='page']/div[5]/div/div[2]/ul/li["

                    btn2 = "]/div[3]/div[2]/div[2]/button"

                    full_xpathBtn = btn1 + str(aux3) + btn2

                    #answers the client
                    browser1.find_element(By.XPATH, xpath_full).send_keys("Olá, poderia me enviar o chassi de seu veículo da seguinte maneira - 'Chassi numero_chassi', para que possamos lhe informar corretamente, Ford Slaviero agradece seu contato, e aguarda anciosamente por sua compra.")
                    aux = browser1.find_element(By.XPATH, full_xpathBtn)
                    browser1.execute_script("arguments[0].click();", aux)
                    aux1 = 0

#Get number of questions
number_questions = browser1.find_element_by_xpath('//*[@id="page"]/div[4]/div[3]/div').text

#remove all text and leave only numbers
number_questions = re.sub('[^0-9]', '', number_questions)

#show number in console
print(number_questions)

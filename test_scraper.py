import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import extraction_functions
import tensorflow as tf 
import tensorflow.contrib.eager as tfe
tf.enable_eager_execution()
from Download import download
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
all_tags = ['h1','h2','h3','h4','h5','h6','td','b','p','span','div']

classifierLoad = tf.keras.models.load_model('Bid_Prediction_Model.h5',compile=False)
Titleclassifierload = tf.keras.models.load_model('Title_Prediction_Model.h5',compile=False)

#SSLDOASSTATE
driver.get('https://ssl.doas.state.ga.us/PRSapp/PR_index.jsp')
time.sleep(5)
js = 'document.querySelectorAll(`input`)[2].click()'
driver.execute_script(js)
time.sleep(10)
page_link = driver.find_elements(By.TAG_NAME, 'a')
all_hrefs = []
for page in page_link:
    all_hrefs.append(page.get_attribute('href'))
driver.quit()

for i in range(5, len(all_hrefs)):
    href = all_hrefs[i]
    time.sleep(2)
    html = download(href)
    soup = BeautifulSoup(html,'html.parser')
    print("\n\n****************************************\n\n")
    combined,phone_number_list,email_list,date_list = extraction_functions.extraction(soup)
    print("Date:",date_list)
    print("List_Phone_Number:",phone_number_list)
    print("Email:",email_list)
    combined_number = [com for com in combined if extraction_functions.only_alpha(com)]
    combined_number = [com for com in combined_number if len(com) < 20]
    predict_matrix_number = extraction_functions.fill_matrix(combined_number)
    class_ids = ["0", "1"]
    Bid_Number_predictions = classifierLoad.predict(predict_matrix_number)
    probabilities = []
    for pred in Bid_Number_predictions:
        probabilities.append(pred[1])
    highest_prob = 0
    index = 0
    highest_index = 0
    for prob in probabilities:
        if prob > highest_prob:
            highest_prob = prob
            highest_index = index
        index += 1
    print("Bid_Number:",combined_number[highest_index][0])
    predict_matrix_title = extraction_functions.fill_matrix(combined)
    Title_predictions = Titleclassifierload.predict(predict_matrix_title)
    probabilities_title = []
    for pred1 in Title_predictions:
        probabilities_title.append(pred1[1])
    highest_prob1 = 0
    index1 = 0
    highest_index1 = 0
    for prob1 in probabilities_title:
        if prob1 > highest_prob1:
            highest_prob1 = prob1
            highest_index1 = index1
        index1 += 1
    print("Title:",combined[highest_index1][0])
    print("\n****************************************\n")


'''
#EMMA MARYLAND 
all_hrefs = []
driver.get("https://emma.maryland.gov/page.aspx/en/rfp/request_browse_public")
for i in range(2,27):
    element = driver.find_element(By.ID,"body_x_grid_grd__ctl{}_img___colManagegrid".format(i))
    elem = element.get_attribute("href")
    all_hrefs.append(elem)
driver.quit()

for i in range(len(all_hrefs)):
    href = all_hrefs[i]
    time.sleep(2)
    html = download(href)
    soup = BeautifulSoup(html,'html.parser')
    print("\n\n****************************************\n\n")
    combined,phone_number_list,email_list = extraction_functions.extraction(soup)
    print("List_Phone_Number:",phone_number_list)
    print("Email:",email_list)
    combined_number = [com for com in combined if extraction_functions.only_alpha(com)]
    combined_number = [com for com in combined_number if len(com) < 20]
    predict_matrix_number = extraction_functions.fill_matrix(combined_number)
    class_ids = ["0", "1"]
    Bid_Number_predictions = classifierLoad.predict(predict_matrix_number)
    probabilities = []
    for pred in Bid_Number_predictions:
        probabilities.append(pred[1])
    highest_prob = 0
    index = 0
    highest_index = 0
    for prob in probabilities:
        if prob > highest_prob:
            highest_prob = prob
            highest_index = index
        index += 1
    print("Bid_Number:",combined_number[highest_index][0])
    predict_matrix_title = extraction_functions.fill_matrix(combined)
    Title_predictions = Titleclassifierload.predict(predict_matrix_title)
    probabilities_title = []
    for pred1 in Title_predictions:
        probabilities_title.append(pred1[1])
    highest_prob1 = 0
    index1 = 0
    highest_index1 = 0
    for prob1 in probabilities_title:
        if prob1 > highest_prob1:
            highest_prob1 = prob1
            highest_index1 = index1
        index1 += 1
    print("Title:",combined[highest_index1][0])
    print("\n****************************************\n")
    '''
time.sleep(5)
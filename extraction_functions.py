import re
import Web_Extract
import tensorflow as tf 
import tensorflow.contrib.eager
tf.enable_eager_execution()

def only_alpha(tup):
    if tup[0].isalpha():
        return False
    else:
        return True

def phone_number(phone):
     if (phone[0].isdigit() and len(phone[0]) == 10):
        return False
     elif re.match(r'\d\d\d-\d\d\d-\d\d\d\d', str(phone[0])):
         cleaned = re.sub(r'[^\w]', '', str(phone[0]))
         if (cleaned.isdigit() and len(cleaned) == 10):
             return False
     else:
         return True
     
def Find_Phone_Number(store):
    phone_number_store = []
    for item in store:
        if re.match(r'\d\d\d-\d\d\d-\d\d\d\d', str(item)):
            phone_number_store.append(item)
        else:
            numericlist = [num for num in store if num.isdigit()]
            for subitem in numericlist:
                if len(subitem) == 10:
                    phone_number_store.append(subitem)
    
    return phone_number_store

def Find_Date(store):
    data_list = []
    for item in store:
        if re.findall(r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}',str(item)):
            data_list.append(item)
        if re.findall(r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2}),\s+(\d{4})',str(item)):
            data_list.append(item)
        if re.findall(r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2}),\s+(\d{4})@[0-1]{0,1}[0-9]{1,2}:[0-5][0-9]\s(AM|PM)',str(item)):
            data_list.append(item)
        if re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", str(item)):
            data_list.append(item)
    return data_list

def extraction(soup):
    fresh_elements = []
    all_elements =[]
    date_list = []
    all_Date_list = []
    all_phone_number_list = []
    phone_number_list = []
    email_list = []
    all_email_list = []
    for tag in soup.find_all():
        all_elements.append(tag.name)
    wanted_tags = ['h1','h2','h3','h4','h5','h6','td','b','p','span','div']
    fresh_elements = [el for el in all_elements if el in wanted_tags]
    unique_elem = set(fresh_elements)
    unique_list = list(unique_elem)
    store, tag_name, index_number = Web_Extract.Web_Extraction(soup,unique_list)
    all_phone_number_list = Find_Phone_Number(store)
    all_phone_number_list = set(all_phone_number_list)
    phone_number_list = list(all_phone_number_list)
    all_email_list = re.findall(r"[A-Za-z0-9._%+-]+"r"@[A-Za-z0-9.-]+"r"\.[A-Za-z]{2,4}",str(store))
    all_email_list = set(all_email_list)
    email_list = list(all_email_list)
    all_Date_list = Find_Date(store)
    all_Date_list = set(all_Date_list)
    date_list = list(all_Date_list)
    combined = []
    for i in range(len(store)):
        combined.append((store[i], tag_name[i], index_number[i]))
    combined = [com for com in combined if phone_number(com)]    
    return combined,phone_number_list,email_list,date_list

all_tags = ['h1','h2','h3','h4','h5','h6','td','b','p','span','div']

#called each time per index of array
def format_array(index, combined):
    element_array = []
    store = []
    tag_name = []
    index_number = []
    for com in combined:
        store.append(com[0])
        tag_name.append(com[1])
        index_number.append(com[2])
    #print("Formatting:", str(index), ":", store[index])
    for tag in all_tags:
        if tag_name[index] == tag:
            element_array.append(1)
        else:
            element_array.append(0)
    length_data = len(store[index])
    element_array.append(length_data)
    num_numbers = 0
    num_alpha = 0
    for char in store[index]:
        if char.isdigit():
            num_numbers += 1
        elif char.isalpha():
            num_alpha += 1
        else:
            pass 
    element_array.append(num_numbers)
    element_array.append(num_alpha)
    element_array.append(len(store[index]) - len(re.findall('[\w]',store[index])))
    element_array.append(index_number[index])
    element_array.append(len(re.findall(" ", store[index])))
    element_array.append(len(re.findall("-", store[index])))
    element_array.append(len(re.findall("_", store[index])))
    element_array.append(len(re.findall("#", store[index])))
    element_array.append(len(re.findall('RFP', store[index])))
    element_array.append(len(re.findall('RFQ', store[index])))
    element_array.append(len(re.findall('RFA', store[index])))
    element_array.append(len(re.findall('IFB', store[index])))
    element_array.append(len(re.findall('/', store[index])))
    return element_array


def fill_matrix(combined):
    final_matrix = []
    num_elems = len(combined)
    for index in range(num_elems):
        final_matrix.append(format_array(index, combined))
    return tf.convert_to_tensor(final_matrix)


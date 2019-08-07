# -*- coding: utf-8 -*-
import time
from Download import download
from bs4 import BeautifulSoup
import Scrap_Preprocess
import Pred_module
import csv
import pandas as pd

fieldnames = ['Data']

test_array = ["http://www.eslcafe.com/joblist/index.cgi?read=51505",
              "http://www.eslcafe.com/joblist/index.cgi?read=51422",
              "http://www.eslcafe.com/joblist/index.cgi?read=51426",
              "http://www.eslcafe.com/joblist/index.cgi?read=51198",
              "http://www.eslcafe.com/joblist/index.cgi?read=51557",
              "https://nevadaepro.com/bso/external/bidAck.sdo;jsessionid=A82E2720A2C12D5B3B195B79AD4AE0D7?bidId=30DOE-S626&parentUrl=activeBids",
              "https://nevadaepro.com/bso/external/bidAck.sdo;jsessionid=A82E2720A2C12D5B3B195B79AD4AE0D7?bidId=99SWC-S616&parentUrl=activeBids",
              "https://ssl.doas.state.ga.us/PRSapp/PublicBidNotice?bid_op=196621800021",
              "http://www.newyorkbids.net/bid_opportunities/2019/06/13/9451949-replacement-of-roof-at-the-town-highway-garage---2019.html",
              "https://www.miamidade.gov/DPMww/SolicitationDetails.aspx?Id=EDP%20POOL%20OPENING",
              "https://www.miamidade.gov/DPMww/SolicitationDetails.aspx?Id=20190120%20(MCC%207360)",
              "https://bidopportunities.iowa.gov/Home/BidInfo?bidId=4e64eb9a-0fd6-4721-83fe-a51201957477",
              "https://bidopportunities.iowa.gov/Home/BidInfo?bidId=f773b1fe-0be9-4c4c-8efb-6dab4dd6b7b3",
              "https://bidopportunities.iowa.gov/Home/BidInfo?bidId=f773b1fe-0be9-4c4c-8efb-6dab4dd6b7b3",
              "https://bidopportunities.iowa.gov/Home/BidInfo?bidId=dd135811-7bf6-4364-9f02-991257c72cf2",
              "https://bidopportunities.iowa.gov/Home/BidInfo?bidId=dd135811-7bf6-4364-9f02-991257c72cf2"
              ]

with open('testarrayData.csv', 'a') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(fieldnames)

nrows =len(test_array)

#CONVERT DATA FROM A LIST TO A CSV AND PERFORM WEBSCRAP       
for i in range(nrows):
    print(i)
    next = False
    if next:
        continue
    link = test_array[i]
    if str(link).startswith("http"):
        print("Getting Link")
        html = download(link)
        soup = BeautifulSoup(html,'html.parser')
        print("Got link")
        Scrap_Preprocess.extraction(soup)
        print("extracted, goodnight")
        time.sleep(5)
    else:
        next = True

data = pd.read_csv("testarrayData.csv")
y_pred1 = Pred_module.prediction(data)

Solic_links = []

for i in range(len(y_pred1)):
    if y_pred1[i] == 0:
        print(i,"Solication Page")
    elif y_pred1[i] == 1:
        print(i,"Non Solication Page")
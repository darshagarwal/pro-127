from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("D:/coding/cl127/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Name","Distance","Mass","Radius"]
    star_data = []
    
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for td_tag in soup.find_all("td",attrs={"class","headerSort"}):
        td_tags = td_tag
        temp_list=[]
        for index,li_tag in enumerate(td_tags):
            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else: 
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        star_data.append(temp_list)

    with open("proscrapper.csv","w") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(headers)
        csv_write.writerows(star_data)

scrape()
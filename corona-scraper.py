from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import pandas as pd
import os
import shutil

#Name of columns
field_list = ["Name","Total Cases","New Cases","Total Deaths","New Deaths","Total Recovered","New Recovered","Active Cases","Serious Cases","Total Tests","Population"]

#Specify current day as filename and create path from current work directory with filename
#filename = str(date.today().strftime("%d/%m/%Y")).replace("/", "-")
filename = str(datetime.today().strftime('%d-%m-%Y @ %H.%M') + " Uhr")
path = str(str(os.getcwd()) + "\\" + filename + "\\")

#specifiy filename and current + new path for csv
filename_csv = str(datetime.today().strftime('%d-%m-%Y @ %H.%M') + " Uhr") + ".csv"
path_csv = str(str(os.getcwd()) + "\\" + filename + ".csv")
new_path_csv = str(str(os.getcwd()) + "\\" + filename + "\\" + filename + ".csv")

#specifiy filename and current + new path for html
filename_html = str(datetime.today().strftime('%d-%m-%Y @ %H.%M') + " Uhr") + ".html"
path_html = str(str(os.getcwd()) + "\\" + filename + ".html")
new_path_html = str(str(os.getcwd()) + "\\" + filename + "\\" + filename + ".html")

#scrape all data
def get_all_data():
    url = requests.get("https://www.worldometers.info/coronavirus/").text
    soup = BeautifulSoup(url,"lxml")
    complete_data = []
    world_data = soup.find("tbody").find_all("tr")
    for i in range(8,229):
        data = []
        list_data = world_data[i].find_all("td")
        for i in list_data:
            data.append(i.text)
        complete_data.append(data)
    
    mapped_data = list(map(lambda x: x[1:10] + [x[12]] +[x[14]],complete_data))
  
    #create csv file
    with open(filename_csv,"w+",newline = "") as csvfile:
        fout = csv.writer(csvfile,delimiter = ",")
        fout.writerow(field_list)
        fout.writerows(mapped_data)

    #convert to html
    df = pd.read_csv(filename_csv, encoding="latin-1")
    df.to_html(filename_html)

    #if no folder named for current day then create one
    if not os.path.isdir(path):
        os.mkdir(path)

    #move files into new directory
    shutil.move(path_html, new_path_html)
    shutil.move(path_csv, new_path_csv)
        

if __name__ == "__main__":
    get_all_data()
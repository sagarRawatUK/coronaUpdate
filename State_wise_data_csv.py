import requests;
import csv;
from bs4 import  BeautifulSoup;

fields = ['Sr.no.','State', 'Total Cases', 'Cured ','Deaths'];
filename = "State_corona_update.csv";

def get_html_data(url):
    data = requests.get(url);
    return data;

def get_corona_detail():
    details = [];
    url = "https://www.mohfw.gov.in/";
    try:
        html_data = get_html_data(url);
    except Exception as e:
        print "Failed to connect to Internet";
        exit();
    soup = BeautifulSoup(html_data.text,"html.parser");
    container = soup.find("table",class_="table").find("tbody").findAll("td");
    with open(filename,'a') as csvfile:
        csvwriter = csv.writer(csvfile);
        csvwriter.writerow(fields);
        for i in range(0,5*32,5):
            num = container[0+i];
            state = container[1+i];
            total = container[2+i];
            cured = container[3+i];
            deaths = container[4+i];
            rows = [num.text,state.text,total.text,cured.text,deaths.text];
            csvwriter.writerows([rows]);



def main():
   get_corona_detail();

main();

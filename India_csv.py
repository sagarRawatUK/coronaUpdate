import requests;
import csv;
from bs4 import  BeautifulSoup;

fields = ['Category','Count'];
filename = "corona_update.csv";


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
    container = soup.find("div",class_="site-stats-count").findAll("li");
    with open(filename,'a') as csvfile:
        csvwriter = csv.writer(csvfile);
        csvwriter.writerow(fields);
        for block in container:
            name = block.find("span");
            count = block.find("strong");
            if name != None or count != None:
                rows = [name.text , count.text];
                csvwriter.writerows([rows]);

def main():
    get_corona_detail();
    
    
main();

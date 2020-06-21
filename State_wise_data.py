import requests;
from bs4 import BeautifulSoup;
import Tkinter as tk;
import time;
import datetime;
from PIL import ImageTk,Image;

import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_html_data(url):
    data = requests.get(url);
    return data;

def get_corona_detail():
    details = "State : Total Cases : Cured : Deaths";
    url = "https://www.mohfw.gov.in/";
    html_data = get_html_data(url);try:
        html_data = get_html_data(url);
    except Exception as e:
        print "Failed to connect to Internet";
        exit();
    soup = BeautifulSoup(html_data.text,"html.parser");
    container = soup.find("table",class_="table").find("tbody").findAll("td");
    for i in range(0,5*32,5):
        #num = container[0+i];
        state = container[1+i];
        total = container[2+i];
        cured = container[3+i];
        deaths = container[4+i];
        details = ''.join([details,'\n',state.text," : ",total.text," : ",cured.text," : ",deaths.text]);
    return details;
        

def main():
   get_corona_detail();
   
def refresh():
    newdata = get_corona_detail();
    print "refreshing....";
    mainlabel['text']= newdata;
root = tk.Tk();
root.geometry("800x800");
root.title("Corona Live Statewise Update India");
f = ("poppins",12,"normal");

image = Image.open(resource_path("icon.png"));
image = image.resize((150,150));
banner = ImageTk.PhotoImage(image);
bannerlabel = tk.Label(root,image=banner);
bannerlabel.pack();

mainlabel = tk.Label(root,text=get_corona_detail(),font = f);
mainlabel.pack();

rebt= tk.Button(root,text="Refresh",font = f,relief = 'solid',height=25,width=40,command=refresh);
rebt.pack();



root.mainloop();

main();

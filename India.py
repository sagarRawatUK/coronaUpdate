import requests;
from bs4 import  BeautifulSoup;
import Tkinter as tk;
import plyer;
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
    details = "";
    url = "https://www.mohfw.gov.in/";
    try:
        html_data = get_html_data(url);
    except Exception as e:
        print "Failed to connect to Internet";
        exit();
    soup = BeautifulSoup(html_data.text,"html.parser");
    container = soup.find("div",class_="site-stats-count").findAll("li");
    for block in container:
        name = block.find("span");
        count = block.find("strong");
        if name != None or count != None:
                details = ''.join([details,'\n',name.text ,":", count.text]);
    return details;
def main():
   get_corona_detail();

def refresh():
    newdata = get_corona_detail();
    print "refreshing....";
    mainlabel['text']= newdata;

root = tk.Tk();
root.geometry("800x600");
root.title("Corona Live Update India");
f = ("poppins",25,"normal");

image = Image.open(resource_path("icon.png"));
image = image.resize((250,250));
banner = ImageTk.PhotoImage(image);
bannerlabel = tk.Label(root,image=banner);
bannerlabel.pack();

mainlabel = tk.Label(root,text=get_corona_detail(),font = f);
mainlabel.pack();

rebt= tk.Button(root,text="Refresh",font = f,relief = 'solid',height=30,width=50,command=refresh);
rebt.pack();



root.mainloop();

main();
    

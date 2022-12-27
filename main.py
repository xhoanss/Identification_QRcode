
import pandas as pd
import requests
import os

#This part of the code downloads images from the website to the local site
def saveFile():
    path = 'captchas'
    df = pd.read_csv("csv/shixi-challenge-filenames.csv", header=None)
    x = df.iloc[:, 0]

    for i in x:
        down_url= "https://cs7ns1.scss.tcd.ie/?shortname=shixi&myfilename="+i
        r = requests.get(down_url)
        img = r.content
        with open('captchas/'+i,'wb') as f:
            f.write(img)



if __name__ == '__main__':
    saveFile()



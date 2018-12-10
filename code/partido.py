# Imports
import requests
import lcddriver
import time
from bs4 import BeautifulSoup
import sys

display = lcddriver.lcd()

# Search for digits on an string
def searchForDigits(s):
   return int(''.join(list(filter(str.isdigit, s))))

try:
    while True:
        # Get the url of the match as an argument
        url = sys.argv[1]
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        score = soup.findAll("span", {"class": "claseR"})
        timer = soup.findAll("span", {"class": "jor-live"})
        name = soup.findAll("b", {"itemprop": "name"})

        # Extract names 
        local = name[0].text
        visitante = name[1].text

        # Extract scores
        local_score = score[0].text
        visitante_score = score[1].timer_txt

        # Extract and parse time
        timer_txt = timer[0].text
        time = searchForDigits(timer_txt)
       
        score_str = local_score + "-" + visitante_score + "     minute: " + str(time)
        names_str = local + " - " + visitante

        # Display strings 
        display.lcd_display_string(score_str, 1)
        display.long_string(names_str, 2)
        
        print(local,"-",visitante,"  minute: ",time)
        time.sleep(15)

except KeyboardInterrupt:   
    print("Cleaning up!")
    display.lcd_clear()

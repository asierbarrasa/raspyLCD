# Imports
import lcddriver
import time
from bs4 import BeautifulSoup
import requests
import sys

display = lcddriver.lcd()

# Search for digits on an string
def searchForDigits(s):
   return int(''.join(list(filter(str.isdigit, s))))

try:    
    while True:
        url = sys.argv[1]
        url_2 = sys.argv[2]

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text,"lxml")
        subs_1 = soup.findAll("span", {"id": "youtube-stats-header-subs"})

        response_2 = requests.get(url_2, headers=headers)
        soup_2 = BeautifulSoup(response_2.text,"lxml")
        subs_2 = soup_2.findAll("span", {"id": "youtube-stats-header-subs"})

        subs_1_txt = searchForDigits(subs_1[0].text)
        subs_2_txt = searchForDigits(subs_2[0].text)

        print("name_1 ",subs_1_txt)
        print("name_2:  ",subs_2_txt)

        string_1 = "name1:  " + str(subs_1_txt)
        string_2 = "name2:    " + str(name_txt2)

        display.lcd_display_string(string_1, 1)
        display.lcd_display_string(string_2, 2)

        # Update every 15 seconds
        time.sleep(15)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    display.lcd_clear()
    print("Cleaning up!")
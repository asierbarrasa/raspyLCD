# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import lcddriver
import time
from bs4 import BeautifulSoup
import requests


# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

try:    
    while True:
        url = "https://socialblade.com/youtube/user/thegrefg"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text,"lxml")
        name = soup.findAll("span", {"id": "youtube-stats-header-subs"})
        name_txt = int(''.join(list(filter(str.isdigit, name[0].text))))
        print(name_txt)
        print("Grefg ",name_txt)
        s = "Grefg:  " + str(name_txt)
        display.lcd_display_string(s, 1)
        url2 = "https://socialblade.com/youtube/channel/UC8cO6QIqDJv1RdruiXpiQvA"
        headers2 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response2 = requests.get(url2, headers=headers)
        soup2 = BeautifulSoup(response2.text,"lxml")
        name2 = soup2.findAll("span", {"id": "youtube-stats-header-subs"})
        name_txt2 = int(''.join(list(filter(str.isdigit, name2[0].text))))
        print("SpiuK:  ",name_txt2)
        t = "SpiuK:    " + str(name_txt2)
        display.lcd_display_string(t, 2)

        time.sleep(15)
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    display.lcd_clear()
    print("Cleaning up!")
# Import requests (to download the page)
import requests
import lcddriver
import time


# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time


try:
    def long_string(display, text = '', num_line = 1, num_cols = 20):
        if(len(text) > num_cols):
            display.lcd_display_string(text[:num_cols],num_line)
            time.sleep(1)
            for i in range(len(text) - num_cols + 1):
                text_to_print = text[i:i+num_cols]
                display.lcd_display_string(text_to_print,num_line)
                time.sleep(0.4)
        else:
            display.lcd_display_string(text,num_line)
    while True:
       #url = input("https://www.resultados-futbol.com/partido/X/X")
        url = "https://www.resultados-futbol.com/partido/Juventus-Fc/Internazionale"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        mydivs = soup.findAll("span", {"class": "claseR"})
        timer = soup.findAll("span", {"class": "jor-live"})
        local = mydivs[0].text
        visitante = mydivs[1].text
        timer_txt = timer[0].text
        t = int(''.join(list(filter(str.isdigit, timer_txt))))
        name = soup.findAll("b", {"itemprop": "name"})
        x = local + "-" + visitante + "     time: " + str(t)
        y = name[0].text + " - " + name[1].text
        display.lcd_display_string(x, 1)
        #display.lcd_display_string(name[0].text,2)
        long_string(display, y, 2)
        print(local,"-",visitante,"time: ",t)
        time.sleep(15)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()

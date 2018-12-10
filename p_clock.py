# Imports
import lcddriver
import time
import datetime

display = lcddriver.lcd()

try:
    while True:
        # Print the date
        display.lcd_display_string(str(time.strftime("%d/%m/%Y")), 1) 
        # Print the time
        display.lcd_display_string(str(time.strftime("%H:%M:%S")), 2) 
    
except KeyboardInterrupt: 
    print("Cleaning up!")
    display.lcd_clear()

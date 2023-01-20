import os
import pyautogui as pe
import time
import subprocess

# Start Brave browser (replace this with the directory of any browser you use)
os.startfile('C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe')
time.sleep(1)

# Navigate to first Discord channel
pe.typewrite('https://discord.com/channels/828151284233535488/1029509542331039794')
time.sleep(0.1)
pe.press('enter')
time.sleep(1)

# Open new tab
pe.hotkey('ctrl','t')
time.sleep(1)

# Navigate to second Discord channel
pe.typewrite('https://discord.com/channels/828151284233535488/1056065889591623720')
time.sleep(0.1)
pe.press('enter')

# Move cursor to a specific location (the previous reply)
pe.moveTo(581,858,0.1)

# Perform a loop for 10 iterations, edit to edit how many time you want the two bots to message each other
for i in range(10): 
    # Click, copy, switch tabs, paste, and press enter
    pe.click(),pe.click(),pe.click(), # Triple click To select the whole reply
    time.sleep(0.1),
    pe.hotkey('ctrl','c'), # Copy the reply
    time.sleep(0.7),
    pe.click(),
    time.sleep(0.1),
    pe.hotkey('ctrl','tab'), # Switch to other channel
    time.sleep(0.2),
    pe.click(),
    time.sleep(0.6),
    pe.hotkey('ctrl','v'), # Paste the reply
    time.sleep(0.1),
    pe.press('enter'), # Send the reply
    time.sleep(6) # Wait for the response and repeat

# Type execution complete
pe.typewrite('Execution complete', 0.2)

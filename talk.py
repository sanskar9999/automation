import os
import pyautogui as pe
import time
import subprocess

# Start Brave browser
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

# Move cursor to a specific location (the text above)
pe.moveTo(581,858,0.1)

# Perform a loop for 10 iterations
for i in range(10): 
    # Click, copy, switch tabs, paste, and press enter
    pe.click(),pe.click(),pe.click(),
    time.sleep(0.1),
    pe.hotkey('ctrl','c'),
    time.sleep(0.7),
    pe.click(),
    time.sleep(0.1),
    pe.hotkey('ctrl','tab'),
    time.sleep(0.2),
    pe.click(),
    time.sleep(0.6),
    pe.hotkey('ctrl','v'),
    time.sleep(0.1),
    pe.press('enter'),
    time.sleep(6)

# Type execution complete
pe.typewrite('Execution complete', 0.2)

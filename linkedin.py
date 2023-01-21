import os # importing os module for interacting with the system
import pyautogui as pe # importing pyautogui for automating GUI actions
import time # importing time module for adding delays

# Opening a text file which contains the post content
os.startfile('C:/Users/91800/Desktop/post.txt') 
time.sleep(1) # waiting for the text file to open

# Selecting the text in the file
pe.hotkey('ctrl','a')
time.sleep(0.5) # waiting for the text to be selected

# Copying the text
pe.hotkey('ctrl','c')
time.sleep(0.5) # waiting for the text to be copied

# Closing the text file
pe.hotkey('alt','f4')
time.sleep(0.2) # waiting for the text file to close

# Opening Brave browser
os.startfile('C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe')
time.sleep(1) # waiting for the browser to open

# Navigating to LinkedIn homepage
pe.typewrite('https://www.linkedin.com/feed/',0.02)
time.sleep(0.1) # waiting for the URL to be typed
pe.press('enter') # pressing enter to navigate to the URL
time.sleep(8) # waiting for the LinkedIn homepage to load

# Clicking on create post button
pe.moveTo(692,248,0.3) # moving the cursor to the create post button
time.sleep(5) # waiting for the cursor to reach the button
pe.click() # clicking on the create post button

#Pasting the copied text from the text file
pe.moveTo(610,397,0.1) # moving the cursor to the text area in the create post form
pe.click() # clicking on the text area
time.sleep(1) #waiting for the cursor to reach the text area
pe.hotkey('ctrl','v') # pasting the copied text
time.sleep(2) # waiting for the text to be pasted

# Typing additional text in the post
pe.typewrite('Ill let you out on a little secret ... This post has been made by automation aswell')

# Submitting the post
pe.moveTo(1282,676,0.3) # moving the cursor to the post button
pe.click() # clicking on the post button
pe.press('enter') # pressing enter to submit the post

#this app allows you to block access to websites of your choices in anytime you want. it can be used as a parental control apps
#it blocks the websites by redirecting the links to those websites to the localhost ip by adding entries to the windows host file
# this app is designed to be scheduled on every time windows lunchs and will stay running in the background
#save the script as .pyw to be run in the background

import time
from datetime import datetime as dt

host_temp='./hosts'  #used for testing
host_path='C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
sites_list= ['www.facebook.com','facebook.com'] # websites to be blocked
working_hours=[8,12]

while True :
    # the program check every 60 sec if the actual time is between working hours , if it's true
    # the program adds the items on the list sitelist to the host file with the ip of localhost so they will be redirected
    if dt(dt.now().year,dt.now().month,dt.now().day,working_hours[0]) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,working_hours[1]):
        #print('working hours') # used only for testing
        with open(host_temp,'r+') as file :
            content= file.read()
            for w in sites_list:
                if w in content :
                    pass
                else :
                    file.write(redirect + '   ' + w +'\n')
    else :
        #in this part, we are out of selected working hours, so we want this part to delete the websites above from the host file
        #we can do this by checking each line , if it's note in the website list, we will write it in the host file
        with open(host_temp,'r+') as file :
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in sites_list):
                    file.write(line)
        file.truncate() #this line is used so the text will be writen only once
        # print("enjoy your free time")  # this line is used for testing


    time.sleep(60) # the process will be repeated every 60 second

from selenium import webdriver
from time import sleep
import PySimpleGUI as sg

i=0
while True:
    i=i

sg.theme('DarkAmber')

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get('https://web.whatsapp.com/')

layout = [  [sg.Text("Image[0] or Text[1]?"), sg.Input(key='Input')],
            [sg.Text("How often do you wanna send it?"), sg.Input(key='count')],
            [sg.Text("Who do you wanna send it to?"), sg.Input(key='Name')],
            [sg.Text("Text oder Pfad:"), sg.Input(key='content')],
            [sg.Text("Press enter when you scanned the QR Code"), sg.Button("Start"), sg.Exit()]]

window = sg.Window('SpamBot', layout)

while True:

    event, values = window.read()
    print(event, values)       
    if event in (None, 'Exit'):      
        break
    if event in (None, 'Start'):
        switch = values['Input']
        count = int(values['count'])
        name = values['Name']

        if(switch=="0"):
            filepath = values['content']

            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()

            for i in range(count):

                attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
                attachment_box.click()

                image_box = driver.find_element_by_xpath(
                    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(filepath)

                sleep(3)

                send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
                send_button.click()
        else:
            text = values['content']

            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()

            for i in range(count):

                text_field = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                text_field.send_keys(text)

                send_button = driver.find_element_by_class_name('_3M-N-')
                send_button.click()
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pylint
import os
import sys
import winsound
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver1 = webdriver.Chrome(PATH)


duration = 1000  # milliseconds
freq = 600  # Hz

site1 = "https://www.doctolib.fr/vaccination-covid-19/sainte-marie-du-mont?ref_visit_motive_ids[]=6970&ref_visit_motive_ids[]=7005&force_max_limit=2"
#site1 = "https://www.doctolib.fr/vaccination-covid-19/sainte-marie-du-mont?ref_visit_motive_ids[]=6970&ref_visit_motive_ids[]=7005&ref_visit_motive_ids[]=7107&ref_visit_motive_ids[]=7945"
driver1.get(site1)
a = None
while True : 
   try :
      
      a = driver1.find_element_by_class_name("availabilities-slot")
   except :
      print("NOT FOUND")
   if a != None:
      print("ALERT VACCIN FOUND!!! https://www.doctolib.fr/vaccination-covid-19/sainte-marie-du-mont?ref_visit_motive_ids[]=6970&ref_visit_motive_ids[]=7005&force_max_limit=2")
      winsound.Beep(freq, duration)
      
   driver1.refresh()
   time.sleep(5)





print((f.text).split("\n")[0])
                    print(e[2][0])
                    if (f.text).split("\n")[0] == e[2][0] and isGood((f.text).split[7]):
                        bingo = 1
                        messagebox.showerror(title="BADURL", message="BINGO!!!")
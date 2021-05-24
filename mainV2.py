import tkinter
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pylint
import os
import sys
import winsound
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
soundalert = False
duration = 1000  # milliseconds
freq = 600  # Hz

PATH = "./chromedriver.exe"
driver1 = None

checkboxL = []
L = []
toSurveiller = []



class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def peuplementDelaListe():
    driver1 = webdriver.Chrome(PATH)
    urldocto = inpute.get()
    try:
        driver1.get(urldocto)
    except:
        messagebox.showerror(title="BADURL", message="URL Invalide")
        return

    
    time.sleep(2)
    L.clear()
    try:
        results = driver1.find_elements(By.CLASS_NAME,"dl-search-result")
    except:
        print("Erreur lors de la recuperation des résultats")
        return
    
    for e in results:
        e.find_element(By.CLASS_NAME, "dl-search-result-name")
        L.append((e.text).split("\n"))
    driver1.close()
    showList()


def showList():
    checkboxL.clear()
    for e in L:
        crVar = IntVar()
        crCB = Checkbutton(scrollFrame.scrollable_frame,text=e[0],variable=crVar).pack()
        checkboxL.append((crCB,crVar,e))
    return


def surveiller():
    surete = 0
    toobad="Aucun rendez-vous de vaccination n'est disponible dans ce lieu d'ici demain soir."
    driver2 = webdriver.Chrome(PATH)
    driver2.get(inpute.get())
    bingo = 0
    toSurveiller.clear()
    for e in checkboxL:
            if e[1].get() == 1:
                toSurveiller.append(e[2][0])
                
    while bingo == 0 :
        driver2.refresh()
        time.sleep(2)
        results = driver2.find_elements(By.CLASS_NAME,"dl-search-result")
        for i in results:
            str = i.text
            for j in toSurveiller:
                if str.find(j) != -1 and str.find(toobad) == -1 and surete == 4:
                    bingo=1
                    messagebox.showinfo(title="BINGO", message="VACCIN FOUND")
                    surete = surete +1
                else:
                    surete =0


        
                    
                    






            
 
window=Tk()
window.title('VITEUNVACCIN')
labelink = Label(window,text="Lien Doctolib avec vos filtres",fg='black')
labelink.place(x=170,y=30)
inpute = Entry(window)
inpute.place(x=180,y=60)
scanBtn = Button(window,text="Scan",command=peuplementDelaListe, fg='blue')
scanBtn.place(x=200,y=90)
scrollFrame = ScrollableFrame(window)
scrollFrame.place(x=30,y=110)
survBtn = Button(window,text="Surveiller",command=surveiller, fg='blue')
survBtn.place(x=200,y=400)
window.geometry("500x500+10+20")
window.mainloop()








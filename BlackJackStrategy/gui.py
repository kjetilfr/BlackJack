#Import the required libraries
from tkinter import *
from tkinter import ttk
from main import Start

#Create an instance of Tkinter Frame
win = Tk()

Label(win, text='Card 1').grid(row=0)
Label(win, text='Card 2').grid(row=1)
Label(win, text='Dealer Card').grid(row=2)

e1 = Entry(win)
e2 = Entry(win)
e3 = Entry(win)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


#Set the geometry
win.geometry("700x250")

# Define a function to return the Input data
def get_data():
   card1 = label.config(text= e1.get(), font= ('Helvetica 13'))
   card2 = label2.config(text=e2.get(), font=('Helvetica 13'))
   dealerCard = label3.config(text=e3.get(), font=('Helvetica 13'))
   return [card1, card2], dealerCard


#Inititalize a Label widget
label= Label(win, text="", font=('Helvetica 13'))
label.grid()
label2= Label(win, text="", font=('Helvetica 13'))
label2.grid()
label3= Label(win, text="", font=('Helvetica 13'))
label3.grid()

#Create a Button to get the input data
data = ttk.Button(win, text= "Play Hand", command=lambda: get_data).grid(row=4, column=1)
#ttk.grid(row=4, column=1)

ttk.Button(win, text= "Start", command=lambda: Start([1,2], 4)).grid()

win.mainloop()

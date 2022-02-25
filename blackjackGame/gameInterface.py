from textwrap import fill
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color
root = Tk()
frm = Frame(root)
# root.geometry("550x350")
frm.grid()
frm.config(padx=10, pady=10, relief="groove", bd=5)
frm.pack(fill=BOTH)


coinLabel = Label(frm, text="Coins : 1" ).grid(column=0, row=0, sticky=N+W)
# coinLabel.pack(side="left");
turnLabel = Label(frm, text="Turn : 1").grid(column=0, row=1)
turnLabel = Label(frm, text="").grid(column=1, row=1)
turnLabel = Label(frm, text="").grid(column=2, row=1)

croupierId = Label(frm, text=" Croupier").grid(column=5, row=0)
handOfCroupier = Label(frm, text="20").grid(column=5, row=1)
statusLabel = Label(frm, text="Winner is ").grid(column=5, row=3)
handOfPlayer = Label(frm, text="18").grid(column=5, row=5)
playerId = Label(frm, text="Player").grid(column=5, row=6)

playerCardOne = LabelFrame(frm, text="One", width=35, height=75).grid(column=3, row=2)
playerCardTwo = LabelFrame(frm, text="Two", width=35, height=75).grid(column=4, row=2)
playerCardThree = LabelFrame(frm, text="Three", width=35, height=75).grid(column=5, row=2)
playerCardFour = LabelFrame(frm, text="Four", width=35, height=75).grid(column=6, row=2)
playerCardFive = LabelFrame(frm, text="One", width=35, height=75).grid(column=7, row=2)

croupierCardOne = LabelFrame(frm, text="One", width=35, height=75).grid(column=3, row=4)
croupierCardTwo = LabelFrame(frm, text="Two", width=35, height=75).grid(column=4, row=4)
croupierCardThree = LabelFrame(frm, text="Three", width=35, height=75).grid(column=5, row=4)
croupierrdFour = LabelFrame(frm, text="Four", width=35, height=75).grid(column=6, row=4)
croupierCardFive = LabelFrame(frm, text="Five", width=35, height=75).grid(column=7, row=4)

turnLabel = Label(frm, text="").grid(column=8, row=1)
turnLabel = Label(frm, text="").grid(column=9, row=1)
turnLabel = Label(frm, text="Created By\n JhashMe").grid(column=10, row=0)

Questions = Label(frm, text="Do you Want").grid(column=3, row=7, columnspan=3)

yesButton = Button(frm, text="Yes").grid(column=4, row=8)
notButton = Button(frm, text="No").grid(column=6, row=8)

root.mainloop()
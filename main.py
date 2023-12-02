from  tkinter import *
import requests,random

respones= requests.get("https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=boolean")

lists=[]
for item in respones.json()['results']:
	lists.append(item)
def creat_qrustion():
	ask=random.choices(lists)
	canvas.itemconfig(qs,text=ask[0]['question'])
	print(ask[0])

bgColor = "#393E46"
window = Tk()
window.config(bg=bgColor,padx=20,pady=20)
window.minsize(400,700)
label=Label(text="your score: 0",bg=bgColor,font=("italic",25,"bold"),fg="#F7F7F7")
label.pack()
canvas= Canvas(width=400,height=400,bg="#F2E7D5")
qs=canvas.create_text(200,200,text="")
canvas.pack()
creat_qrustion()


window.mainloop()
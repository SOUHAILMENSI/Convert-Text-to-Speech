import pyttsx3
from tkinter import *
import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.title("Text to speech")
root.geometry("400x500")

engine = pyttsx3.init()


def check():

    var_new=e1.get()
    if len(var_new)==0:
        messagebox.showerror("Enter Again","Dont Leave the input space!!")
    else:
        pass

def speak():
    try:
        check()

        """ RATE"""
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        engine.setProperty('rate', 150)  # setting up new voice rate

        """VOLUME"""
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        print(volume)  # printing current volume level
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

        """VOICE"""
        voices = engine.getProperty('voices')  # getting details of current voice
        # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 1 for female

        for voice in voices:
            print("Voice:")
            print(" - ID: %s" % voice.id)
            print(" - Name: %s" % voice.name)
            print(" - Languages: %s" % voice.languages)
            print(" - Gender: %s" % voice.gender)
            print(" - Age: %s" % voice.age)


        new_var=e1.get()
        engine.say(new_var)

        engine.runAndWait()
    except:
        messagebox.showerror("Wrong input","Enter Correct Input")

l2=Label(root, text="Enter Text Below",font=("MS Sans Serif",15), fg="black")
l2.pack(padx=30,pady=40)

ans=StringVar()
e1=Entry(root,font=("Verdana",10),text=ans,width=40)
e1.pack()


btn=Button(root,text="Speak Now!",fg="blue",command=speak)

btn.pack(padx=50,pady=50, ipadx=15,ipady=10)

root.resizable(width=0,height=0)

if __name__=="__main__":
    root.mainloop()
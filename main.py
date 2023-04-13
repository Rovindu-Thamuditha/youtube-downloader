#Importing modules
import io
import os
import tkinter
import pytube
import base64
import urllib
import tkinter as tk
from tkinter import * 
from tkinter import font 
from tkinter.ttk import *
from pytube import YouTube
from PIL import ImageTk,Image
from tkinter import filedialog
from urllib.request import urlopen
from tkinter.constants import ANCHOR

#base64 image encoder
base64.encodestring = base64.encodebytes

#window configurations
window = tk.Tk()
window.title("YouTube Video Downloader")
window.resizable(width=False,height=False)
window.geometry ('950x230')
window.iconbitmap ('yt.ico')

img = ImageTk.PhotoImage(Image.open("img.png"))
panel = Label(window, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.place(x=0, y=0, relwidth=1, relheight=1)


#definitions
def browse():
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def Download_Video():
    try:  
        vid_url = str(video_url.get())
        link = YouTube(vid_url)
        save_location = str(folder_path.get())
        video = link.streams.get_highest_resolution()
        video.download(save_location)
        message = tkinter.messagebox.showinfo(title="Download Report", message="Your Video Downloaded Sucessfully!")

    except:
        message = tkinter.messagebox.showerror(title="Error",message="An Error occured. Check the video before downloading.")

def Check_Video():
    try:
        vid_url = str(video_url.get())
        link = YouTube(vid_url)
        title = link.title
        message = tkinter.messagebox.showinfo(title="Video Information", message=title)
    except:
        message = tkinter.messagebox.showerror(title="ERROR", message="Please enter a valid url.")



#string variables
video_url = StringVar()
folder_path = StringVar()

#!--Interface--!

url_ask = tk.Label (
    text="Enter your YouTube video url" , 
    font = ('calibri',20),
    bg = 'snow' 
)

url_ask.pack()


#video url
url = tk.Entry (
    font = ('calibri',15),
    width=72 , 
    textvariable=video_url
)

url.place (x = 52 ,y = 70)

#Browser Button
browse_btn = tkinter.Button(
    window,
    text='Browse',
    font = ('calibri',16) ,
    bg='powder blue' ,
    fg='snow',
    width='10' ,
    command=browse
)

browse_btn.place (x=815 , y=60)

tkinter.Button(window,text = 'DOWNLOAD VIDEO', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=490 ,y = 140)

tkinter.Button(window,text = 'CHECK VIDEO', font = 'arial 15 bold' ,fg="white",bg = 'red', padx = 2,command=Check_Video).place(x=310 ,y = 140)


version = tk.Label (
    text="v1.0.1"
)
version.place (x = 850 , y =200)


window.mainloop()
from tkinter import *
from PIL import Image, ImageTk
import pywhatkit

tk = Tk()
tk.title('YouTube')
tk.geometry('500x500')

def playSong():
    song = song_music.get()
    pywhatkit.playonyt(song)

bg = ImageTk.PhotoImage(file = 'spotify.png')
bgi = Label(tk, image=bg).place(x = 0, y = 0 , relwidth= 1 , relheight= 1)

song_music = StringVar()
song_entry = Entry(tk, textvariable=song_music, bd=2)
song_entry.place(x = 180, y= 100)

button = Button(tk, text='Search', width=12, height=1, command=playSong)
button.place(x = 190, y = 130)


tk.mainloop()
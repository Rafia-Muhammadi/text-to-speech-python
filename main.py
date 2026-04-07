import tkinter as tk
from tkinter import ttk, filedialog
import pyttsx3
from gtts import gTTS
import pygame

# initialize engines
engine = pyttsx3.init()
pygame.mixer.init()

# Speak using pyttsx3
def speak():
    progress.start()

    text = txt.get("1.0","end-1c")

    engine.stop()
    engine.setProperty('rate', tempo.get())
    engine.setProperty('volume', volume.get())

    voices = engine.getProperty('voices')

    if voice.get() == "Male":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

    progress.stop()


# Save and play MP3
def save_mp3():
    text = txt.get("1.0","end-1c")
    lang = language.get()

    file = filedialog.asksaveasfilename(defaultextension=".mp3",
                                        filetypes=[("MP3 files","*.mp3")])

    if file:
        tts = gTTS(text=text, lang=lang)
        tts.save(file)

        pygame.mixer.music.load(file)
        pygame.mixer.music.play()


# Clear text
def clear_text():
    txt.delete("1.0","end")


# Window
root = tk.Tk()
root.title("Text to Speech Converter - Rafia")
root.geometry("650x420")
root.configure(bg="#1e1e1e")

# Title
title = tk.Label(root,
                 text="Text To Speech Converter",
                 font=("Arial",20,"bold"),
                 bg="#1e1e1e",
                 fg="white")
title.pack(pady=10)

# Text box
txt = tk.Text(root,
              height=6,
              width=50,
              font=("Arial",12),
              bg="#2b2b2b",
              fg="white")
txt.pack(pady=10)

# Controls frame
frame = tk.Frame(root,bg="#1e1e1e")
frame.pack()

# Volume
tk.Label(frame,text="Volume",bg="#1e1e1e",fg="white").grid(row=0,column=0,padx=10,pady=5)
volume = tk.DoubleVar(value=1.0)
tk.Scale(frame,from_=0,to=1,resolution=0.1,
         orient="horizontal",
         variable=volume).grid(row=0,column=1)

# Speed
tk.Label(frame,text="Speed",bg="#1e1e1e",fg="white").grid(row=1,column=0,padx=10,pady=5)
tempo = tk.IntVar(value=150)
tk.Scale(frame,from_=50,to=300,
         orient="horizontal",
         variable=tempo).grid(row=1,column=1)

# Voice
tk.Label(frame,text="Voice",bg="#1e1e1e",fg="white").grid(row=2,column=0,padx=10,pady=5)
voice = ttk.Combobox(frame,values=["Male","Female"])
voice.set("Female")
voice.grid(row=2,column=1)

# Language
tk.Label(frame,text="Language",bg="#1e1e1e",fg="white").grid(row=3,column=0,padx=10,pady=5)
language = ttk.Combobox(frame,values=["English","Hindi","Urdu","Telugu"])
language.set("en")
language.grid(row=3,column=1)

# Buttons
btn_frame = tk.Frame(root,bg="#1e1e1e")
btn_frame.pack(pady=20)

ttk.Button(btn_frame,text="Speak",command=speak).grid(row=0,column=0,padx=10)
ttk.Button(btn_frame,text="Save MP3",command=save_mp3).grid(row=0,column=1,padx=10)
ttk.Button(btn_frame,text="Clear",command=clear_text).grid(row=0,column=2,padx=10)

# Progress bar
progress = ttk.Progressbar(root,mode="indeterminate")
progress.pack(fill="x",padx=40,pady=10)

root.mainloop()

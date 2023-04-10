import tkinter as tk
import random
from pytube import YouTube
from tkinter import filedialog

colors = ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3', '#00BCD4', '#009688', '#4CAF50', '#FFC107', '#FF9800', '#795548']

def change_background():
    color = random.choice(colors)
    root.configure(background=color)

    # update foreground color based on background color
    if color in ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#795548']:
        output_color = 'white'
    else:
        output_color = 'black'
    status_label.config(fg=output_color)
    filepath_label.config(fg=output_color)

    # set font size to 22
    output_font = ('Arial', 22)
    status_label.config(font=output_font)
    filepath_label.config(font=output_font)

    root.after(5000, change_background)

def get_video_details():
    url = entry.get()
    yt = YouTube(url)

    # set video details
    title_label.config(text='Title: ' + yt.title)
    author_label.config(text='Author: ' + yt.author)
    views_label.config(text='Views: ' + str(yt.views))
    length_label.config(text='Length: ' + str(yt.length) + ' seconds')

def download_video():
    url = entry.get()
    yt = YouTube(url)

    # open file dialog box to select download directory
    download_dir = filedialog.askdirectory()
    if download_dir:
        stream = yt.streams.get_by_itag(22) # choose the format you want to download
        stream.download(download_dir)
        status_label.config(text='Download completed!', fg='green')
        filepath_label.config(text='File saved at: ' + download_dir, fg='green')

        # center the output screen
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        x = int(w/2 - root.winfo_width()/2)
        y = int(h/2 - root.winfo_height()/2)
        root.geometry("+{}+{}".format(x, y))

def clear_output():
    status_label.config(text='', fg=output_color)
    filepath_label.config(text='', fg=output_color)

root = tk.Tk()
root.title('YouTube Video Downloader')

output_color = 'red'

url_label = tk.Label(root, text='Enter YouTube video URL:')
url_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(ipadx=100, ipady=5, padx=10, pady=5)

details_button = tk.Button(root, text='Get Video Details', command=get_video_details)
details_button.pack(pady=10)

title_label = tk.Label(root, text='')
title_label.pack(pady=5)

author_label = tk.Label(root, text='')
author_label.pack(pady=5)

views_label = tk.Label(root, text='')
views_label.pack(pady=5)

length_label = tk.Label(root, text='')
length_label.pack(pady=5)

download_button = tk.Button(root, text='Download', command=download_video)
download_button.pack(pady=10)

clear_button = tk.Button(root, text='Clear Output', command=clear_output)
clear_button.pack(pady=10)

status_label = tk.Label(root, text='')
status_label.pack(pady=5)

filepath_label = tk.Label(root, text='')
filepath_label.pack(pady=5)

change_background() # start changing background color

root.mainloop()

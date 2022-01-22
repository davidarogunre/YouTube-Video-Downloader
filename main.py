import tkinter as tk
from tkinter import Label, Entry, Button
from pytube import YouTube


class DownloaderUI(tk.Tk):


    def download(self, website, directory):
        yt = YouTube(website)
        video = yt.streams.get_by_itag(22)
        video.download(directory)
    def __init__(self):
        
        tk.Tk.__init__(self)
        
        self.geometry("440x400")
        self.resizable(0,0)
        self.title("YouTube Video Downloader")
        self.welcome = Label(text="Welcome to Youtube Video Dowloader", font =('consolas', 14)).grid(row=0,column=0,columnspan=2)
        self.space = Label("").grid(row=1)
        self.urlgetter_text = Label(text='Write YouTube Video Url: ', font=('consolas', 13)).grid(row=2,column= 0)
        self.urlgetter = Entry(font=('consolas'), width=20)
        self.urlgetter.grid(row=2, column=1)
        self.space = Label("").grid(row=3)
        self.directory_text = Label(text='Write Directory: ', font=('consolas', 13)).grid(row=4,column= 0,padx=(0,50))
        self.directory = Entry(font=('consolas'), width=20)
        self.directory.grid(row=4, column=1)
        self.button = Button(text='Download', font=('consolas', 13), command = lambda: self.download(self.urlgetter.get(), self.directory.get())).grid(row = 5, column=0)
    
    
        

    

    
if __name__ == '__main__':
    DownloaderUI()
    tk.mainloop()

    

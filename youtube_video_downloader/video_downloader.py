from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from threading import *
import tkinter.messagebox as tmsg
import tkinter as tk


FolderName = ""
fileSizeInBytes = 0
MaxFileSize = 0

def openDirectory():
    global FolderName
    FolderName=filedialog.askdirectory()
    if(len(FolderName)>1):
        fileLocation.config(text=f"Location-{FolderName}",fg="blue")
    else:
        fileLocation.config(text="Choose Location",fg="red")

def progress(streaNone, chunk=None,bytes_remaining=None):
  file_downloaded=fileSizeInBytes-bytes_remaining
  per=(file_downloaded/fileSizeInBytes)*100
  downloadButton.config(text="{:00.0f} % downloaded".format(per),bg="white")


def DownloadFile():
    global MaxFileSize,fileSizeInBytes,FolderName
    choice=youtubeChoices.get()
    video_link=youtubeEntry.get()

    if (len(FolderName) < 1):
        tmsg.showerror("Error", "Choose Location")
        openDirectory()
    downloadButton.config(text="Please Wait",fg="black")
    downloadButton.config(state=DISABLED)


    if(video_link.startswith("https")):

        if(len(video_link)>1):
            yt=YouTube(video_link,on_progress_callback=progress)
            downloadButton.config(text="Downloading", fg="black")
            youtubeEntryError.config(text=f"Name-{yt.title}",fg="blue",font="lucida 10 bold")

            if choice==downloadChoices[0]:
                message.config(text="Status:720p video file is downloading")
                selected_choice=yt.streams.filter(progressive=True).first()
            elif choice == downloadChoices[1]:
                message.config(text="Status-360p video file is downloading")
                selected_choice = yt.streams.filter(progressive=True,res="360p").first()
            elif choice==downloadChoices[2]:
                message.config(text="Status-144p video file is downloading")
                selected_choice = yt.streams.filter(progressive=True,file_extension="mp4").last()
            elif choice==downloadChoices[3]:
                message.config(text="Status-3gp file is downloading")
                selected_choice = yt.streams.filter(file_extension="3gp").first()
            elif choice==downloadChoices[4]:
                message.config(text="Status-Only Audio file is downloading")
                selected_choice = yt.streams.filter(only_audio=True).first()
            else:
                tmsg.showerror("Error", "Choose Download Option")
                downloadButton.config(text="Download", fg="black", bg="grey")
                downloadButton.config(state=NORMAL)

            fileSizeInBytes=selected_choice.filesize
            MaxFileSize=fileSizeInBytes/1024000
            MB='{:.2f}'.format(MaxFileSize)+"MB"
            filesize.config(text=f"File Size-{MB}",fg="blue")
            # Download the file
            selected_choice.download(FolderName)
            tmsg.showinfo("Success", f"File Downloaded Successfully \n Location-{FolderName}")
            downloadButton.config(text="Download", fg="black",bg="grey")
            downloadButton.config(state=NORMAL)
            reset()
        else:
           tmsg.showerror("Error","Provide Youtube Link")
           downloadButton.config(text="Download", fg="black")
           downloadButton.config(state=NORMAL)
           reset()
    else:
        tmsg.showerror("Error", "Provide Valid Youtube Link")
        downloadButton.config(text="Download", fg="black")
        downloadButton.config(state=NORMAL)
        reset()

def reset():
    youtubeEntryVar.set("")
    youtubeChoices.delete(0, END)
    fileLocation.config(text="Location", fg="blue")
    youtubeEntryError.config(text="File Name", fg="blue")
    message.config(text="Status", fg="blue")
    filesize.config(text="File Size", fg="blue")

def downloadthread():
    thread = Thread(target=DownloadFile)
    thread.start()


root = Tk()
root.title("Video Downloader")
# root.wm_iconbitmap(r"download.ico")
# p1=PhotoImage(file='download1.png')
# root.iconphoto(False,'download1.png')

# root.tk.call('wm','iconphoto',root._w,tk.PhotoImage(file='download.ico'))

w = 600
h = 600

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.config(bg="black")
root.resizable(False,False)

title=Label(root,text="Youtube Video Downloader",fg="red",font="lucida 20 bold",bg="black")
title.pack()

link=Label(root,text="Paste Link Below",fg="green",bg="black",font="lucida 15 bold")
link.pack()

youtubeEntryVar = StringVar()
youtubeEntry = Entry(root,textvariable=youtubeEntryVar,width=50,font="lucida 15 bold")
youtubeEntry.pack(pady=20,ipady=10)

# when link is wrong print this label
youtubeEntryError = Label(root, fg="blue",text="File Name", font="lucida 15 bold",bg="black")
youtubeEntryError.pack()

# Asking where to save file label
SaveLabel = Label(root,text="Choose Path", fg="green",font="lucida 15 bold",bg="black")
SaveLabel.pack(pady=10)

# Asking where to save file Button
SaveEntry = Button(root, width=20, bg="grey", fg="black",text="Browse", font="arial 15 bold",command=openDirectory)
SaveEntry.pack()

# Entry label if user don`t choose directory
fileLocation = Label(root,text="Location", font="lucida 15 bold",bg="black",fg="blue")
fileLocation.pack(pady=5)

# what to download choice
youtubeChooseLabel = Label(root,text="Choose Download Option ",font="lucida 15 bold",bg="black",fg="green")
youtubeChooseLabel.pack(pady=10)

# Combobox with three choices:
downloadChoices = ["720p","360p","144p","3gp","Only_audio"]
youtubeChoices = ttk.Combobox(root, values=downloadChoices,font="lucida 15 bold")
youtubeChoices.pack(ipady=5)

downloadButton = Button(root,text="Download", width=20, bg="grey",fg="black", font="arial 15 bold",command=downloadthread)
downloadButton.pack(pady=20)

message=Label(root,text="Status", font="lucida 20 bold",bg="black",fg="blue")
message.pack(pady=5)

filesize=Label(root,text="File Size", font="lucida 20 bold",bg="black",fg="blue")
filesize.pack(pady=5)

def doSomething():
    # check if saving
    # if not:
    a=tmsg.askquestion('Exit Application', 'Do you really want to exit?')
    if a=='yes':
        root.quit()
    else:
        pass

root.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window



root.mainloop()
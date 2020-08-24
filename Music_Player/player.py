from tkinter import *
import pygame
from tkinter import filedialog
import tkinter.messagebox as tmsg
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root=Tk()
root.title("MP3 Player")
w = 570
h = 400

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False,False)
root.config(bg="grey")

# Initializee Pygame Mixer
pygame.mixer.pre_init(48000,-16,2,1024*3)
pygame.mixer.init(frequency=44100)


# FolderName = ""
# Add Song Function
def add_song():
    # global FolderName
    # FolderName = filedialog.askdirectory()
    song=filedialog.askopenfilename(initialdir='D:/Songs',title='Choose A Song',filetypes=(("mp3 files","*.mp3"), ))
    # print(song)
    # song=song.replace("D:/Songs/","")
    # song = song.replace(".mp3", "")
    songbox.insert(END,song)

def play_time():
    if stopped:
        return
    # Grab Current Song Elapsed Time
    current_time = pygame.mixer.music.get_pos() / 1000
    # Throw up temporary label to get data
    # slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')
    # convert to time format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    # Get Currently Playing Song
    # current_song = song_box.curselection()
    # Grab song title from playlist
    song = songbox.get(ACTIVE)
    # Load Song with Mutagen
    song_mut = MP3(song)
    # Get song Length
    global song_length
    song_length = song_mut.info.length
    # Convert to Time Format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    # Increment current_time by 1 sec
    current_time += 1
    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {converted_song_length}  of  {converted_song_length}  ')
    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time):
        # Update Slider To position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # Update Slider To position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        # convert to time format
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))
        # Output time to status bar
        status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')
        # Move this thing along by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)


    # Output time to status bar
    # status_bar.config(text=converted_current_time+"/"+converted_song_length)
    # status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

    # update slider position value to current song position
    # my_slider.config(value=current_time)



    # update time
    status_bar.after(1000,play_time)

# Play Selected Songs
def play():
    # Set Stopped Variable To False So Song Can Play
    global stopped
    stopped=False
    song=songbox.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Call the play_time function to get song length
    play_time()
    # Update Slider To position
    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)

    # Get current volume
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=int(current_volume*100))

    # Get current volume
    current_volume = pygame.mixer.music.get_volume()
    # Times by 100 to make it easier to work with
    current_volume = current_volume * 100
    # slider_label.config(text=current_volume * 100)

    # Change Volume Meter Picture
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 25:
        volume_meter.config(image=vol1)
    elif int(current_volume) >= 25 and int(current_volume) <= 50:
        volume_meter.config(image=vol2)
    elif int(current_volume) >= 50 and int(current_volume) <= 75:
        volume_meter.config(image=vol3)
    elif int(current_volume) >= 75 and int(current_volume) <= 100:
        volume_meter.config(image=vol4)

global stopped
stopped = False
# Stop playing current song
def stop():
    # Reset Slider and Status Bar
    status_bar.config(text='No song playing')
    my_slider.config(value=0)
    # Stop Song From Playing
    pygame.mixer.music.stop()
    songbox.selection_clear(ACTIVE)
    # Clear the status bar
    status_bar.config(text='Song Stopped')
    # Set Stop Variable To True
    global stopped
    stopped = True

global paused
paused=False
# Pause and Unpause the current song
def pause(is_paused):
    global paused
    paused=is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True
        status_bar.config(text='Song Paused')

# Add many songs to playlist
def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='D:/Songs', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

	# Loop thru song list and replace directory info and mp3
	for song in songs:
	    # song = song.replace("C:/gui/audio/", "")
		# song = song.replace(".mp3", "")
		# Insert into playlist
		songbox.insert(END, song)

def about():
    tmsg.showinfo("About","This GUI Application is created by Kshitij Gupta")

# Next Song Forward Button
def forward():
    # Reset Slider and Status Bar
    status_bar.config(text='')
    my_slider.config(value=0)
    # Get the current song tuple number
    next_one=songbox.curselection()
    # Add one to the current song number
    next_one=next_one[0]+1
    # Grab song title from playlist
    song=songbox.get(next_one)
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar in playlist listbox
    songbox.selection_clear(0, END)

    # Activate new song bar
    songbox.activate(next_one)

    # Set Active Bar to Next Song
    songbox.selection_set(next_one, last=None)

def previous():
    # Reset Slider and Status Bar
    status_bar.config(text='')
    my_slider.config(value=0)
    # Get the current song tuple number
    next_one = songbox.curselection()
    # Add one to the current song number
    next_one = next_one[0] - 1
    # Grab song title from playlist
    song = songbox.get(next_one)
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar in playlist listbox
    songbox.selection_clear(0, END)

    # Activate new song bar
    songbox.activate(next_one)

    # Set Active Bar to Next Song
    songbox.selection_set(next_one, last=None)

# Delete A Song
def delete_song():
    stop()
    a= tmsg.askyesno("Delete","Are you sure?")
    if a==1:
        # Delete Currently Selected Song
        songbox.delete(ANCHOR)
        # Stop Music if it's playing
        pygame.mixer.music.stop()
        tmsg.showinfo("Successful","Song deleted successfully")
    else:
        pass

# Delete All Songs from Playlist
def delete_all_songs():
    stop()
    a = tmsg.askyesno("Delete", "Are you sure?")
    if a == 1:
        # Delete All Songs
        songbox.delete(0, END)
        # Stop Music if it's playing
        pygame.mixer.music.stop()
        tmsg.showinfo("Successful", "Song List deleted successfully")
    else:
        pass

def slide(x):
    # slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    song = songbox.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    # Get current volume
    current_volume=pygame.mixer.music.get_volume()
    # Times by 100 to make it easier to work with
    current_volume = current_volume * 100
    # slider_label.config(text=current_volume * 100)

    # Change Volume Meter Picture
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 25:
        volume_meter.config(image=vol1)
    elif int(current_volume) >= 25 and int(current_volume) <= 50:
        volume_meter.config(image=vol2)
    elif int(current_volume) >= 50 and int(current_volume) <= 75:
        volume_meter.config(image=vol3)
    elif int(current_volume) >= 75 and int(current_volume) <= 100:
        volume_meter.config(image=vol4)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create master frame
master_frame=Frame(root)
master_frame.pack(pady=20)
master_frame.config(bg="brown")
# Create Playlist Box
songbox=Listbox(master_frame,bg="black",fg="green",width=60,font="lucida 10 bold",selectbackground="green",selectforeground="black",yscrollcommand = scrollbar.set)
songbox.grid(row=0,column=0,padx=5)
scrollbar.config(command=songbox.yview)

# Create Player Control Button Images
back_btn_img=PhotoImage(file="img/back50.png")
forward_btn_img=PhotoImage(file="img/forward50.png")
play_btn_img=PhotoImage(file="img/play50.png")
pause_btn_img=PhotoImage(file="img/pause50.png")
stop_btn_img=PhotoImage(file="img/stop50.png")

# Define Volume Control Images
global vol0
global vol1
global vol2
global vol3
global vol4
vol0 = PhotoImage(file='img/volume0.png')
vol1 = PhotoImage(file='img/volume1.png')
vol2 = PhotoImage(file='img/volume2.png')
vol3 = PhotoImage(file='img/volume3.png')
vol4 = PhotoImage(file='img/volume4.png')

# Create Player Control Frames
control_frame=Frame(master_frame,bg="brown")
control_frame.grid(row=1,column=0,pady=20)

# Create Volume Meter
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1, padx=10)

# Create volume label frame
volume_frame=LabelFrame(master_frame,text="Volume")
volume_frame.grid(row=0,column=1,padx=30)

# Create Player Control Buttons
back_btn=Button(control_frame,image=back_btn_img,bg="brown",borderwidth=0,command=previous)
forward_btn=Button(control_frame,image=forward_btn_img,bg="brown",borderwidth=0,command=forward)
play_btn=Button(control_frame,image=play_btn_img,bg="brown",borderwidth=0,command=play)
pause_btn=Button(control_frame,image=pause_btn_img,bg="brown",borderwidth=0,command=lambda:pause(paused))
stop_btn=Button(control_frame,image=stop_btn_img,bg="brown",borderwidth=0,command=stop)

back_btn.grid(row=0,column=0,padx=10)
forward_btn.grid(row=0,column=1,padx=10)
play_btn.grid(row=0,column=2,padx=10)
pause_btn.grid(row=0,column=3,padx=10)
stop_btn.grid(row=0,column=4,padx=10)

# Create Menu
my_menu=Menu(root)
root.config(menu=my_menu,bg="brown")

# Add Add_Songs Menu
add_song_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Add One Song",command=add_song)
add_song_menu.add_command(label="Add Many Song",command=add_many_songs)

# Create Delete Song Menu
remove_song_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete Current Song", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs", command=delete_all_songs)

help_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About",command=about)

# Create Status Bar
status_bar = Label(root, text='No song playing', bd=1, relief=GROOVE, anchor=W ,bg="black",fg="white")
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Music Position Slider
my_slider = ttk.Scale(
master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2,column=0,pady=10)

# Create Volume Slider
volume_slider = ttk.Scale(
volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)

# Creaate Temporary slider label
# slider_label=Label(root,text="0",bg="grey")
# slider_label.pack()




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
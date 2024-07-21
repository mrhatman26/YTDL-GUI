import tkinter as t
import sys, subprocess
from tkinter.ttk import *
from tkinter import messagebox, filedialog as f
def button_exit(window):
    if messagebox.askquestion("Exit?", "Are you sure you want to exit?") == "yes":
        window.destroy()
        sys.exit()
    else:
        return

def button_file_select(widget_output_entry, output_entry):
    file = t.filedialog.askdirectory()
    output_entry.change_state('normal')
    print(file)
    widget_output_entry.delete(0, "end")
    if file is None and file != "":
        widget_output_entry.insert(0, "C:/")
    else:
        widget_output_entry.insert(0, str(file))
    output_entry.change_state('disabled')

def button_execute(widget_link_entry, widget_output_entry, playlist_var, audio_var, audio_format, window):
    if str(widget_link_entry.get()) == "":
        messagebox.showerror("Error", "No video or playlist link given.")
        return
    if str(widget_output_entry.get()) == "":
        messagebox.showerror("Error", "No output directory selected.")
        return
    if "playlist?" not in widget_link_entry.get() and "watch?" not in widget_link_entry.get():
        messagebox.showerror("Invalid Link", "Link is not a YouTube video or playlist.")
        return
    ytdl_command = 'yt-dlp -o "' + str(widget_output_entry.get()) + '/%(title)s.%(ext)s"'
    if "playlist" in widget_link_entry.get():
        playlist_var.set(1)
        if messagebox.askyesno("Playlist Detected", "Link is a playlist, not a video. Would you like to download the whole playlist?") is False:
            return
    if bool(playlist_var.get()) is True:
        if "playlist" not in widget_link_entry.get():
            if messagebox.askyesno("Playlist Not Detected", "Link is NOT a playlist. Would you like to download only this video?") is False:
                return
        else:
            ytdl_command = ytdl_command + " --yes-playlist"
    if bool(audio_var.get()) is True:
        if audio_format == "":
            messagebox.showinfo("Default Format", "No audio format was selected. Audio will be mp3")
            audio_format = "MP3"
        ytdl_command = ytdl_command + " --extract-audio --audio-format " + audio_format.lower()
        #Todo: Allow users to change the audio format
    ytdl_command = ytdl_command + " " + str(widget_link_entry.get())
    window.destroy()
    print(ytdl_command)
    subprocess.run(ytdl_command)
    temp_root = t.Tk()
    temp_root.withdraw()
    if messagebox.askyesno("Again?", "Download complete, would you like to reopen YTDL GUI?") is True:
        #subprocess.run("python main.py") #<- For when running as a Python Scripts
        subprocess.run("yt-dl-gui.exe") #<- For when running as an executeable.
    else:
        messagebox.showinfo("Complete", "Thank you for using YTDL GUI")
    temp_root.destroy()
    sys.exit()

def button_about():
    message = "This was a program made by MrHatman26, AKA nobody important."
    message = message + "\n\nWhat is this?: This is a tool to automate the usage of the yt-dl app by entering the command and parameters for you so you don't need to remember it all."
    message = message + "\nBecause of this, this tool requires that yt-dl be installed on your system."
    message = message + "\n\nThis program was made using Python and uses the following libraries:\n-tkinter: For the GUI\n-sys: For exiting the program\n-subprocess: To run YT-DL"
    message = message + "\n\nCurrent Version: ?.?.? (I wasn't keeping track...)"
    #This is a stupid way to do messages, but whatever
    messagebox.showinfo("About", message)

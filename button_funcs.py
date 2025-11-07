import tkinter as t
import sys, subprocess
from tkinter.ttk import *
from tkinter import messagebox, filedialog as f
from misc import *

def button_exit(window):
    if ask_question("Exit?", "Are you sure you want to exit?") is True:
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
        show_error("Error", "No video or playlist link given.")
        return
    if str(widget_output_entry.get()) == "":
        show_error("Error", "No output directory selected.")
        return
    if "playlist?" not in widget_link_entry.get() and "watch?" not in widget_link_entry.get():
        show_error("Invalid Link", "Link is not a YouTube video or playlist.")
        return
    ytdl_command = 'yt-dlp -o "' + str(widget_output_entry.get()) + '/%(title)s.%(ext)s"'
    if "playlist" in widget_link_entry.get():
        if bool(playlist_var) is False:
            playlist_var.set(1)
            if ask_question("Playlist Detected", "Link is a playlist, not a video. Would you like to download the whole playlist?") is False:
                return
    if bool(playlist_var.get()) is True:
        if "playlist" not in widget_link_entry.get():
            if ask_question("Playlist Not Detected", "Link is NOT a playlist. Would you like to download only this video?") is False:
                return
        else:
            ytdl_command = ytdl_command + " --yes-playlist"
    if bool(audio_var.get()) is True:
        if audio_format == "":
            show_message("Default Format", "No audio format was selected. Audio will be mp3")
            audio_format = "MP3"
        #ytdl_command = ytdl_command + " --extract-audio --audio-format " + audio_format.lower()
        ytdl_command = ytdl_command + " --extract-audio --audio-format " + audio_format.lower() + " --cookies cookies_test.txt"
    ytdl_command = ytdl_command + " " + str(widget_link_entry.get())
    window.destroy()
    print(ytdl_command)
    try:
        subprocess.run(ytdl_command)
    except Exception as e:
        print("yt-dlp not found, trying youtube-dl.exe instead\nActual exception was: " + str(e))
        try:
            ytdl_command = ytdl_command.replace("yt-dlp", "youtube-dl.exe")
            subprocess.run(ytdl_command)
        except Exception as e:
            show_error("No Downloader", "Neither yt-dlp nor youtube-dl.exe were found. Are either on the System or User PATH?\nActual exception was: " + str(e))
    temp_root = t.Tk()
    temp_root.withdraw()
    if ask_question("Again?", "Download complete, would you like to reopen YTDL GUI?") is True:
        #subprocess.run("python main.py") #<- For when running as a Python Scripts
        subprocess.run("yt-dl-gui.exe") #<- For when running as an executeable.
    else:
        show_message("Complete", "Thank you for using YTDL GUI")
    temp_root.destroy()
    sys.exit()

def button_about():
    print(load_file(True))
    message = "This was a program made by MrHatman26, AKA nobody important."
    message = message + "\n\nWhat is this?: This is a tool to automate the usage of the yt-dl app by entering the command and parameters for you so you don't need to remember it all."
    message = message + "\nBecause of this, this tool requires that yt-dl be installed on your system."
    message = message + "\n\nThis program was made using Python and uses the following libraries:\n-tkinter: For the GUI\n-sys: For exiting the program\n-subprocess: To run YT-DL"
    message = message + "\n\nCurrent Version: 1.2.0"
    #This is a stupid way to do messages, but whatever
    show_message("About", message)

def button_update_downloader():
    if ask_question("Update?", "Would you like to update YouTube Downloader?") is True:
        try:
            print("Updating yt-dlp...")
            subprocess.run("yt-dlp -U")
        except Exception as e:
            print("yt-dlp not found, trying youtube-dl.exe instead\nActual exception was: " + str(e))
            try:
                print("Updating youtube-dl.exe...")
                subprocess.run("youtube-dl.exe -U")
            except Exception as e:
                show_error("No Downloader", "Neither yt-dlp nor youtube-dl.exe were found. Are either on the System or User PATH?\nActual exception was: " + str(e))
                return
            show_message("Updated", "youtube-dl.exe was updated")
            return
        show_message("Updated", "yt-dlp was updated")
    else:
        return

def button_load_cookies():
    pass

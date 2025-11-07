import tkinter as t
from tkinter.ttk import *
from widgets import *
from button_funcs import button_exit, button_file_select, button_execute, button_about, button_update_downloader
from misc import show_warning, load_file
class MainWindow(t.Tk):
    def __init__(self, resolution, title):
        t.Tk.__init__(self)
        self.geometry(resolution)
        self.title(title)
        self.resizable(False, False)

class MainApplicationLayout(t.Frame):
    def __init__(self, parent):
        t.Frame.__init__(self)
        self.parent = parent
        #Input Frame
        self.input_frame = Frame(parent, True)
        ##Link
        self.link_label = Label(self.input_frame, "Video/Playlist Link:")
        self.link_entry = Entry(self.input_frame, "center", 40)
        ##Output
        self.output_label = Label(self.input_frame, "Output Destination:")
        self.output_entry = Entry(self.input_frame, "center", 40)
        self.output_entry.change_state('disabled')
        self.output_browse_button = Button(self.input_frame, "Browse", lambda: button_file_select(self.output_entry, self.output_entry), 11)
        #Checkbox Frame
        self.checkbox_frame = Frame(parent, True)
        ##Playlist
        self.playlist_frame = Frame(self.checkbox_frame, False)
        self.playlist_label = Label(self.playlist_frame, "Is Playlist?:")
        self.playlist_value = t.IntVar()
        self.playlist_checkbox = Checkbutton(self.playlist_frame, self.playlist_value)
        ##Audio
        self.audio_format = ""
        self.audio_frame = Frame(self.checkbox_frame, False)
        self.audio_label = Label(self.audio_frame, "Audio Only?")
        self.audio_value = t.IntVar()
        self.audio_select_button = Button(self.checkbox_frame, "Audio Format", lambda: self.change_a_form(True), 11)
        self.audio_checkbox = Checkbutton(self.audio_frame, self.audio_value, lambda: self.match_button_state(self.audio_select_button, self.audio_value, edit_value=self.audio_format))
        self.match_button_state(self.audio_select_button, self.audio_value, edit_value=self.audio_format)
        ##Cookies
        self.cookie_file = ""
        self.cookie_frame = Frame(parent, True)
        self.cookie_top_frame = Frame(self.cookie_frame, False)
        self.cookie_use_label = Label(self.cookie_top_frame, "Use Cookies?:")
        self.cookie_use_value = t.IntVar()
        self.cookie_use_checkbox = Checkbutton(self.cookie_top_frame, self.cookie_use_value, lambda: self.match_button_state(self.cookie_load_button, self.cookie_use_value, edit_value=self.cookie_file))
        self.cookie_bottom_frame = Frame(self.cookie_frame, False)
        self.cookie_load_button = Button(self.cookie_bottom_frame, "Load Cookies", self.change_cookies, 11)
        self.cookie_file_label = Label(self.cookie_bottom_frame, "No Cookies")
        self.match_button_state(self.cookie_load_button, self.cookie_use_value, edit_value=self.cookie_file)
        #Buttons Frame
        self.button_frame = Frame(parent, False)
        self.download_button = Button(self.button_frame, "Download", lambda: button_execute(self.link_entry, self.output_entry, self.playlist_value, self.audio_value, self.audio_format, parent), 21)
        self.update_downloader_button = Button(self.button_frame, "Update", button_update_downloader, 21)
        self.about_button = Button(self.button_frame, "About", button_about, 21)
        self.exit_button = Button(self.button_frame, "Exit", lambda: button_exit(parent), 21)
        self.parent.protocol("WM_DELETE_WINDOW", lambda: button_exit(parent))
        self.pack_all()        

    def pack_all(self):
        #Input Frame
        ##Link
        self.link_label.grid(row=0, column=0, padx=20, pady=5)
        self.link_entry.grid(row=0, column=1)
        ##Output
        self.output_label.grid(row=1, column=0)
        self.output_entry.grid(row=1, column=1)
        self.output_browse_button.grid(row=1, column=2, padx=10)
        self.input_frame.pack(pady=5)
        #Checkbox Frame
        ##Playlist
        self.playlist_label.pack(side=t.LEFT)
        self.playlist_checkbox.pack(side=t.RIGHT)
        self.playlist_frame.pack(pady=10)
        ##Audio
        self.audio_label.pack(side=t.LEFT)
        self.audio_checkbox.pack(side=t.RIGHT)
        self.audio_frame.pack(side=t.LEFT)
        self.audio_select_button.pack(side=t.RIGHT)
        self.checkbox_frame.pack(pady=5)
        #Cookie Frame
        self.cookie_use_label.pack(side=t.LEFT)
        self.cookie_use_checkbox.pack(side=t.RIGHT)
        self.cookie_top_frame.pack(pady=3)
        self.cookie_load_button.pack(side=t.TOP)
        self.cookie_file_label.pack(side=t.BOTTOM)
        self.cookie_bottom_frame.pack()
        self.cookie_frame.pack()
        #Buttons Frame
        self.download_button.pack(pady=5)
        self.update_downloader_button.pack(pady=5)
        self.about_button.pack()
        self.exit_button.pack(pady=5)
        self.button_frame.pack()

    def change_state(self, new_state):
        self.link_entry.configure(state=new_state)
        self.output_entry.configure(state=new_state)
        self.output_browse_button.configure(state=new_state)
        self.playlist_checkbox.configure(state=new_state)
        self.audio_checkbox.configure(state=new_state)
        self.audio_select_button.configure(state=new_state)
        self.cookie_use_checkbox.configure(state=new_state)
        self.cookie_load_button.configure(state=new_state)
        self.download_button.configure(state=new_state)
        self.update_downloader_button.configure(state=new_state)
        self.about_button.configure(state=new_state)
        self.exit_button.configure(state=new_state)

    def change_a_form(self, start, new_form=""):
        if start is True:
            self.change_state("disabled")
            AudioFormatBox(self)
        else:
            self.change_state("normal")
            self.audio_format = new_form
            print(self.audio_format)

    def match_button_state(self, button, value, edit_value=None):
        if bool(value.get()) is True:
            button.configure(state="normal")
        else:
            if edit_value is not None:
                edit_value = ""
            button.configure(state="disabled")

    def change_cookies(self):
        cookie_file = load_file(include_filename=True)
        try:
            cookie_file[0].close()
            print("Good going bro")
        except:
            print("Oh no bro!")

class AudioFormatBox(t.Frame):
    def __init__(self, main_app):
        self.parent = t.Tk()
        self.parent.geometry("380x155")
        self.parent.title("Audio Format")
        self.parent.resizable(False, False)
        self.parent.protocol("WM_DELETE_WINDOW", self.prevent_exit)
        self.label = Label(self.parent, "Please select an audio format:", ("TkDefaultFont", 20))
        self.label.pack()
        self.mp3_button = Button(self.parent, "MP3", lambda: self.confirm_new_format(0, main_app), 21)
        self.wav_button = Button(self.parent, "WAV", lambda: self.confirm_new_format(1, main_app), 21)
        self.flac_button = Button(self.parent, "FLAC", lambda: self.confirm_new_format(2, main_app), 21)
        self.buttons = [self.mp3_button, self.wav_button, self.flac_button]
        for item in self.buttons:
            item.pack(pady=5)
        self.parent.mainloop()

    def confirm_new_format(self, button_no, main_app):
        new_format = self.buttons[button_no]['text']
        self.parent.destroy()
        main_app.change_a_form(False, new_format)

    def prevent_exit(self):
        show_warning("Warning!", "Please select an audio format!")


A simple Python GUI made to automate the useage of Youtube Download.

To use, it is recommended to launch the program in the command prompt so that it does not close upon any errors.
(If you have the code instead of the executeable, run "main.py" first)

Once you have entered the video or playlist link and the output destination folder (and selected the options), the program will
launch youtube-dl with the commands needed to download the video or playlist. When done, it will ask if you want to reload the program or not.
Note: If youtube-dl itself has any errors or fails to download a video, the GUI will assume the video or playlist has been downloaded.
I should probably fix that...

To Do:\
-Add option to load cookies to allow for downloading of age restricted videos.\
-Add option to use custom yt-dl.exe in case the file is not in the PATH or cannot be found for some other reason.\
-Make it so the program keeps the last directory selected when the user doesn't select one (As of now, it replaces the directory with a blank string).
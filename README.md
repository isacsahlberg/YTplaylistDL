# YouTube Playlist downloader/merger

...meh, don't publish this as a public repo, it's not that useable and all that

## Usage:
Modify the first beginning of ```main_downloader.py```, and set the url to the 
desired YouTube Playlist. By default, a directory called ```audio_files/```
will be created, and the audio files will go there.
Running
```bash
$ python main_downloader.py
```
will then download the audio files from the individual videos, and additionally
call the ```merge()``` function from the ```merger.py``` file, which combines the
files into one long audio file.
Note: the audio files will automatically be ordered alphabetically, unless you
give a smart key by which to sort them.

(You could add a way to get the name of the video, then add a number by using
enumerate() blah blah, but anyway, I don't know who you are, or if you are perhaps
me, but you're probably smart, you can figure it out.)
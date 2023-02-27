# YouTube Playlist downloader/merger


### Usage:
Running
```bash
$ python main_downloader.py -l "<link here>"
```
will download the audio files from the individual videos, and additionally
call the ```merge()``` function from the ```merger.py``` file, which combines the
files into one long audio file.
By default, a directory called ```audio_files/``` will be created, and the audio files will go there. 
This code does not delete those files, so like, just you do that.
If you don't provide a link, then the default link will be used, and I'm sorry, you will get some Bach on your hard drive, which, well that sounds like a win either way, so...


### General warning
```pytube``` seems to be a bit buggy, so you may run into Errors or Exceptions,
but sometimes just running the program again a few times actually let's you get away without problems ```¯\_(ツ)_/¯```


## The point is
If you just want to download the video or audio of a Youtube video, this is how:
```bash
$ from pytube import YouTube
$ yt = YouTube('https://www.youtube.com/watch?v=gVah1cr3pU0')
```

and then
```bash
$ video = yt.streams.get_highest_resolution()  # or e.g. "lowest" resolution
$ video.download()                             # or the more specific .download(filename=...)
```

for just the audio, this would be
```bash
$ audio = yt.streams.get_audio_only()
$ audio.download()
```

but for a long playlist, we can do everything in one swoop. 
The ```main_downloader.py``` simply uses a YouTube Playlist object to download the audio from all of the videos, one by one.
The second part is then about merging those audio files into one long track; that's all handled by the function defined in ```merger.py```.
By default, the audio files will be ordered in the same order as the original playlist. You can use a custom ordering key if you'd like, but that part is on you.


### Requirements (aside from ```python3```):
```bash
pytube
pydub
```
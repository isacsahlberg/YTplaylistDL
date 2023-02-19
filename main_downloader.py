import merger

import time
t1 = time.monotonic()

import argparse
import os
from pytube import Playlist

if not os.path.exists('audio_files/'):
    os.mkdir('audio_files/')

    # #%% maybe add later for command-line arguments and stuff
    # parser = argparse.ArgumentParser
    # parser.add_argument("--link", "-l", help="give link to the Youtube playlist")
    # return parser.parse_known_args()[0]

# # Note that if you just want to download the audio of 1 Youtube video, this is how:
# from pytube import YouTube
# v = YouTube('https://www.youtube.com/watch?v=nPHIZw7HZq4')
# a = v.streams.get_audio_only()
# a.download()  # or the more specific  a.download('audio_files/')

# Link -- "Bach The Well-Tempered Clavier András Schiff" ...
# For this particular link, we want the audio files ordered with this key
link = 'https://www.youtube.com/playlist?list=PLJ-xfJ6MiKtxytddZgWWTnyvVGNLiDifU'
key = lambda file_str: int(file_str.split()[-1].split('.')[0])

# For this particular link, we want the audio files ordered with this key
# link = 'https://www.youtube.com/playlist?list=PLVA3F_69rVEx40NiR-LoAb2D0vNzgfreB'
# key = lambda file_str: file_str.split()[4]

playlist = Playlist(link)
title = playlist.title

# videos = playlist.videos  # (quasi)list of YouTube objects
videos = [v for v in playlist.videos]  # list of YouTube objects (for better slicing)
# videos = videos[:3]
title = 'J.S. Bach - The Well-Tempered Clavier Book I - András Schiff (1986)'


#%%

# Focus only on the audio
# audios = [video.streams.get_audio_only() for video in Playlist(link).videos]
audios = []
subtypes = []
counter = 0
for video in videos:
    # audio = video.streams.get_audio_only()
    try:
        audio = video.streams.get_audio_only()
    except:
        print("Something didn't quite work \n(Sometimes this just happens?", \
              "especially IncompleteRead or whatever it's called)")
        print('Exiting........')
        exit(0)
    
    audios.append(audio)
    subtypes.append(audio.subtype)
    counter += 1
    print(f"Yay, {counter} done!")

# Check the format
if len(set(subtypes)) == 1:
    subtype = subtypes[0]
    print(f"---> Great, all audios are in the same format: '{subtype}'")
else:
    print("\nThere are several subtypes! See for yourself")
    print(set(subtypes))
    print("What do we do now...?")
    exit_()

# Download
for audio in audios:
    audio.download('audio_files/')  # only works if the filename is _not_ taken (which should be quite fine)

#%%

# Merging
merger.merge('audio_files/', subtype, title, key)


t2 = time.monotonic()
print(f"That took {(t2-t1)/60:.2f} min")

import argparse
import os
from pytube import Playlist
import time

import merger

t1 = time.monotonic()

if not os.path.exists("audio_files/"):
    os.mkdir("audio_files/")

parser = argparse.ArgumentParser()
parser.add_argument("--link", "-l", help="give link to the Youtube playlist")
p = parser.parse_known_args()[0]

# Link
# The default order is the same as in the original playlist
link = "https://www.youtube.com/playlist?list=OLAK5uy_lkiSEO2O57_2YQroYKBmBaUCbAJuWxqqQ"

# for custom ordering, we can use a key, e.g.
# link = "https://www.youtube.com/playlist?list=PLJ-xfJ6MiKtxytddZgWWTnyvVGNLiDifU"
# key = lambda filename: int(filename.split()[-1].split(".")[0])
#
# link = 'https://www.youtube.com/playlist?list=PLVA3F_69rVEx40NiR-LoAb2D0vNzgfreB'
# key = lambda filename: int(filename.split()[4])

if p.link:
    link = p.link
else:
    print(f"\nYou provided no '--link' --> continuing with \n{link}\n")

playlist = Playlist(link)
title = playlist.title

# Now, playlist.videos is an iterable of YouTube objects, we want a proper list
videos = [v for v in playlist.videos]
# videos = videos[:3]  # for testing

# Give the titles an extra beginning so that they are then alphabetically
# ordered but preserve the original order
titles = [
    (f"{i+1:02}-" + v.title).replace(":", " -") for i, v in enumerate(videos)
]


#%%
# Extract only on the audio
audios = []
subtypes = []
counter = 0
for video in videos:
    try:
        audio = video.streams.get_audio_only()
    except:
        print(
            "Something didn't quite work \n(Sometimes this just happens?",
            "especially IncompleteRead or whatever it's called)",
        )
        print("Exiting........")
        exit_()  # yeah yeah I know, this is just to abort

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


#%%
# Download
print(f"Attempting to download {len(audios)} files...")
for audio, title_ in zip(audios, titles):
    audio.download(filename="audio_files/" + title_ + "." + audio.subtype)


#%%
# Merging -- the default order is alphabetical
# for a custom order, use a key (see above)
merger.merge("audio_files/", subtype, title, key=None)

t2 = time.monotonic()
print(f"That took {(t2-t1)/60:.2f} min")

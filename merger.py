import os
from pathlib import Path
from pydub import AudioSegment


def merge(
    folname: str,
    format_: str,
    destination_filename: str = "combined",
    key=None,
):
    # First we get all the relevant file names (those with the same format)
    filenames = [
        filename
        for filename in os.listdir(folname)
        if filename.split(".")[-1] == format_
    ]
    # Then sort them according to the given key
    filenames = sorted(filenames, key=key)  # also works with None

    sounds = []
    counter = 0
    print("---> Extracting...")
    for filename in filenames:
        filepath = Path(folname, filename)
        sounds.append(AudioSegment.from_file(filepath))
        counter += 1
        print(f"{filename[:24]} extracted -- {counter} audio files in total")
    print("---> Done!\n")

    # Awesome! These AudioSegment objects have a nicely defined __add__ method (appends sounds)
    # and we can simply sum them, s1 + s2 -- or we can simply take a sum over the list!
    print("---> Merging...")
    merged = sum(sounds)  # another AudioSegment object
    print("---> Done!\n")

    # Export
    filename = destination_filename + "." + format_
    print(
        "---> Exporting... (this may take several seconds (maybe 1s per 1min of audio material?)"
    )
    _ = merged.export(Path(folname, filename), format=format_)
    print("---> Done!\n")

    # Summary
    print("Summary:")
    N_audio = len(sounds)
    durations = [s.duration_seconds for s in sounds]
    dur_min = min(durations)
    dur_max = max(durations)
    print(
        f"There were {N_audio} audio files ranging in length from {dur_min:.1f} s to {dur_max:.1f} s"
    )
    print(f"The sum of the durations would be {sum(durations):.1f} s")
    print(
        f"The new comined audio files has a length of {merged.duration_seconds:.1f} s\n"
    )

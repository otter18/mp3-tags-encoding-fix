import os
import sys

from mutagen.easyid3 import EasyID3


def decode_(s):
    try:
        return s.encode("latin-1").decode('cp1251').encode('utf8').decode('utf8')
    except Exception:
        return s


folder = sys.argv[1]
os.chdir(folder)

for filename in sorted(os.listdir()):
    if filename[-3:] != 'mp3':
        continue

    print('-' * 20, filename, '-' * 20)
    audio = EasyID3(filename)
    print('Was:', audio)

    for key, vals in audio.items():
        audio[key] = [decode_(elem) for elem in vals]

    print('Now:', audio)
    audio.save(f"{filename}-fixed.mp3")

    print('-' * 50)

#!/usr/bin/env python3

import json
import sys
import simpleaudio as sa
from pathlib import Path

base_dir = Path(__file__).resolve().parent

json_path = base_dir / "data.json"
wav_path = base_dir / "media/yay-sfx.wav"

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# bold red, green, reset
BR = "\033[1;31m"
G = "\033[32m"
RE = "\033[0m"


def main():
	with open(json_path, "r", encoding="utf-8") as f:
		data = json.load(f)

	if data["first_time"]:
		setup()

	else:
		if data["style"] == "b":
			basic()
		elif data["style"] == "n":
			nice()
		else:
			setup()

def setup():
	style = input("\nChoose your style: Basic (b) or Nice (n)\n> ")

	new_data = {"first_time": False, "style": style}

	with open(json_path, "w", encoding="utf-8") as f:
		json.dump(new_data, f, indent=4)

	if style == "b":
        basic()
    else:
        nice()

def basic():
    pos = 0

    while True:
        pos += 1
        letter = input("\nNext letter in the alphabet: ").strip().lower()

        if letter != alphabet[pos]:
            exit()

        if pos == 25:
            print("\nYou completed the English alphabet.")
            exit() 

def nice():
    pos = 0

    while True:

        yay_sound = sa.WaveObject.from_wave_file(str(wav_path))

        pos += 1
        previous_letter = alphabet[pos - 1]

        print(f"\nPrevious letter: {previous_letter}")
        letter = input("Next letter in the alphabet: ").strip().lower()
        
        for _ in range(2):
            sys.stdout.write("\033[1A\r\033[2K")

        sys.stdout.write("\033[1A")
        sys.stdout.flush()

        if letter != alphabet[pos]:
        	print(f"\n{BR}You have failed me.{RE}\n")
        	exit()

        if pos == 25:
            print(f"\n{G}You completed the English alphabet.{RE}\n")

            play_obj = yay_sound.play()
            play_obj.wait_done()

            exit()

if __name__ == '__main__':
	main()
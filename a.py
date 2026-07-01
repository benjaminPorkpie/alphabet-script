#!/usr/bin/env python3

import string
import json
import sys
import simpleaudio as sa
from pathlib import Path
import argparse

base_dir = Path(__file__).resolve().parent

json_path = base_dir / "data.json"
wav_path = base_dir / "media/yay-sfx.wav"

parser = argparse.ArgumentParser(description="Alphabet script (to waste your time lol)")

parser.add_argument(
    "--settings",
    help="Change the theme between basic and nice"  
)

args = parser.parse_args()

if args.settings == "basic":
    print(f"Changing theme to basic")

    new_data = {"first_time": False, "style": "b"}

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, indent=4)

    print(f"\n{new_data}\n")
    exit()

elif args.settings == "nice":
    print(f"Changing theme to nice")

    new_data = {"first_time": False, "style": "n"}

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, indent=4)

    print(f"\n{new_data}\n")
    exit()

alphabet = list(string.ascii_lowercase)

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

def clear_lines(line_amount):
    for _ in range(line_amount):
        sys.stdout.write("\033[1A\r\033[2K")

    sys.stdout.write("\033[1A")
    sys.stdout.flush()

def setup():
    style = input("\nChoose your style: Basic (b) or Nice (n)\n> ")

    new_data = {"first_time": False, "style": style}

    with open(json_path, "w", encoding="utf-8") as f:
	    json.dump(new_data, f, indent=4)

    if style == "b":
        clear_lines(2)
        basic()
    elif style == "n":
        clear_lines(2)
        nice()
    else:
        print(f"{BR}Error:{RE} Please restart the script.")

def basic():
    pos = 0

    while True:
        pos += 1
        letter = input("\nNext letter in the alphabet: ").strip().lower()

        if letter == "help":
            clear_lines(1)
            print("\nType the next letter of the alphabet each time,\nuntil 'z'.\n\nCommands:\nhelp - print this message\nsettings - change the settings")
            pos -= 1
            continue

        if letter != alphabet[pos]:
            exit()

        if pos == 25:
            print("\nYou completed the English alphabet.")
            exit() 

def nice():
    pos = 0

    yay_sound = sa.WaveObject.from_wave_file(str(wav_path))

    while True:
        pos += 1
        previous_letter = alphabet[pos - 1]

        print(f"\nPrevious letter: {previous_letter}")
        letter = input("Next letter in the alphabet: ").strip().lower()
        
        clear_lines(2)

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
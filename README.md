![License](https://img.shields.io/badge/license-MIT-green)

# alphabet-script

## About

**alphabet-script** is designed to make you complete the English alphabet, once you've started it.
There's 2 styles to choose from, *Basic*, and *Nice*. *Basic* is the minimal way to do it, while *Nice* looks a bit nicer.

If you follow the **Setup** guide, you can make this into a command, so when you type "a" in your terminal, it will tell you to finish the alphabet.

You can add a --settings argument, either **basic**, or **nice**.
You can do -h or --help to view this later.

## Compatability

This script works on Linux, macOS and Windows, but the setup was designed for Linux, so the setup may not work on other operating systems.

## Requirements

- Python 3
- simpleaudio Python library

## Setup

> Note: this setup guide was designed to work on Linux.
>       It may not work on other operating systems

### 1. Clone this repo

First you must clone the repo:

`git clone https://github.com/benjaminPorkpie/alphabet-script.git`

### 2. Move the folder

It's recommended that you move the folder, (if not in `home`), and rename it:

`mv alphabet-script ~/.a`

### 3. Rename the script

It's also recommended to rename the script:

`mv ~/.a/a.py ~/.a/a`

This way it'll feel more like a command, and it can be typed more naturally.

### 4. Make the script executable

To run a script, it has to be executable:

`chmod +x ~/.a/a`

### 5. Create the ~/.local/bin directory

This is commonly already on most systems, but on some, it may be missing.
To create it:

`mkdir -p ~/.local/bin`

### 6. Add ~/.local/bin to PATH

This is also commonly in most systems, but to be sure, or if you just had to create it, run this command:

`export PATH="$HOME/.local/bin:$PATH"`

### 7. Create a symlink to ~/.a/a

We create a link from ~/.local/bin/a to point to ~/.a/a:

`ln -s ~/.a/a ~/.local/bin/a`

### 8. Install simpleaudio

This script uses the simpleaudio library, so we install it:

`python3 -m pip install simpleaudio`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

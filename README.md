### Aptall

A simple tool to use apt easier. Inspired from pacman and [yay](https://github.com/Jguer/yay)

## Installation

Aptall requires:

- Python3
- Aptitude
- Make (Only for installation)

After installing these dependencies, aptall can be installed by make.

```console
$ sudo make install
```

## Usage

Here some examples

Help
```console
$ aptall --help
usage: aptall [-h] [-i] [-r] [-a] [-u] [<Package Name>]

positional arguments:
  <Package Name>    Name of the package

optional arguments:
  -h, --help        show this help message and exit
  -i, --install     Install the given package, same as 'aptall <package name>'
  -r, --remove      Remove the given package
  -a, --autoremove  Remove unused packages
  -u, --upgrade     Upgrade packages, same as using without argument
  -f, --file        Read package names from given file, separated by lines and download them
```

Upgrade packages
```console
$ aptall
```

Install
```console
$ aptall telegram
6)node-telegram-bot-api
    node.js module for Telegram Bot API
5)python3-python-telegram-bot
    python module for Telegram Bot API (Python 3)
4)python3-python-telegram-bot-doc
    python module for Telegram Bot API (common documentation)
3)telegram-cli
    Command-line interface for Telegram messenger
2)telegram-desktop [Installed]
    fast and secure messaging application
1)telegram-purple
    Purple plugin to support Telegram

Please select what you want to install. Ex: 1 | 1 2 3 | 1-4
 >>
```

Remove
```console
$ aptall -r chromium
1)chromium-browser
    Transitional package - chromium-browser -> chromium snap
2)chromium-codecs-ffmpeg-extra
    Transitional package - chromium-codecs-ffmpeg-extra -> chromium-ffmpeg snap

Please select what you want to remove. Ex: 1 | 1 2 3 | 1-4
 >>
```

## TODO
- [x] Chance order of remove
- [x] Ability to select more than one package

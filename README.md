### Aptall

A simple tool to use apt easier

## Installation

Aptall requires:

- Python 3
- Aptitude
- Make (Only for installation)

After installing these dependencies, aptall can be installed by make.

```command
$ sudo make install
```

## Usage

Here some examples

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

Please select what you want to install
 >>
```

Remove
```console
$ aptall -r chromium
1)chromium-browser
    Transitional package - chromium-browser -> chromium snap
2)chromium-codecs-ffmpeg-extra
    Transitional package - chromium-codecs-ffmpeg-extra -> chromium-ffmpeg snap

Please select what you want to remove
 >>
```

## TODO
- [x] Chance order of remove
- [ ] Ability to select more than one package
- [ ] apt-cache instead of aptitude, for less dependency
- [ ] Better code

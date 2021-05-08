from typing import Union



COLORMAP = {
    'black': '\u001b[30m',
    'red': '\u001b[31m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m',
    'bblack': '\u001b[30;1m',
    'bred': '\u001b[31;1m',
    'bgreen': '\u001b[32;1m',
    'byellow': '\u001b[33;1m',
    'bblue': '\u001b[34;1m',
    'bmagenta': '\u001b[35;1m',
    'bcyan': '\u001b[36;1m',
    'bwhite': '\u001b[37;1m',
    'bgblack': '\u001b[40m',
    'bgred': '\u001b[41m',
    'bggreen': '\u001b[42m',
    'bgyellow': '\u001b[43m',
    'bgblue': '\u001b[44m',
    'bgmagenta': '\u001b[45m',
    'bgcyan': '\u001b[46m',
    'bgwhite': '\u001b[47m',
    'bgbblack': '\u001b[40;1m',
    'bgbred': '\u001b[41;1m',
    'bgbgreen': '\u001b[42;1m',
    'bgbyellow': '\u001b[43;1m',
    'bgbblue': '\u001b[44;1m',
    'bgbmagenta': '\u001b[45;1m',
    'bgbcyan': '\u001b[46;1m',
    'bgbwhite': '\u001b[47;1m',
    'reversed': '\u001b[7m'
    }

def reset():#resets the color of the code
    print('\u001b[0m', end='')

def color(in_color: Union[str, int]) -> None:
    """
    Either type in the name of the color or it's number in the map
    """
    if isinstance(in_color, int):
        col = COLORMAP.values().index(in_color % len(COLORMAP))
    else:
        col = COLORMAP[in_color.lower()]
    print(col, end='')

def cprint(text, in_color: Union[str, int], **kwargs):
    color(in_color)
    print(text, **kwargs)
    reset()

def clear():
    print('\u001b[2J')

def up(n=1000):
    print(f'\u001b[{n}A')

def down(n=1000):
    print(f'\u001b[{n}B')

def left(n=1000):
    print(f'\u001b[{n}D')

def right(n=1000):
    print(f'\u001b[{n}C')

def moveTo(row=0, col=0):
    print(f'\u001b[{row};{col}H', end='')
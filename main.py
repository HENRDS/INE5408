import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from views import SGI


def wowo():
    import re
    with open("data/test1.obj") as f:
        for m in re.finditer(".", ):
            print(m)


def main():
    v = SGI()
    v.show()
    try:
        Gtk.main()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    # main()
    wowo()

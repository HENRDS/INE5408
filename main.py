import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from views import SGI


def main():
    v = SGI()
    v.show()
    try:
        Gtk.main()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

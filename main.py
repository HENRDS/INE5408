import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from views import SGI


def main():
    builder = Gtk.Builder.new_from_file("main_window.glade")
    v = SGI(builder)
    v.show()
    try:
        Gtk.main()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

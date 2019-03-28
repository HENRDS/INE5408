import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk, GObject
from sgi import SGI


def main():
    builder = Gtk.Builder.new_from_file("main_window.glade")
    v = SGI(builder)
    v.show()
    v.connect_model()
    try:
        Gtk.main()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

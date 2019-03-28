import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk, GObject
from infra.ui import UI


def main():
    builder = Gtk.Builder.new_from_file("main_window.glade")
    v = UI(builder)
    v.show()
    Gtk.main()


if __name__ == '__main__':
    main()

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from views import SGI
from gi._gtktemplate import Template


@Template.from_file("main_window.glade")
class MainWindow(Gtk.Window):
    __gtype_name__ = "win_main"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class App(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.gnome.SGI',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)

        win.present()


def main_templ():
    app = App()
    return app.run(sys.argv)

def main():
    builder = Gtk.Builder.new_from_file("main_window.glade")
    v = SGI(builder)
    v.show()
    try:
        Gtk.main()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main_templ()

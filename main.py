import sys
import gi
from core.objfile import Lexer, Parser

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from views import SGI


def wowo():
    with open("data/test1.obj") as f:
        parser = Parser(Lexer(f))
        objects = parser.parse()
        print(objects)


def main():
    v = SGI()
    v.show()
    try:
        Gtk.main()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
    # wowo()

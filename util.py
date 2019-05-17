from cairo import Context
from contextlib import contextmanager
import gi
import itertools as itt

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk


@contextmanager
def this_source(ctx: Context, src):
    old = ctx.get_source()
    ctx.set_source(src)
    try:
        yield
    finally:
        ctx.set_source(old)


@contextmanager
def this_source_rgb(ctx: Context, r: float, g: float, b: float):
    old = ctx.get_source()
    ctx.set_source_rgb(r, g, b)
    try:
        yield
    finally:
        ctx.set_source(old)


def pop_msg(widget: Gtk.Widget, msg: str):
    pop = Gtk.Popover.new(widget)
    pop.lbl_txt = Gtk.Label(msg)
    pop.add(pop.lbl_txt)
    pop.set_position(Gtk.PositionType.RIGHT)
    return pop

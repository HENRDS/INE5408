#!usr/bin/env python3
"""
This script generates code for ui event handlers and groups them in classes
author: Henry R. Da Silva
"""
from xml.etree import ElementTree
import os
import weakref
import typing as tp

try:
    from mako.template import Template
except ImportError:
    raise ImportError("Mako template engine is required to run this file")

_extra_args = {
    "draw": ["ctx: Context"],
    "key-press-event": ["event: Gdk.EventKey"],
    "row-activated": ["path: Gtk.TreePath", "column: Gtk.TreeViewColumn"]
}
from dataclasses import dataclass


@dataclass
class Control:
    name: str
    type_: str
    cls_name: str
    attr_name: str
    events: tp.List["Event"]

    def __init__(self, node: ElementTree.Element):
        self.name: str = node.get("id")
        self.type_: str = node.get("class")
        self.cls_name = self.name.title().replace("_", "")
        self.attr_name = f"_{self.name.upper()}"
        self.events = [Event(self, e) for e in node.findall("signal")]

    @property
    def py_type(self):
        return f".".join(self.type_.rpartition("Gtk")[1:])


@dataclass
class Event:
    ctrl: Control
    name: str
    handler: str
    args: tp.List[str]

    def __init__(self, ctrl, node: ElementTree.Element):
        self.ctrl = weakref.proxy(ctrl)
        self.name = node.get("name")
        self.handler = node.get("handler")
        args = _extra_args.get(self.name)
        self.args = [] if args is None else args


@dataclass
class Window(Control):
    controls: tp.List[Control]

    def __init__(self, node: ElementTree.Element):
        super().__init__(node)
        self.controls = []
        for c in node.findall(".//object[@id]"):
            ctrl = Control(c)
            self.controls.append(ctrl)

    @property
    def all_events(self):
        for e in self.events:
            yield e
        for c in self.controls:
            for e in c.events:
                yield e


def main(ui_file_path: str, template_path: str, des_path: str, ui_class="UI", main_window="win_main"):
    from pprint import pprint
    file = os.path.abspath(ui_file_path)
    tree = ElementTree.parse(file)
    root = tree.getroot()
    windows = [Window(x) for x in root.findall("./object[@id][@class='GtkWindow']")]
    windows.extend(Window(x) for x in root.findall("./object[@id][@class='GtkPopover']"))
    pprint(windows)
    templ = Template(filename=template_path)
    text = templ.render(cls_name=ui_class,
                        main_window=main_window,
                        windows=windows)
    with open(des_path, "w") as src:
        src.write(text)
    print(f"Saved to {des_path}")


if __name__ == "__main__":
    main("../main_window.glade", "ui.py.mako", "../views/ui.py")

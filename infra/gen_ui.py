#!usr/bin/env python3
"""
This script generates code for ui event handlers and groups them in classes
author: Henry R. Da Silva
"""
from xml.etree import ElementTree
import os
import weakref
import typing as tp
from dataclasses import dataclass

try:
    from mako.template import Template
except ImportError:
    raise ImportError("Mako template engine is required to run this file")

_extra_args = {
    "draw": ["ctx: Context"],
    "key-press-event": ["event: Gdk.EventKey"],
    "row-activated": ["path: Gtk.TreePath", "column: Gtk.TreeViewColumn"]
}
_all_controls = {}


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

        global _all_controls
        _all_controls[self.name] = self

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


class GUI:
    _WIN_TYPES = {"GtkDialog", "GtkPopover", "GtkWindow"}

    def __init__(self, cls_name: str, des_file: str, main_window: str = ...):
        self.cls_name = cls_name
        self.des_file = des_file
        self.__files = {}
        self.main_window = main_window

    def files(self):
        for path, file_dict in self.__files.items():
            yield os.path.relpath(path, os.path.abspath("..")), file_dict

    @property
    def windows(self):
        from itertools import chain
        for ctrl in chain(*self.__files.values()):
            if isinstance(ctrl, Window):
                yield ctrl

    def add_file(self, path: str):
        file = os.path.abspath(path)
        if file in self.__files:
            raise RuntimeWarning(f"'{file}' was added multiple times")
        tree = ElementTree.parse(file)
        root = tree.getroot()
        windows = []
        controls = []
        for x in root.findall("./object[@id]"):
            cls_name = x.get("class")
            if cls_name in self._WIN_TYPES:
                windows.append(Window(x))
            else:
                controls.append(Control(x))
        self.__files[file] = [*controls, *windows]

    def render(self, template_path: str):
        templ = Template(filename=template_path)
        text = templ.render(gui=self, Window=Window)
        with open(self.des_file, "w") as src:
            src.write(text)


def main(ui_file_path: str, template_path: str, des_file: str):
    ui = GUI("UI", des_file, "win_main")
    ui.add_file(ui_file_path)
    ui.render(template_path)
    print(ui.cls_name)
    for ctrl in ui.windows:
        print("\t", ctrl)

    print(f"Saved to {des_file}")


if __name__ == "__main__":
    main("../main_window.glade", "ui.py.mako", "../views/ui.py")

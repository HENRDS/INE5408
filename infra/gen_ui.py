#!usr/bin/env python3
from xml.etree import ElementTree
import os
import weakref
import typing as tp

try:
    from mako.template import Template
except ImportError:
    raise ImportError("Mako template engine is required to run this file")

_extra_args = {
    "draw": ["ctx: Context"]
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
            self.events.extend(ctrl.events)
            self.controls.append(ctrl)


def main():
    from pprint import pprint
    file = os.path.abspath("../main_window.glade")
    tree = ElementTree.parse(file)
    root = tree.getroot()
    windows = [Window(x) for x in root.findall("./object[@id][@class='GtkWindow']")]
    pprint(windows)
    templ = Template(filename="ui.py.mako")
    text = templ.render(cls_name="UI",
                        main_window="win_main",
                        windows=windows)
    with open("../views/ui.py", "w") as src:
        src.write(text)
    print("Saved to ./ui.py")


if __name__ == "__main__":
    main()

#!usr/bin/env python3
from xml.etree import ElementTree
import re
import os
import weakref

try:
    from mako.template import Template
except ImportError:
    raise ImportError("Mako template engine is required to run this file")


_extra_args = {
    "draw": ("ctx: Context",)
}

class Control:
    def __init__(self, node: ElementTree.Element):
        self.name: str = node.get("id")
        self.type_: str = node.get("class")
        self.cls_name = self.name.title().replace("_", "")
        self.attr_name = f"_{self.name.upper()}"
        self.events = [Event(self, e) for e in node.findall("signal")]

    @property
    def py_type(self):
        return f".".join(self.type_.rpartition("Gtk")[1:])

    def __repr__(self):
        return f"Control(name={self.name}, type={self.type_}, py_type={self.py_type})"


class Event:
    def __init__(self, ctrl, node: ElementTree.Element):
        self.ctrl = weakref.proxy(ctrl)
        self.name = node.get("name")
        args = _extra_args.get(self.name)
        if args is not None:
            self.args = args
        self.handler = node.get("handler")

    def __repr__(self):
        return f"Event(ctrl={self.ctrl.name}, name={self.name}, handler={self.handler})"


class Window(Control):
    def __init__(self, node: ElementTree.Element):
        super().__init__(node)
        self.controls = [Control(c) for c in node.findall(".//object[@id]")]




def main():
    file = os.path.abspath("../main_window.glade")
    tree = ElementTree.parse(file)
    root = tree.getroot()
    props = [(Window if x.get("class") == "GtkWindow" else Control)(x)
             for x in root.findall("./object[@id]")]
    print(len(props))
    templ = Template(filename="ui.py.mako")
    text = templ.render(cls_name="UI",
                        props=props,
                        windows=[w for w in props if isinstance(w, Window)])
    with open("./ui.py", "w") as src:
        src.write(text)
    print("Saved to ./ui.py")

if __name__ == "__main__":
    main()

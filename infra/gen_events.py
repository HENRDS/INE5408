#!usr/bin/env python3
from xml.etree import ElementTree
from string import Template
import os
from mako.template import Template
import weakref

class Control:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_
        self.ptr_t = type_ + "*"
        self.events = []

    @property
    def py_type(self):
        return f".".join(self.type_.rpartition("Gtk")[1:])

    def __repr__(self):
        return f"Control(name={self.name}, type={self.type_}, ptr_t={self.ptr_t})"

class Event:
    def __init__(self, ctrl: Control, name: str, handler: str):
        self.ctrl = weakref.proxy(ctrl)
        self.name = name
        self.handler = handler

    def __repr__(self):
        return f"Event(ctrl={self.ctrl.name}, name={self.name}, handler={self.handler})"


def cpp(controls, events):
    header_templ = Template(filename="events.hpp.mako")    
    src_templ = Template(filename="events.cc.mako")    
    with open("./events.hpp", "w") as header:
        header.write(header_templ.render(guard="EVENTS_HPP", controls=controls, events=events))
    print("header")
    with open("./events.cc", "w") as src:
        src.write(src_templ.render(header_path="events.hpp", controls=controls, events=events))

def python3(controls, events):
    py_templ = Template(filename="ui.py.mako")
    text = py_templ.render(cls_name="UI", controls=controls, events=events)
    with open("./ui.py", "w") as src:
        src.write(text)

def main():
    file = os.path.abspath( "../main_window.glade")
    tree = ElementTree.parse(file)
    root = tree.getroot()
    controls = []
    events = []

    for c in root.findall(".//object[@id]"):
        name = c.get("id")
        ctrl = Control(name, c.get("class")) 
        controls.append(ctrl)
        for x in c.findall("signal"):
            event = Event(ctrl, x.get("name"), x.get("handler"))
            if event.name == "draw":
                event.args = ("ctx",)
            ctrl.events.append(event)
            events.append(event)
    python3(controls, events)


if __name__ == "__main__":
    main()






from .model import GraphicalModel
import weakref
from util import pop_msg
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk


class WindowEventHandler:
    def __init__(self, app_handler: "ApplicationHandler"):
        """
        :param app_handler: Handler for events of the whole application
        """
        self.app_handler: ApplicationHandler = weakref.proxy(app_handler)
        self.model: GraphicalModel = weakref.proxy(app_handler.model)

    def entries(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if isinstance(attr, Gtk.Entry):
                yield attr

    def check_numeric_entries(self):
        for entry in self.entries():
            p = entry.get_input_purpose()
            if p == Gtk.InputPurpose.NUMBER:
                try:
                    float(entry.get_text())
                except ValueError:
                    entry.grab_focus()
                    pop_msg(entry, "Invalid real number").show_all()
                    return False
        return True

    def check_name(self, entry: Gtk.Entry):
        valid = entry.get_text() not in self.model.display_file
        if not valid:
            pop_msg(entry, "An object with this name already exists")
        return valid


class ApplicationHandler:
    def __init__(self, model: GraphicalModel = ...):
        if model is ...:
            model = GraphicalModel()
        self.model: GraphicalModel = model

    @property
    def main_window(self) -> WindowEventHandler:
        raise NotImplemented

    @staticmethod
    def clean_entries(win: WindowEventHandler):
        for entry in win.entries():
            p = entry.get_input_purpose()
            if p == Gtk.InputPurpose.NUMBER:
                entry.set_text("0.0")
            else:
                entry.set_text("")

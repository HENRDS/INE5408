from core import GraphicalModel, WindowEventHandler, ApplicationHandler
from cairo import Context
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk


%for win in gui.windows:
class ${win.cls_name}(WindowEventHandler):
    def __init__(self, app_handler: "${gui.cls_name}", builder: Gtk.Builder):
        super().__init__(app_handler)
        self.win: ${win.py_type} = builder.get_object("${win.name}")
    % for control in win.controls:
        self.${control.name}: ${control.py_type} = builder.get_object("${control.name}")
    % endfor
    % for event in win.events:
        self.win.connect("${event.name}", self.${event.handler})
    %endfor
    % for control in win.controls:
    %if control.events:
        # ${control.name} handlers
    %endif
    % for event in control.events:
        self.${control.name}.connect("${event.name}", self.${event.handler})
    %endfor
    % endfor
% for event in win.all_events:

    def ${event.handler}(self, sender: ${event.ctrl.py_type}\
%if event.args:
, ${', '.join(event.args)}\
%endif
) -> None:
        """Handler for event '${event.name}' of control ${event.ctrl.name}."""
        pass
%endfor


%endfor
class ${gui.cls_name}(ApplicationHandler):
%for win in gui.windows:
    ${win.attr_name} = ${win.cls_name}
%endfor

    def __init__(self, model: GraphicalModel = ...):
        super().__init__(model)
    %for path, controls in gui.files():
        builder = Gtk.Builder.new_from_file("${path}")
    %for control in controls:
    %if isinstance(control, Window):
        self.${control.name}: ${control.cls_name} = self.${control.attr_name}(self, builder)
    %else:
        self.${control.name}: ${control.py_type} = builder.get_object("${control.name}")
    %endif
    %endfor
    %endfor
        self.main_window.win.connect("destroy", Gtk.main_quit)


    @property
    def main_window(self):
        return self.${gui.main_window}

    def show(self):
        self.main_window.win.show()
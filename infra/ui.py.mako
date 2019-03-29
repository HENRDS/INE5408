from shapes import GraphicalObject
from cairo import Context
from typing import List
from weakref import proxy
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk, GObject


%for win in windows:
class ${win.cls_name}:
    def __init__(self, app_handler: "${cls_name}", builder: Gtk.Builder):
        self.app_handler: "${cls_name}" = proxy(app_handler)
        self.win: ${win.py_type} = builder.get_object("${win.name}")
    % for control in win.controls:
        self.${control.name}: ${control.py_type} = builder.get_object("${control.name}")
    % endfor
    % for control in win.controls:
    %if control.events:
        # ${control.name}
    %endif
    % for event in control.events:
        self.${control.name}.connect("${event.name}", self.${event.handler})
    %endfor
    % endfor
% for event in win.events:

    def ${event.handler}(self, sender: ${event.ctrl.py_type}\
%if hasattr(event, "args"):
, ${', '.join(event.args)}\
%endif
) -> None:
        pass
%endfor


%endfor
class ${cls_name}:
%for win in windows:
    ${win.attr_name} = ${win.cls_name}
%endfor

    def __init__(self, builder: Gtk.Builder):
        self.display_file: List[GraphicalObject] = []
    %for win in windows:
        self.${win.name}: ${win.py_type} = self.${win.attr_name}(self, builder)
    %endfor
    %for prop in props:
        self.${prop.name}: ${prop.py_type} = builder.get_object("${control.name}")
    %endfor

    % for control in win.controls:
    %if control.events:
        # ${control.name}
    %endif
    % for event in prop.events:
        self.${control.name}.connect("${event.name}", self.${event.handler})
    %endfor
    % endfor
        self.${main_window}.win.connect("destroy", Gtk.main_quit)

    def show(self):
        self.${main_window}.win.show()

% for event in win.events:
    def ${event.handler}(self, sender: ${event.ctrl.py_type}\
%if hasattr(event, "args"):
, ${', '.join(event.args)}\
%endif
) -> None:
        pass

%endfor
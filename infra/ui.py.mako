from cairo import Context
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk, GObject


%for win in windows:
class ${win.cls_name}:
    def __init__(self, builder: Gtk.Builder):
    % for control in win.controls:
        self.${control.name}: Gtk.${control.py_type} = builder.get_object("${control.name}")
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
    %for prop in props:
        self.${prop.name}: Gtk.${prop.py_type} = self.${win.attr_name}(builder)
    %endfor


        self.main_window.connect("destroy", Gtk.main_quit)

    def show(self):
        self.main_window.show()

% for event in win.events:
    def ${event.handler}(self, sender: ${event.ctrl.py_type}\
%if hasattr(event, "args"):
, ${', '.join(event.args)}\
%endif
) -> None:
        pass

%endfor
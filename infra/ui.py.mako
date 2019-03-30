from cairo import Context
from weakref import proxy
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk


class WindowEventHandler:
    def __init__(self, app_handler: "${cls_name}", builder: Gtk.Builder):
        """
        :param app_handler: Handler for events of the whole application
        :param builder: GtkBuilder used to load the controls, windows and connect their signals
        :type Gtk.Builder
        """
        self.app_handler: "${cls_name}" = proxy(app_handler)


%for win in windows:
class ${win.cls_name}(WindowEventHandler):
    def __init__(self, app_handler: "${cls_name}", builder: Gtk.Builder):
        super().__init__(app_handler, builder)
        self.win: ${win.py_type} = builder.get_object("${win.name}")
    % for control in win.controls:
        self.${control.name}: ${control.py_type} = builder.get_object("${control.name}")
    % endfor
    % for control in win.controls:
    %if control.events:
        # ${control.name} handlers
    %endif
    % for event in control.events:
        self.${control.name}.connect("${event.name}", self.${event.handler})
    %endfor
    % endfor
% for event in win.events:

    def ${event.handler}(self, sender: ${event.ctrl.py_type}\
%if event.args:
, ${', '.join(event.args)}\
%endif
) -> None:
        """Handler for event '${event.name}' of control ${event.ctrl.name}."""
        pass
%endfor


%endfor
class ${cls_name}:
%for win in windows:
    ${win.attr_name} = ${win.cls_name}
%endfor

    def __init__(self, builder: Gtk.Builder):
    %for win in windows:
        self.${win.name}: ${win.cls_name} = self.${win.attr_name}(self, builder)
    %endfor
        self.${main_window}.win.connect("destroy", Gtk.main_quit)

    def show(self):
        self.${main_window}.win.show()
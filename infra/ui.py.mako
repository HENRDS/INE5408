import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk, GObject
import abc

class ${cls_name}:
    def __init__(self, builder: Gtk.Builder):
    % for control in controls:
        self.${control.name}: Gtk.${control.type_.lstrip("Gtk")} = builder.get_object("${control.name}")
    % endfor
    % for control in controls:
    %if control.events:
        # ${control.name}
    %endif
    % for event in control.events:
        self.${control.name}.connect("${event.name}", self.${event.handler})
    %endfor
    % endfor
    
        self.main_window.connect("destroy", Gtk.main_quit)

    def show(self):
        self.main_window.show()

% for event in events:
    @abc.abstractmethod
    def ${event.handler}(self\
%if hasattr(event, "args"):
, ${', '.join(event.args)}\
%endif
) -> None:
        pass

%endfor
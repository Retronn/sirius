import bpy
from .takeoff_grid import TakeoffGridPanel
from .led_control import LEDControlPanel

def register():
    bpy.utils.register_class(TakeoffGridPanel)
    bpy.utils.register_class(LEDControlPanel)

def unregister():
    bpy.utils.unregister_class(TakeoffGridPanel)
    bpy.utils.unregister_class(LEDControlPanel)

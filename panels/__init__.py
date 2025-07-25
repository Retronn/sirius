import bpy
from .takeoff_grid import TakeoffGridPanel

def register():
    bpy.utils.register_class(TakeoffGridPanel)


def unregister():
    bpy.utils.unregister_class(TakeoffGridPanel)

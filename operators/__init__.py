import bpy
from .create_takeoff_grid import CreateTakeoffGrid
from .change_led_color import ChangeLEDColor

def register():
    bpy.utils.register_class(CreateTakeoffGrid)
    bpy.utils.register_class(ChangeLEDColor)


def unregister():
    bpy.utils.unregister_class(CreateTakeoffGrid)
    bpy.utils.unregister_class(ChangeLEDColor)

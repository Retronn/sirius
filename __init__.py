from . import panels, operators, props, materials


bl_info = {
    "name": "Sirius",
    "author": "Alexandr Tkachyov",
    "version": (1, 0, 0),
    "blender": (4, 3, 2),
    "location": "View3D > Sidebar > Sirius",
    "description": "Create and manage drone show formations and flight paths.",
    "category": "Object"
}


def register():
    props.register()
    operators.register()
    panels.register()
    


def unregister():
    props.unregister()
    materials.unregister()
    operators.unregister()
    panels.unregister()
    
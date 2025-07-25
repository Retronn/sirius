
from .drone_emission_material import create_drone_emission_material, delete_drone_emission_material

def register():
    create_drone_emission_material()

def unregister():
    delete_drone_emission_material()
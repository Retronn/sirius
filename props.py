import bpy 

class DroneShowSettings(bpy.types.PropertyGroup):
    
    drone_count: bpy.props.IntProperty(
        name="Number of Drones",
        default = 100,
        min = 1,
        max=1000,
        description = "Total number of drones in the show"
    )    
    
    rows_count: bpy.props.IntProperty(
        name="Rows",
        default = 10,
        min = 1,
        max=1000,
        description = "Total number of rows in the takeoff grid"
    )  
    
    cols_count: bpy.props.IntProperty(
        name="Columns",
        default = 10,
        min = 1,
        max=1000,
        description = "Total number of columns in the takeoff grid"
    )  
    
    horizontal_spacing: bpy.props.FloatProperty(
        name="Horizontal Spacing (m)",
        default = 3,
        min = 0.5,
        max=20,
        description = "Spacing between the columns in meters"
    )      
    
    vertical_spacing: bpy.props.FloatProperty(
        name="Vertical Spacing (m)",
        default = 3,
        min = 0.5,
        max=20,
        description = "Spacing between the rows in meters"
    )     



def register():
    print("Regsisisidianiaf")
    bpy.utils.register_class(DroneShowSettings) 
    bpy.types.Scene.my_props = bpy.props.PointerProperty(type=DroneShowSettings)

def unregister():
    del bpy.types.Scene.my_props
    bpy.utils.unregister_class(DroneShowSettings) 
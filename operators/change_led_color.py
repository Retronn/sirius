import bpy

class ChangeLEDColor(bpy.types.Operator):

    bl_idname="object.change_drone_led_color"
    bl_label= "Change Drone LED Color"
    bl_description = "Applies LED color to all selected drones"

    def execute(self,context):
        
        props = context.scene.my_props

        drones_to_change = []

        if(props.apply_to_all_drones):
            for coll in bpy.data.collections:
                if(coll.name=="Drones"):
                    drones_collection = coll
            for object in drones_collection.objects:
                if(object.name.startswith("Drone")):
                    drones_to_change.append(object)
        else:
            for object in context.selected_objects:
                if(object.name.startswith("Drone")):
                    drones_to_change.append(object)
    
        for drone in drones_to_change:
            for material in drone.data.materials:
                if(material.name.startswith("LED color of")):
                    emission = material.node_tree.nodes.get('Drone Glow')
                    emission.inputs["Strength"].default_value = props.glow_strength
                    emission.inputs["Color"].default_value = list(props.drone_color) + [1.0]  

        props.apply_to_all_drones = False
        return {'FINISHED'}
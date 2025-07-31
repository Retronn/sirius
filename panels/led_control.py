import bpy


class LEDControlPanel(bpy.types.Panel):
    bl_label = "LED Control"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sirius'

    def draw(self,context):
        props = context.scene.my_props
        layout = self.layout

        layout.label(text="Drone Color")
        layout.prop(props, 'drone_color')
        layout.prop(props, 'glow_strength')
        layout.prop(props, "apply_to_all_drones")
        layout.operator("object.change_drone_led_color")
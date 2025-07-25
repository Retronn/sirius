import bpy

class TakeoffGridPanel(bpy.types.Panel):
    bl_label = 'Takeoff Grid'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sirius'
    
    
    
    def draw(self, context):
        props = context.scene.my_props
        layout = self.layout

        layout.label(text="Grid")
        layout.prop(props, 'drone_count')
        layout.prop(props, 'rows_count')
        layout.prop(props, 'cols_count')

        layout.separator()

        layout.label(text="Spacing")
        layout.prop(props, 'horizontal_spacing')
        layout.prop(props, 'vertical_spacing')

        layout.separator()
        
        layout.operator("object.create_takeoff_grid")
        
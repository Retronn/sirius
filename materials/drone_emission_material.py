import bpy

def create_drone_emission_material():
    if "DroneEmissionMaterial" not in bpy.data.materials:
        mat = bpy.data.materials.new(name="DroneEmissionMaterial")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        nodes.clear()

        emission = nodes.new(type="ShaderNodeEmission")
        emission.inputs["Color"].default_value = (1,1,1,1)
        emission.inputs["Strength"].default_value = 5.0

        output = nodes.new(type="ShaderNodeOutputMaterial")
        links.new(emission.outputs["Emission"], output.inputs["Surface"])


def delete_drone_emission_material():
    if "DroneEmissionMaterial" in bpy.data.materials:
        bpy.data.materials.remove(bpy.data.materials["DroneEmissionMaterial"])

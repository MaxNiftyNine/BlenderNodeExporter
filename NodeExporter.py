import bpy
import os

def export_material_nodes():
    # Get the active material
    material = bpy.context.object.active_material
    
    if material is None:
        print("No active material found.")
        return
    
    # Get the user's home directory
    user_path = os.path.expanduser("~")
    
    # Create the file path for exporting
    filepath = os.path.join(user_path, "exported_material_nodes.txt")
    
    # Open the file for writing
    with open(filepath, 'w') as file:
        # Write material name
        file.write("Material: {}\n".format(material.name))
        
        # Iterate over material nodes
        for node in material.node_tree.nodes:
            # Write node type and name
            file.write("Node: {}\n".format(node.type))
            
            # Check if it's a node group
            if node.type == 'GROUP':
                # Get the internal nodes of the node group
                group = bpy.data.node_groups[node.node_tree.name]
                for internal_node in group.nodes:
                    # Write internal node type and name
                    file.write("\tInternal Node: {}\n".format(internal_node.type))
                    # Write internal node attributes
                    for attr in internal_node.inputs.keys():
                        value = get_socket_value(internal_node.inputs[attr])
                        file.write("\t\t{}: {}\n".format(attr, value))
            else:
                # Write node attributes
                for attr in node.inputs.keys():
                    value = get_socket_value(node.inputs[attr])
                    file.write("\t{}: {}\n".format(attr, value))
            
            # Write node connections
            for input_socket in node.inputs:
                if input_socket.is_linked:
                    for connection in input_socket.links:
                        output_node = connection.from_node
                        output_socket = connection.from_socket
                        output_attr = output_socket.name
                        file.write("\tConnection: {} --> {} --> {}\n".format(output_node.name, node.type, output_attr))
            
            file.write("\n")  # Add a blank line after each node
            
        print("Material nodes exported to", filepath)


def get_socket_value(socket):
    if socket.is_linked:
        return "Linked"
    else:
        if socket.type == 'VALUE':
            return socket.default_value
        elif socket.type == 'RGBA':
            return socket.default_value[:3]  # Exclude alpha value
        elif socket.type == 'VECTOR':
            return tuple(socket.default_value)
        else:
            return "Not Applicable"


# Usage
export_material_nodes()

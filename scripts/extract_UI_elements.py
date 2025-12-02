import xml.etree.ElementTree as ET
import os

def get_tag(node):
    resource_id = node.attrib.get('resource-id', '')
    text = node.attrib.get('text', '')
    class_name = node.attrib.get('class', '')

    if resource_id:
        tag = resource_id.split('/')[-1]
    elif text:
        tag = text
    elif class_name:
        tag = class_name.split('.')[-1]
    else:
        tag = "unknown"

    tag = tag.replace(' ', '_').replace(':', '_')
    return tag

def get_ui_type(class_name):
    # define tipos básicos por class_name
    if 'Button' in class_name:
        return 'Button'
    elif 'EditText' in class_name or 'TextField' in class_name:
        return 'TextField'
    elif 'TextView' in class_name:
        return 'Text'
    else:
        return 'View'

def write_node_txt(node, file, indent=0):
    class_name = node.attrib.get('class', '')
    ui_type = get_ui_type(class_name)
    tag = get_tag(node)
    clickable = node.attrib.get('clickable', 'false')
    enabled = node.attrib.get('enabled', 'false')
    bounds = node.attrib.get('bounds', '')
    text = node.attrib.get('text', '').replace('\n', ' ').replace('\r', '')

    line = f'{ui_type}(tag="{tag}", clickable={clickable}, enabled={enabled}, bounds="{bounds}"'
    if text:
        line += f', text="{text}"'
    line += ')\n'

    file.write(line)

    for child in node.findall('node'):
        write_node_txt(child, file, indent + 1)

def parse_and_save_txt(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    folder = os.path.dirname(xml_path)
    output_path = os.path.join(folder, "ui_elements.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        for node in root.findall('node'):
            write_node_txt(node, f)

    print(f"arquivo salvo em: {output_path}")


#add paths
#xml_path = 


parse_and_save_txt(xml_path)

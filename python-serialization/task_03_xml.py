#!/usr/bin/python3
"""explore serialization and deserialization using XML
as an alternative format to JSON"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize the dictionary into XML and save it
    to the given filename

    Args:
        dictionary (_type_): _description_
        filename (_type_): _description_
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            # Create a child element with the key as tag
            child = ET.SubElement(root, key)
            # Set the element's text content to the string
            # representation of the value
            child.text = str(value)

        # Create an ElementTree from the root and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """read the XML data from that file, and return
    a deserialized Python dictionary

    Args:
        filename (_type_): _description_
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()  # <data> element

        result = {}
        # Iterate over each child element
        for child in root:
            key = child.tag
            value = child.text

            # Convert text to appropriate Python type
            if value is not None:
                value = (
                    value.strip()
                )  # Remove leading/trailing whitespace
                # Try integer
                try:
                    value = int(value)
                except ValueError:
                    # Try float
                    try:
                        value = float(value)
                    except ValueError:
                        # Try boolean (case-insensitive)
                        if value.lower() == "true":
                            value = True
                        elif value.lower() == "false":
                            value = False
                        else:
                            # Keep as string
                            value = value
            else:
                value = ""  # or None, but empty string is common
                # for empty elements
            result[key] = value
        return result
    except Exception:
        return False

from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd


def childnodes(child_id):
    number = 0
    for term_child in terms:
        id_node_child = term_child.getElementsByTagName("id")[0]
        is_a_nodes = term_child.getElementsByTagName("is_a")
        for is_a_node in is_a_nodes:
            is_a_value = is_a_node.firstChild.nodeValue
            if child_id == is_a_value:
                number += childnodes(id_node_child.firstChild.nodeValue) + 1
    return number  # Use a recursive algorithm to calculate the number of child nodes


data = {'id': [], 'name': [], 'definition': [], 'childNodes': []}
DOMTree = xml.dom.minidom.parse("go_obo.xml")  # Parse the XML file into a DOM document object.
collection = DOMTree.documentElement  # Get the root element of the document
terms = collection.getElementsByTagName("term")  # Take out the list of "term"
for term in terms:
    id_node = term.getElementsByTagName("id")[0]
    name_node = term.getElementsByTagName("name")[0]
    defstr_node = term.getElementsByTagName("defstr")[0]  # Return the nodelists of id, name and defstr
    if "autophagosome" in defstr_node.firstChild.nodeValue:
        childNodes = childnodes(id_node.firstChild.nodeValue)
        data['id'].append(id_node.firstChild.nodeValue)
        data['name'].append(name_node.firstChild.nodeValue)
        data['definition'].append(defstr_node.firstChild.nodeValue)
        data['childNodes'].append(childNodes)  # If a 'defstr' has the 'autophagosome', store the above data into a list as temporary data
df = pd.DataFrame(data)
df.to_excel("autophagosome.xlsx", index=False)

from enum import Enum 

from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum): 
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text 
        self.text_type = text_type
        self.url = url 
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(node):
    if node.text_type not in TextType:
        raise Exception
    if node.text_type.name == "LINK":
        html = LeafNode(node.text_type.value, node.text, {"href": node.url})
    elif node.text_type.name == "IMAGE":
        html = LeafNode(node.text_type.value, "", {"src": node.url, "alt": node.txt})
    else: 
        html = LeafNode(node.text_type.value, node.text)
    return html

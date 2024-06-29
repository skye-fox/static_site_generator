"""Module to handle functionality of text nodes"""

from htmlnode import LeafNode


class TextNode:
    """Class for creating text nodes."""

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode{self.text, self.text_type, self.url}"


def text_node_to_html_node(text_node):
    """Function to convert text nodes into LeafNodes."""
    types = ["text", "bold", "italic", "code", "link", "image"]

    if text_node.text_type in types:
        if text_node.url is not None:
            if text_node.text_type == "link":
                return LeafNode(
                    tag="a",
                    value=text_node.text,
                    props={"href": text_node.url},
                )
            return LeafNode(
                tag="img",
                value="",
                props={"src": text_node.url, "alt": text_node.text},
            )
        if text_node.text_type == "text":
            return LeafNode(value=text_node.text)
        if text_node.text_type == "bold":
            return LeafNode(tag="b", value=text_node.text)
        if text_node.text_type == "italic":
            return LeafNode(tag="i", value=text_node.text)
        return LeafNode(tag=text_node.text_type, value=text_node.text)
    raise TypeError(
        "text node type must be one of: text, bold, italic, code, link, image"
    )

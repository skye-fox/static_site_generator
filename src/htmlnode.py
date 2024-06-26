"""This module implements the classes used to process inputs to html."""


class HTMLNode:
    """Class for building html nodes"""

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """Method for processing inputs to html. Overridden in child classes."""
        raise NotImplementedError(
            "to_html can only be called on child classes of HTMLNode"
        )

    def props_to_html(self):
        """Method for processing the props dictionary into appropriate html output"""
        if self.props is not None:
            html = ""
            for key, value in self.props.items():
                html += f" {key}={value}"
            return html
        return ""

    def __repr__(self):
        return f"HTMLNode{self.tag, self.value, self.children, self.props}"


class LeafNode(HTMLNode):
    """Class to process an HTMLNode that has can't have children."""

    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required")

        if self.tag is None:
            return self.value

        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    """Class for processing HTMLNodes that must have children."""

    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        result = f"<{self.tag}>"
        if self.tag is None:
            raise ValueError("tag property is required")
        if self.children is None:
            raise ValueError("children property is required")
        result = ""
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"

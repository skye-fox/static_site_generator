class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(
            "to_html can only be called on child classes of HTMLNode"
        )

    def props_to_html(self):
        if self.props is not None:
            html = ""
            for key, value in self.props.items():
                html += f"{key}={value} "
            return html.strip()
        return None

    def __repr__(self):
        return f"HTMLNode{self.tag, self.value, self.children, self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required")

        if self.tag is None:
            return self.value

        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        result = f"<{self.tag}>"
        if self.tag is None:
            raise ValueError("tag property is required")
        if self.children is None:
            raise ValueError("children property is required")
        if self.props is None:
            if len(self.children) < 1:
                return result
            for child in self.children:
                result += child.to_html()
            return f"{result}</{self.tag}>"
        result = f"<{self.tag} {self.props_to_html()}>"
        if len(self.children) < 1:
            return result
        for child in self.children:
            result += child.to_html()
        return f"{result}</{self.tag}>"

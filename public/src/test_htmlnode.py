import unittest

from htmlnode import HTMLNode, LeafNode

test_dict = {"href": '"https://www.google.com"', "target": '"_blank"'}
test_dict2 = {"href": '"https://www.google.com"'}


class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = HTMLNode(props=test_dict)
        self.assertEqual(
            node.props_to_html(), 'href="https://www.google.com" target="_blank"'
        )


class TestLeafNode(unittest.TestCase):
    def test(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", test_dict2)
        print(f"node 2: {node2}")
        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(
            node2.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

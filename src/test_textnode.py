"""Module for testing text node module"""

import unittest

from htmlnode import LeafNode
from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    """Class for testing TextNodes."""

    def test_eq(self):
        """Test if two TextNode instances without url are equal"""

        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        """Test if two TextNode instances with url are equal"""

        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        """Test if two TextNode instances are not equal"""

        node3 = TextNode("This is a text node", "bold")
        node4 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node3, node4)

    def test_not_eq2(self):
        """Test if two TextNode instances are not equal"""
        node3 = TextNode("This is  text node", "bold")
        node4 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node3, node4)

    def test_not_eq3(self):
        """Test if two TextNode instances are not equal"""
        node3 = TextNode("This is a text node", "italic")
        node4 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node3, node4)


text_node1 = TextNode("Hello World", "bold")
text_node2 = TextNode("Hello World", "italic")
text_node3 = TextNode("Hello World", "text")
text_node4 = TextNode("print('hello world')", "code")
text_node5 = TextNode(
    '"boot.dev logo"',
    "image",
    '"https://www.boot.dev/img/bootdev-logo-full-small.webp"',
)
text_node6 = TextNode(
    "Click me!",
    "link",
    '"https://www.boot.dev"',
)


class TestTextNodeToHtmlNode(unittest.TestCase):
    """Class to test the text_node_to_html_node function."""

    def test1_eq(self):
        """Test to see if html output of a node with the bold tag created by
        the function is equal to the html output of a node created by hand"""

        node = text_node_to_html_node(text_node1)
        self.assertEqual(node.to_html(), LeafNode("bold", "Hello World").to_html())

    def test2_eq(self):
        """Test to see if html output of a node with the italic tag created by
        the function is equal to the html output of a node created by hand"""

        node = text_node_to_html_node(text_node2)
        self.assertEqual(node.to_html(), LeafNode("italic", "Hello World").to_html())

    def test3_eq(self):
        """Test to see if html output of a node with no tag created by
        the function is equal to the html output of a node created by hand"""

        node = text_node_to_html_node(text_node3)
        self.assertEqual(node.to_html(), LeafNode(None, "Hello World").to_html())

    def test4_eq(self):
        """Test to see if html output of a node with the code tag created by
        the function is equal to the html output of a node created by hand"""

        node = text_node_to_html_node(text_node4)
        self.assertEqual(
            node.to_html(), LeafNode("code", "print('hello world')").to_html()
        )

    def test5_eq(self):
        """Test to see if html output of a node with the image tag created by
        the function is equal to the html output of a node created by hand"""

        node = text_node_to_html_node(text_node5)
        self.assertEqual(
            node.to_html(),
            LeafNode(
                "img",
                "",
                {
                    "src": '"https://www.boot.dev/img/bootdev-logo-full-small.webp"',
                    "alt": '"boot.dev logo"',
                },
            ).to_html(),
        )

    def test6_eq(self):
        """Test to see if html output of a node with the anchor tag created by
        the function is equal to the html output of a node created by hand"""

        node = text_node_to_html_node(text_node6)
        self.assertEqual(
            node.to_html(),
            LeafNode(
                "a",
                "Click me!",
                {"href": '"https://www.boot.dev"'},
            ).to_html(),
        )


if __name__ == "__main__":
    unittest.main()

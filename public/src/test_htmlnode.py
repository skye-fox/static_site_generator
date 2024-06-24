"""This module is for testing the html node module"""

import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

test_dict = {"href": '"https://www.google.com"', "target": '"_blank"'}
test_dict2 = {"href": '"https://www.google.com"'}
test_dict3 = {
    "src": '"https://www.boot.dev/img/bootdev-logo-full-small.webp"',
    "alt": '"boot.dev logo"',
}
test_list = [
    LeafNode("b", "Bold text"),
    LeafNode(None, "Normal text"),
    LeafNode("i", "italic text"),
    LeafNode(None, "Normal text"),
]
test_list2 = [
    LeafNode("ul", "item 1"),
    LeafNode("ul", "item 2"),
    LeafNode("ul", "item 3"),
    LeafNode("ul", "item 4"),
]
node_1 = LeafNode("a", "item 1", test_dict2)
node_2 = LeafNode("a", "item 2", test_dict2)
node_3 = LeafNode("a", "item 3", test_dict2)
node_4 = LeafNode("a", "item 4", test_dict2)
ul_node1 = LeafNode("ul", node_1.to_html())
ul_node2 = LeafNode("ul", node_2.to_html())
ul_node3 = LeafNode("ul", node_3.to_html())
ul_node4 = LeafNode("ul", node_4.to_html())
test_list3 = [
    ul_node1,
    ul_node2,
    ul_node3,
    ul_node4,
]


class TestHTMLNode(unittest.TestCase):
    """Tests for the HTMLNode class."""

    def test_eq(self):
        """Test for the props_to_html method."""
        node = HTMLNode(props=test_dict)
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )


class TestLeafNode(unittest.TestCase):
    """Tests for the LeafNode class."""

    def test1_eq(self):
        """Test paragraph tags."""
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test2_eq(self):
        """Test anchor tags."""
        node = LeafNode("a", "Click me!", test_dict2)
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test3_eq(self):
        """Test nested LeafNodes."""
        self.assertEqual(
            ul_node1.to_html(), '<ul><a href="https://www.google.com">item 1</a></ul>'
        )

    def test4_eq(self):
        """Test img tags."""
        node = LeafNode("img", "", props=test_dict3)
        self.assertEqual(
            node.to_html(),
            '<img src="https://www.boot.dev/img/bootdev-logo-full-small.webp" alt="boot.dev logo">',
        )


class TestParentNode(unittest.TestCase):
    """Test for the ParentNode class."""

    def test1_eq(self):
        """Test ParentNode functionality without props."""
        node = ParentNode("p", test_list)
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test2_eq(self):
        """Test ParentNode functionality with props."""
        node = ParentNode("a", test_list, test_dict2)
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</a>',
        )

    def test3_eq(self):
        """Test ParentNode use with lists."""
        node = ParentNode("li", test_list2)
        self.assertEqual(
            node.to_html(),
            "<li><ul>item 1</ul><ul>item 2</ul><ul>item 3</ul><ul>item 4</ul></li>",
        )

    def test4_eq(self):
        """Testing ParentNode with many different nested LeafNodes."""
        node = ParentNode("li", test_list3)
        self.assertEqual(
            node.to_html(),
            '<li><ul><a href="https://www.google.com">item 1</a></ul><ul><a href="https://www.google.com">item 2</a></ul><ul><a href="https://www.google.com">item 3</a></ul><ul><a href="https://www.google.com">item 4</a></ul></li>',
        )

    def test5_eq(self):
        """Test nested ParentNodes with nested LeafNodes."""
        node = ParentNode("p", test_list)
        node2 = ParentNode("a", [node], test_dict2)
        self.assertEqual(
            node2.to_html(),
            '<a href="https://www.google.com"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></a>',
        )

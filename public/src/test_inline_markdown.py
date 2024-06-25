"""This module is for testing the inline_markdown module"""

import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    """Class to test the split_nodes_delimiter function"""

    def test1_eq(self):
        """Test split_nodes_delimiter function for code type"""

        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a", "text"),
                TextNode("code block", "code"),
                TextNode("word", "text"),
            ],
        )

    def test2_eq(self):
        """Test split_nodes_delimiter function for bold type"""

        node = TextNode("This is text with a **bold** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a", "text"),
                TextNode("bold", "bold"),
                TextNode("word", "text"),
            ],
        )

    def test3_eq(self):
        """Test split_nodes_delimiter function for italic type"""

        node = TextNode("This is text with a *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a", "text"),
                TextNode("italic", "italic"),
                TextNode("word", "text"),
            ],
        )

    def test4_eq(self):
        """Test split_nodes_delimiter function for multiple occurances in the string"""

        node = TextNode(
            "**This** is text with a **bold** word and also a few **bold words**",
            "text",
        )
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This", "bold"),
                TextNode("is text with a", "text"),
                TextNode("bold", "bold"),
                TextNode("word and also a few", "text"),
                TextNode("bold words", "bold"),
            ],
        )

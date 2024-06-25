"""This module is for testing the inline_markdown module"""

import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
)
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


class ExtractMarkdownImagesAndLinks(unittest.TestCase):
    """Class for testing the extract_markdown_images & extract_markdown_links functions"""

    def test_image_extraction(self):
        """Test to check that the function properly extracts alt text and the url"""
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        images = [
            (
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            (
                "another",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png",
            ),
        ]
        self.assertEqual(extract_markdown_images(text), images)

    def test_link_extraction(self):
        """Test to check that the function properly extracts anchor text and the url"""
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        links = [
            ("link", "https://www.example.com"),
            ("another", "https://www.example.com/another"),
        ]
        self.assertEqual(extract_markdown_links(text), links)

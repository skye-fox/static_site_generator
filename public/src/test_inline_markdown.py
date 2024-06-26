"""This module is for testing the inline_markdown module"""

# pylint: disable=line-too-long
import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
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


node1 = TextNode(
    "This is an ![image](https://www.boot.dev/img/bootdev-logo-full-small.webp) it's the only one",
    "text",
)
list1 = [
    TextNode("This is an ", "text"),
    TextNode("image", "image", "https://www.boot.dev/img/bootdev-logo-full-small.webp"),
    TextNode(" it's the only one", "text"),
]

node2 = TextNode(
    "This is text with an ![image](https://www.boot.dev/img/bootdev-logo-full-small.webp) and another ![second image](https://www.boot.dev/img/bootdev-logo-full-small.webp)",
    "text",
)
list2 = [
    TextNode("This is text with an ", "text"),
    TextNode("image", "image", "https://www.boot.dev/img/bootdev-logo-full-small.webp"),
    TextNode(" and another ", "text"),
    TextNode(
        "second image", "image", "https://www.boot.dev/img/bootdev-logo-full-small.webp"
    ),
]

node3 = TextNode(
    "![image](https://www.boot.dev/img/bootdev-logo-full-small.webp) This is text after an image",
    "text",
)
list3 = [
    TextNode("image", "image", "https://www.boot.dev/img/bootdev-logo-full-small.webp"),
    TextNode(" This is text after an image", "text"),
]

node4 = TextNode(
    "This is text with an ![image](https://www.boot.dev/img/bootdev-logo-full-small.webp) and another ![second image](https://www.boot.dev/img/bootdev-logo-full-small.webp) and yet another ![third image](https://www.boot.dev/img/bootdev-logo-full-small.webp) and some trailing text",
    "text",
)
list4 = [
    TextNode("This is text with an ", "text"),
    TextNode("image", "image", "https://www.boot.dev/img/bootdev-logo-full-small.webp"),
    TextNode(" and another ", "text"),
    TextNode(
        "second image", "image", "https://www.boot.dev/img/bootdev-logo-full-small.webp"
    ),
    TextNode(" and yet another ", "text"),
    TextNode(
        "third image", "image", "https://www.boot.dev/img/bootdev-logo-full-small.webp"
    ),
    TextNode(" and some trailing text", "text"),
]


class SplitNodesImage(unittest.TestCase):
    """Class for testing split_nodes_image function"""

    def test_image_split(self):
        """Test if function works"""
        self.assertEqual(split_nodes_image([node1]), list1)

    def test_image_at_end(self):
        """Test if function works when image is at the end of the string"""
        self.assertEqual(split_nodes_image([node2]), list2)

    def test_image_at_start(self):
        """Test if function works when image is at the start of the string"""
        self.assertEqual(split_nodes_image([node3]), list3)

    def test_multiple_images(self):
        """Test if function works with multiple images throughout string"""
        self.assertEqual(split_nodes_image([node4]), list4)

    def test_image_only(self):
        """Test if function works when the string is only an image"""
        node = TextNode(
            "![image](https://www.boot.dev/img/bootdev-logo-full-small.webp)", "text"
        )
        lst = [
            TextNode(
                "image",
                "image",
                "https://www.boot.dev/img/bootdev-logo-full-small.webp",
            )
        ]
        self.assertEqual(split_nodes_image([node]), lst)

    def test_multiple_lists(self):
        """test if function works given many nodes in the list"""
        lst = [node1, node2, node3, node4]
        lst2 = list1 + list2 + list3 + list4
        self.assertEqual(split_nodes_image(lst), lst2)

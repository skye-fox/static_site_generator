"""This is a module for testing the block_markdown.py module"""

# pylint: disable=line-too-long

import unittest

from block_markdown import (
    BLOCK_TYPE_CODE,
    BLOCK_TYPE_HEADING,
    BLOCK_TYPE_ORDERED_LIST,
    BLOCK_TYPE_PARAGRAPH,
    BLOCK_TYPE_QUOTE,
    BLOCK_TYPE_UNORDERED_LIST,
    block_to_block_type,
    code_block_to_html,
    heading_block_to_html,
    markdown_to_blocks,
    ordered_list_block_to_html,
    quote_block_to_html,
    unordered_list_block_to_html,
)
from htmlnode import LeafNode, ParentNode


class TestBlockMarkdown(unittest.TestCase):
    """This is a class for testing the block_markdown.py module"""

    def test_markdown_to_blocks(self):
        """Test function markdown_to_blocks"""
        document = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        self.assertEqual(
            markdown_to_blocks(document),
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type_h1(self):
        """Test h1 heading block"""
        block = "# This is an H1 heading"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_HEADING)

    def test_block_to_block_type_h3(self):
        """Test h3 heading block"""
        block = "### This is an H3 heading"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_HEADING)

    def test_block_to_block_type_h6(self):
        """Test h6 heading block"""
        block = "###### This is an H6 heading"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_HEADING)

    def test_block_to_block_type_code(self):
        """Test code block"""
        block = "```This is code block```"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_CODE)

    def test_block_to_block_type_quote(self):
        """Test quote block"""
        block = (
            "> This is a quote\n> where the quote continues\n> across multiple lines"
        )
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_QUOTE)

    def test_block_to_block_type_unordered_list(self):
        """Test unordered list block with * symbol"""
        block = "* This is a list item\n* This is a second list item\n* This is a third list item"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_UNORDERED_LIST)

    def test_block_to_block_type_unordered_list2(self):
        """Test unordered list block with - symbol"""
        block = "- This is a list item\n- This is a second list item\n- This is a third list item"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        """Test ordered list block"""
        block = "1. This is a list item\n2. This is a second list item\n3. This is a third list item"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        """Test paragraph block"""
        block = "This is a normal paragraph"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_PARAGRAPH)

    def test_heading_block_to_html_h1(self):
        """Test html h1"""
        block = "# This is an H1"
        self.assertEqual(
            heading_block_to_html(block, BLOCK_TYPE_HEADING).to_html(),
            LeafNode("h1", "This is an H1").to_html(),
        )

    def test_heading_block_to_html_h4(self):
        """Test html h4"""
        block = "#### This is an H4"
        self.assertEqual(
            heading_block_to_html(block, BLOCK_TYPE_HEADING).to_html(),
            LeafNode("h4", "This is an H4").to_html(),
        )

    def test_heading_block_to_html_h6(self):
        """Test html h6"""
        block = "###### This is an H6"
        self.assertEqual(
            heading_block_to_html(block, BLOCK_TYPE_HEADING).to_html(),
            LeafNode("h6", "This is an H6").to_html(),
        )

    def test_quote_block_to_html(self):
        """Test markdown to html quote"""
        block = ">This is a quote\n>This is another quote\n>This is a third quote"
        self.assertEqual(
            quote_block_to_html(block, BLOCK_TYPE_QUOTE).to_html(),
            LeafNode(
                "blockquote",
                "This is a quote\nThis is another quote\nThis is a third quote",
            ).to_html(),
        )

    def test_code_block_to_html(self):
        """Test markdown to html code"""
        block = "```This is a code block/nThis is another line in the code block```"
        self.assertEqual(
            code_block_to_html(block, BLOCK_TYPE_CODE).to_html(),
            ParentNode(
                "pre",
                [
                    LeafNode(
                        "code",
                        "This is a code block/nThis is another line in the code block",
                    )
                ],
            ).to_html(),
        )

    def test_unordered_list_block_to_html_asterisk(self):
        """Test markdown to html unordered list with asterisk marker"""
        block = "* This is the first list item\n* This is the second list item\n* This is the third list item"
        self.assertEqual(
            unordered_list_block_to_html(block, BLOCK_TYPE_UNORDERED_LIST).to_html(),
            ParentNode(
                "ul",
                [
                    LeafNode("li", "This is the first list item"),
                    LeafNode("li", "This is the second list item"),
                    LeafNode("li", "This is the third list item"),
                ],
            ).to_html(),
        )

    def test_unordered_list_block_to_html_dash(self):
        """Test markdown to html unordered list with dash marker"""
        block = "- This is the first list item\n- This is the second list item\n- This is the third list item"
        self.assertEqual(
            unordered_list_block_to_html(block, BLOCK_TYPE_UNORDERED_LIST).to_html(),
            ParentNode(
                "ul",
                [
                    LeafNode("li", "This is the first list item"),
                    LeafNode("li", "This is the second list item"),
                    LeafNode("li", "This is the third list item"),
                ],
            ).to_html(),
        )

    def test_ordered_list_block_to_html(self):
        """Test markdown to html ordered list"""
        block = "1. This is the first list item\n2. This is the second list item\n3. This is the third list item"
        self.assertEqual(
            ordered_list_block_to_html(block, BLOCK_TYPE_ORDERED_LIST).to_html(),
            ParentNode(
                "ul",
                [
                    LeafNode("li", "This is the first list item"),
                    LeafNode("li", "This is the second list item"),
                    LeafNode("li", "This is the third list item"),
                ],
            ).to_html(),
        )

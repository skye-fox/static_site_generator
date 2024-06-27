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
    markdown_to_blocks,
)


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

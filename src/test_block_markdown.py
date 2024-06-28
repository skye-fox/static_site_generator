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
    markdown_to_html,
    ordered_list_block_to_html,
    paragraph_block_to_html,
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
        block = "> This is a quote\n> This is another quote\n> This is a third quote"
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
                "ol",
                [
                    LeafNode("li", "This is the first list item"),
                    LeafNode("li", "This is the second list item"),
                    LeafNode("li", "This is the third list item"),
                ],
            ).to_html(),
        )

    def test_paragraph_block_to_html(self):
        """Test markdown to html paragraph"""
        block = "This is the first line in a paragraph\nThis is the seond line in a paragraph"
        self.assertEqual(
            paragraph_block_to_html(block, BLOCK_TYPE_PARAGRAPH).to_html(),
            LeafNode(
                "p",
                "This is the first line in a paragraph\nThis is the seond line in a paragraph",
            ).to_html(),
        )

    def test_markdown_to_html(self):
        """Test function markdown_to_html"""
        self.assertEqual(
            markdown_to_html(MARKDOWN).to_html(),
            ParentNode(
                "div",
                [
                    ParentNode(
                        "h1",
                        [
                            LeafNode(None, "This is a ", None),
                            LeafNode("bold", "bold", None),
                            LeafNode(None, " H1 heading", None),
                        ],
                        None,
                    ),
                    ParentNode(
                        "p",
                        [
                            LeafNode(None, "This is a ", None),
                            LeafNode("bold", "bolded", None),
                            LeafNode(None, " paragraph", None),
                        ],
                        None,
                    ),
                    ParentNode(
                        "h2", [LeafNode(None, "This is an H2 heading", None)], None
                    ),
                    ParentNode(
                        "p",
                        [
                            LeafNode(None, "This is another paragraph with ", None),
                            LeafNode("italic", "italic", None),
                            LeafNode(None, " text and ", None),
                            LeafNode("code", "code", None),
                            LeafNode(
                                None,
                                " here\nThis is the same paragraph on a new line",
                                None,
                            ),
                        ],
                        None,
                    ),
                    ParentNode(
                        "h3", [LeafNode(None, "This is an H3 heading", None)], None
                    ),
                    ParentNode(
                        "ul",
                        [
                            ParentNode(
                                "li", [LeafNode(None, "This is item 1", None)], None
                            ),
                            ParentNode(
                                "li",
                                [
                                    LeafNode(None, "This is ", None),
                                    LeafNode(
                                        "a", "item 2", {"href": "https://www.boot.dev"}
                                    ),
                                ],
                                None,
                            ),
                            ParentNode(
                                "li", [LeafNode(None, "This is item 3", None)], None
                            ),
                        ],
                        None,
                    ),
                    ParentNode(
                        "h4", [LeafNode(None, "This is an H4 heading", None)], None
                    ),
                    ParentNode(
                        "blockquote",
                        [
                            LeafNode(
                                None,
                                "This is a very inspiring quote\nIt was written by a very inspiring bear\n-- Boots",
                                None,
                            )
                        ],
                        None,
                    ),
                    ParentNode(
                        "h5", [LeafNode(None, "This is an H5 heading", None)], None
                    ),
                    ParentNode(
                        "pre",
                        [
                            ParentNode(
                                "code",
                                [LeafNode(None, 'print("Hello World")', None)],
                                None,
                            )
                        ],
                        None,
                    ),
                    ParentNode(
                        "h6", [LeafNode(None, "This is an H6 heading", None)], None
                    ),
                    ParentNode(
                        "ol",
                        [
                            LeafNode(
                                "li",
                                "This is the first item in an ordered list",
                                None,
                            ),
                            LeafNode(
                                "li",
                                "This is the second item in an ordered list",
                                None,
                            ),
                            LeafNode(
                                "li",
                                "This is the third item in an ordered list",
                                None,
                            ),
                        ],
                        None,
                    ),
                ],
                None,
            ).to_html(),
        )


MARKDOWN = """# This is a **bold** H1 heading

This is a **bolded** paragraph

## This is an H2 heading

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

### This is an H3 heading

* This is item 1
* This is [item 2](https://www.boot.dev)
* This is item 3

#### This is an H4 heading

> This is a very inspiring quote
> It was written by a very inspiring bear
> -- Boots

##### This is an H5 heading

```print("Hello World")```

###### This is an H6 heading

1. This is the first item in an ordered list
2. This is the second item in an ordered list
3. This is the third item in an ordered list"""

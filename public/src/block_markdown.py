"""This module is for processing a document into individual markdown blocks"""

# pylint: disable=line-too-long

import re

from htmlnode import LeafNode

BLOCK_TYPE_PARAGRAPH = "paragraph"
BLOCK_TYPE_HEADING = "heading"
BLOCK_TYPE_CODE = "code"
BLOCK_TYPE_QUOTE = "quote"
BLOCK_TYPE_UNORDERED_LIST = "unordered_list"
BLOCK_TYPE_ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    """Function for splitting a markdown document into individual blocks"""
    get_blocks = re.split("\n\\s+", markdown)
    blocks = []
    for block in get_blocks:
        blocks.append(block.strip())
    return blocks


def block_to_block_type(block):
    """Function that takes a markdown block and returns it's block type"""

    heading_opts = {"#", "##", "###", "####", "#####", "######"}
    heading = block.split()
    lines = block.splitlines()
    if heading[0] in heading_opts:
        return BLOCK_TYPE_HEADING
    if block.startswith("```"):
        if not block.endswith("```"):
            raise SyntaxError("Invalid Markdown: Code block must end with ```")
        return BLOCK_TYPE_CODE
    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                raise SyntaxError(
                    "Invalid Markdown: Every line in a quote block must begin with > followed by a space"
                )
        return BLOCK_TYPE_QUOTE
    if block.startswith("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") and not line.startswith("- "):
                raise SyntaxError(
                    "Invalid Markdown: Every line in an unordered list list must start with * or -"
                )
        return BLOCK_TYPE_UNORDERED_LIST
    if block.startswith("1. "):
        for i, line in enumerate(lines, 1):
            if not line.startswith(f"{i}. "):
                raise SyntaxError(
                    "Invalid Markdown: Every line in an ordered list must start with a number followed by a . and a space, additionally each line must increment the number by one"
                )
        return BLOCK_TYPE_ORDERED_LIST
    return BLOCK_TYPE_PARAGRAPH


def heading_block_to_html(block, block_type):
    """Function to convert a heading block to html"""

    split = block.split(" ", 1)
    heading = split[0]
    content = split[1]
    if block_type != BLOCK_TYPE_HEADING:
        raise TypeError("This function only accepts BLOCK_TYPE_HEADING")
    if len(heading) == 1:
        return LeafNode("h1", content)
    if len(heading) == 2:
        return LeafNode("h2", content)
    if len(heading) == 3:
        return LeafNode("h3", content)
    if len(heading) == 4:
        return LeafNode("h4", content)
    if len(heading) == 5:
        return LeafNode("h5", content)
    if len(heading) == 6:
        return LeafNode("h6", content)
    raise ValueError(
        "Heading must conform to one of: '# ', '## ', '### ', '#### ', '##### ', '###### '"
    )

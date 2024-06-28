"""This module is for processing a document into individual markdown blocks"""

# pylint: disable=line-too-long

import re

from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

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


def text_to_children(text):
    """function that takes markdown text and returns a list of htmlnodes"""
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children


def heading_block_to_html(block, block_type):
    """Function to convert a heading block to html"""

    split = block.split(" ", 1)
    heading = split[0]
    children = text_to_children(split[1])
    if block_type != BLOCK_TYPE_HEADING:
        raise TypeError("This function only accepts BLOCK_TYPE_HEADING")
    if len(heading) == 1:
        return ParentNode("h1", children)
    if len(heading) == 2:
        return ParentNode("h2", children)
    if len(heading) == 3:
        return ParentNode("h3", children)
    if len(heading) == 4:
        return ParentNode("h4", children)
    if len(heading) == 5:
        return ParentNode("h5", children)
    if len(heading) == 6:
        return ParentNode("h6", children)
    raise SyntaxError(
        "Heading must conform to one of: '# ', '## ', '### ', '#### ', '##### ', '###### '"
    )


def code_block_to_html(block, block_type):
    """Function that takes a markdown code block & returns an html code block"""
    if block_type != BLOCK_TYPE_CODE:
        raise TypeError("This function only accepts BLOCK_TYPE_CODE")
    block = block.strip("```")
    children = text_to_children(block)
    return ParentNode("pre", [ParentNode("code", children)])


def quote_block_to_html(block, block_type):
    """Function that takes a markdown quote block and returns an html quote block"""
    if block_type != BLOCK_TYPE_QUOTE:
        raise TypeError("This function only accepts BLOCK_TYPE_QUOTE")
    old_lines = block.splitlines()
    lines = []
    for line in old_lines:
        lines.append(line.strip("> "))
    new_block = "\n".join(lines)
    children = text_to_children(new_block)
    return ParentNode("blockquote", children)


def unordered_list_block_to_html(block, block_type):
    """Function that takes a markdown unordered list block and returns an html unordered list block"""
    if block_type != BLOCK_TYPE_UNORDERED_LIST:
        raise TypeError("This function only accepts BLOCK_TYPE_UNORDERED_LIST")
    old_lines = block.splitlines()
    children = []
    if block.startswith("* "):
        for line in old_lines:
            inner_children = text_to_children(line.strip("* "))
            children.append(ParentNode("li", inner_children))
    if block.startswith("- "):
        for line in old_lines:
            inner_children = text_to_children(line.strip("- "))
            children.append(ParentNode("li", inner_children))
    return ParentNode("ul", children)


def ordered_list_block_to_html(block, block_type):
    """Function that takes a markdown ordered list block and returns an html ordered list block"""
    if block_type != BLOCK_TYPE_ORDERED_LIST:
        raise TypeError("This function only accepts BLOCK_TYPE_ORDERED_LIST")
    old_lines = block.splitlines()
    children = []
    for i, line in enumerate(old_lines, 1):
        inner_children = text_to_children(line.strip(f"{i}. "))
        children.append(ParentNode("li", inner_children))
    return ParentNode("ol", children)


def paragraph_block_to_html(block, block_type):
    """Function that takes a markdown paragraph block and returns an html paragraph block"""
    if block_type != BLOCK_TYPE_PARAGRAPH:
        raise TypeError("This function only accepts BLOCK_TYPE_PARAGRAPH")
    children = text_to_children(block)
    return ParentNode("p", children)


def markdown_to_html(markdown):
    """Function that takes a markdown document and returns an html document"""
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BLOCK_TYPE_HEADING:
            children.append(heading_block_to_html(block, block_type))
        if block_type == BLOCK_TYPE_CODE:
            children.append(code_block_to_html(block, block_type))
        if block_type == BLOCK_TYPE_QUOTE:
            children.append(quote_block_to_html(block, block_type))
        if block_type == BLOCK_TYPE_UNORDERED_LIST:
            children.append(unordered_list_block_to_html(block, block_type))
        if block_type == BLOCK_TYPE_ORDERED_LIST:
            children.append(ordered_list_block_to_html(block, block_type))
        if block_type == BLOCK_TYPE_PARAGRAPH:
            children.append(paragraph_block_to_html(block, block_type))
    return ParentNode("div", children)

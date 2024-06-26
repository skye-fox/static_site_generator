"""This Module is for processing inline markdown"""

import re

from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Function that takes a list of TextNodes, a delimiter, and a text type
    and splits the node into multiple smaller nodes if necessary"""

    new_nodes = []
    for node in old_nodes:
        if node.text.count(delimiter) % 2 != 0:
            raise SyntaxError("Invalid Markdown syntax")
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            split_node = node.text.split(delimiter)
            for string in split_node:
                if string.startswith(" ") or string.endswith(" "):
                    new_nodes.append(TextNode(string, "text"))
                else:
                    if string != "":
                        new_nodes.append(TextNode(string, text_type))
    return new_nodes


def extract_markdown_images(text):
    """Function to extract images from text, returns a tuple containing (alt text, url)"""
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images


def extract_markdown_links(text):
    """Function to extract links from text, returns a tuple containing (anchor text, url)"""
    links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links


def split_nodes_image(old_nodes):
    """Function to split markdown text with images into a list of TextNodes"""
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            original_text = node.text
            images = extract_markdown_images(original_text)
            for image in images:
                split_node = original_text.split(f"![{image[0]}]({image[1]})", 1)
                if split_node[0] != "":
                    new_nodes.append(TextNode(split_node[0], "text"))
                new_nodes.append(TextNode(image[0], "image", image[1]))
                original_text = split_node[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, "text"))
    return new_nodes


def split_nodes_link(old_nodes):
    """Function to split markdown text with links into a list of TextNodes"""
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            original_text = node.text
            links = extract_markdown_links(original_text)
            for link in links:
                split_node = original_text.split(f"[{link[0]}]({link[1]})", 1)
                if split_node[0] != "":
                    new_nodes.append(TextNode(split_node[0], "text"))
                new_nodes.append(TextNode(link[0], "link", link[1]))
                original_text = split_node[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, "text"))
    return new_nodes


def text_to_textnodes(text):
    """Function to convert text to TextNodes, takes a string and returns a list of TextNodes"""
    text_nodes = split_nodes_delimiter([TextNode(text, "text")], "`", "code")
    text_nodes = split_nodes_delimiter(text_nodes, "**", "bold")
    text_nodes = split_nodes_delimiter(text_nodes, "*", "italic")
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes

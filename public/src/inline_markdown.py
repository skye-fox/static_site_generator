"""This Module is for processing inline markdown"""

import re

from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Function that takes a list of TextNodes, a delimiter, and a text type
    and splits the node into multiple smaller nodes if necessary"""

    new_nodes = []
    counter = 0
    words = []
    for node in old_nodes:
        if len(words) > 0:
            new_nodes.append(TextNode(" ".join(words), "text"))
        if node.text_type != "text":
            new_nodes.append(node)
        split_node = node.text.split()
        words = []
        for word in split_node:
            if word.count(delimiter) == 0:
                words.append(word)
            if word.count(delimiter) == 1:
                counter += 1
                if counter == 2:
                    words.append(word.strip(delimiter))
                    new_nodes.append(TextNode(" ".join(words), text_type))
                    words = []
                    counter = 0
                if len(words) > 0:
                    new_nodes.append(TextNode(" ".join(words), "text"))
                    words = []
                    words.append(word.strip(delimiter))
            if word.count(delimiter) == 2:
                if len(words) > 0:
                    new_nodes.append(TextNode(" ".join(words), "text"))
                    words = []
                new_nodes.append(TextNode(word.strip(delimiter), text_type))
    if len(words) > 0:
        new_nodes.append(TextNode(" ".join(words), "text"))
    if counter == 1:
        raise SyntaxError("Invalid Markdown syntax")
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

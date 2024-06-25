"""This Module is for processing inline markdown"""

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

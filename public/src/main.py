from htmlnode import HTMLNode
from textnode import TextNode


def main():
    new_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    new_node2 = HTMLNode("<h1>", "Hello World")
    print(new_node)
    print(new_node2)


main()

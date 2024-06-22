import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node3 = TextNode("This is a text node", "bold")
        node4 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node3, node4)

    def test_not_eq2(self):
        node3 = TextNode("This is  text node", "bold")
        node4 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node3, node4)

    def test_not_eq3(self):
        node3 = TextNode("This is a text node", "italic")
        node4 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node3, node4)


if __name__ == "__main__":
    unittest.main()

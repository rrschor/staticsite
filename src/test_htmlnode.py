import unittest 
from htmlnode import HTMLNode

class TestHTML(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a text node", "bold")
        node2 = HTMLNode("div", "This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("div", "This is a text node", "bold")
        self.assertEqual(str(node), "div")
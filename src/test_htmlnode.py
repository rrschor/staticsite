import unittest 
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTML(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a text node", "bold")
        node2 = HTMLNode("div", "This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("div", "This is a text node", "bold", [])
        self.assertEqual(node.__repr__(),"tag = div, value = This is a text node, props = bold, children = []")
    
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),  'href="https://www.google.com" target="_blank"')

    def test_leaf_node(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node1.to_html(), '<p>This is a paragraph of text.</p>')
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_parent_node(self):
        node = ParentNode(tag = "p", children= [
                                LeafNode("b", "Bold text"), 
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                                ],
                                )

        self.assertEqual(node.to_html(),'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

if __name__ == "__main__":
    unittest.main()
import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        node = HTMLNode("a","Anchor",props={"href": "https://www.google.com","target":"_blank"})
        node1 = HTMLNode("a","DuplicateAnchor",props={"href": "https://www.google.com","target":"_blank"})
        self.assertEqual(node.props_to_html(),node1.props_to_html())

    def test_eq2(self):
        node = HTMLNode("a","Anchor",props={"href": "https://www.google.com","target":"_blank"})
        node1 = HTMLNode("a","DuplicateAnchor",props={"href": "https://www.google.com","target":"_blank"})
        self.assertNotEqual(node.value,node1.value)

    def test_eq3(self):
        node = HTMLNode("a",children="child",props={"href": "https://www.google.com","target":"_blank"})
        node1 = HTMLNode("a","Anchor",props={"href": "https://www.google.com","target":"_blank"})
        self.assertNotEqual(node.value,node1.value)

    def test_eq4(self):
        node = HTMLNode("a",children="child",props={"href": "https://www.google.com","target":"_blank"})
        node1 = HTMLNode("a",children="child",props={"href": "https://www.google.com","target":"_blank"})
        self.assertEqual(node.props_to_html(),node1.props_to_html())
        self.assertEqual(node.value,node1.value)
        self.assertEqual(node.tag,node1.tag)
        self.assertEqual(node.children,node1.children)

if __name__ == "__main__":
    unittest.main()
import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node1 = LeafNode("a","Deez",props={"href": "https://www.google.com","target":"_blank"})
        self.assertEqual(node1.to_html(),"<a href='https://www.google.com' target='_blank' >Deez</a>")

    def test_eq5(self):
        node = LeafNode(None,value="Hello, world!")
        self.assertEqual(node.to_html(),"Hello, world!")

    def test_eq6(self):
        node = LeafNode("p",None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception),"All leaf nodes must have a value")

    def test_eq7(self):
        child_node1 = LeafNode(None,"PlainText")
        child_node2 = LeafNode("a","GoogleLink",{"href": "https://www.google.com","target":"_blank"})
        parent_node = ParentNode("p",[child_node1,child_node2])
        self.assertEqual(parent_node.to_html(),"<p>PlainText<a href='https://www.google.com' target='_blank' >GoogleLink</a></p>")


    def test_eq8(self):
        child_node2 = LeafNode("a","GoogleLink",{"href": "https://www.google.com","target":"_blank"})
        child_node1 = ParentNode("p",[child_node2])
        parent_node = ParentNode("p",[child_node1])
        self.assertEqual(parent_node.to_html(),"<p><p><a href='https://www.google.com' target='_blank' >GoogleLink</a></p></p>")


    def test_eq9(self):
        child_node1 = HTMLNode()
        parent_node = ParentNode("p",[child_node1])

        with self.assertRaises(TypeError) as context:
            parent_node.to_html()

        self.assertEqual(str(context.exception),"Parent Node can only contain LeafNode children")


    def test_eq10(self):
        child_node1 = LeafNode(None,"PlainText")
        child_node2 = LeafNode(None,"AnotherPlainText")

        parent_node1 = ParentNode(None,children=[child_node1,child_node2])
        parent_node2 = ParentNode("p",None)

        with self.assertRaises(ValueError) as context:
            parent_node1.to_html()

        with self.assertRaises(ValueError) as nochildcontext:
            parent_node2.to_html()

        self.assertEqual(str(context.exception),"All parent nodes must have a tag")
        self.assertEqual(str(nochildcontext.exception),"All parent nodes must have Children")
        

if __name__ == "__main__":
    unittest.main()
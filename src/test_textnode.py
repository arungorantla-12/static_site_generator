import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode,ParentNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD,"www.bold.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"www.bold.com")
        self.assertEqual(node,node2)

    def test_eq4(self):
        node = TextNode("This is a text node", TextType.BOLD,"www.bold.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"www.boold.com")
        self.assertNotEqual(node,node2)

    def test_eq5(self):
        node = TextNode("This is a text node", TextType.BOLD,"www.bold.com")
        node2 = TextNode("This is a text node", TextType.IMAGE,"www.bold.com")
        self.assertNotEqual(node,node2)

    def test_eq6(self):
        node = TextNode("This is is", TextType.BOLD,"www.bold.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"www.bold.com")
        self.assertNotEqual(node,node2)

    def test_eq7(self):
        node = TextNode("This is a Plain Text","TEXT")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.value,"This is a Plain Text")

    def test_eq8(self):
        node = TextNode("This is a Plain Text","LINK",'www.google.com')
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.props,{'url': 'www.google.com'})
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.value,"This is a Plain Text")

    def test_eq9(self):
        node = TextNode("This is a Plain Text","IMAGE",'www.google.com')
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.props,{'src':'www.google.com','alt':'This is a Plain Text'})
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.value,"")

    def test_eq10(self):
        node = TextNode("This is a Plain Text","TEXTIE")
        with self.assertRaises(ValueError) as context:
            node.text_node_to_html_node()
        self.assertEqual(str(context.exception),"The type is not the type of Text Node accepted")



    


    
if __name__ == "__main__":
    unittest.main()
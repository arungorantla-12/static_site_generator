from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode

#print(TextNode("This is a image",TextType["IMAGE"],"www.image.com"))

node = HTMLNode("a","Deez",props={"href": "https://www.google.com","target":"_blank"})
print(node)

node1 = LeafNode("a","Deez",props={"href": "https://www.google.com","target":"_blank"})
print(node1)
print(node1.to_html())

node2 = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)

print(node2.to_html())



child_node2 = LeafNode("a","GoogleLink",{"href": "https://www.google.com","target":"_blank"})
child_node1 = ParentNode("p",[child_node2])
parent_node = ParentNode("p",[child_node1])

print(parent_node.to_html())


node = TextNode("This is a Plain Text","LINK",'www.google.com')
html_node = node.text_node_to_html_node()
print(html_node.props)

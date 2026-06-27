from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode

#print(TextNode("This is a image",TextType["IMAGE"],"www.image.com"))

node = HTMLNode("a","Deez",props={"href": "https://www.google.com","target":"_blank"})
print(node)

node1 = LeafNode("a","Deez",props={"href": "https://www.google.com","target":"_blank"})
print(node1)
print(node1.to_html())

from textnode import TextNode,TextType
from htmlnode import HTMLNode

#print(TextNode("This is a image",TextType["IMAGE"],"www.image.com"))

node = HTMLNode("a","Deez",props={"href": "https://www.google.com","target":"_blank"})
print(node)


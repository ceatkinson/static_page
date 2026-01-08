#print("hello world")
from textnode import TextNode, TextType
def main():
    test = TextNode("example text",TextType.PLAIN,"url")
    print(test)

main()
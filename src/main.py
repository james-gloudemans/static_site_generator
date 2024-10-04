from textnode import TextNode
from htmlnode import HTMLNode

def main():
    node = HTMLNode('tag', 'value', ['child1', 'child2'], {'prop1':'val1', 'prop2':'val2'})
    print(node)

if __name__ == '__main__':
    main()
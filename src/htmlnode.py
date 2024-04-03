class HTMLNode:
    """
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def __str__(self):
        return self.tag

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self) -> str:
        return f"tag = {self.tag}, value = {self.value}, props = {self.props}, children = {self.children}"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        """"
        This method should return a string that represents the HTML attributes of the node. 
        """
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props=None):
        if not tag:
            raise ValueError("tag is required for LeafNode")
        super().__init__(value, tag, props)

    def to_html(self):
        if "href" in self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, children, tag, props=None):
        if not children or not isinstance(children, list):
            raise ValueError("children is required for ParentNode")
        if not tag:
            raise ValueError("tag is required for ParentNode")
        super().__init__(tag=tag, props=props, children = children)

    def to_html(self):
        """"
        This method is a recursive method that uses the recursive method. 
        It iterated over all the children and called to_html on each, 
        concatenating the results and injecting them between the opening 
        and closing tags of the parent.
        """
        if "href" in self.props:
            return f"<{self.tag} {self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            val = ""
            for prop in self.props:
                val = val + f' {prop}="{self.props[prop]}"'
            return val

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
    def __eq__(self, other):
        if (self.tag == other.tag and self.value == other.value and self.props == other.props ):
            if (self.children is None or other.children is None) and self.children != other.children:
                return False
            if self.children is not None and other.children is not None and len(self.children) != len(other.children):  
                return False
            if self.children is not None and other.children is not None: 
                for i in range(len(self.children)):  # type: ignore
                    if self.children[i] != other.children[i]:
                        return False
        else:
            return False
        return True
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props = props)
    
    def to_html(self):
        if self.value is None: 
            raise ValueError
        if self.tag is None:
            return self.value  
        else: 
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, children = children, props = props)

    def to_html(self):
        if self.tag is None: 
            raise ValueError
        if self.children is None:
            return ValueError("parent must have children")  
        else: 
            val =  f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                val = val + child.to_html()
            val = val + f"</{self.tag}>"
            return val 
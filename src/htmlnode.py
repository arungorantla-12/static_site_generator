class HTMLNode():
    def __init__(self,tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        final_str = " "
        if self.props is not None and self.props:
            for pro in self.props:
                final_str+= f"{pro}='{self.props[pro]}' "
        return final_str
    

    def __repr__(self):
        return f"HTMLNode{self.tag,self.value,self.children,self.props_to_html()}"
    




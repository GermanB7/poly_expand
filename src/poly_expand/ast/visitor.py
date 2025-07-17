from poly_expand.ast.nodes import Node

class NodeVisitor:
    """
    Patrón visitor: para cada tipo de nodo busca un método visit_<ClassName>.
    Si no existe, lanza excepción.
    """

    def visit(self, node: Node):
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, None)
        if visitor is None:
            raise NotImplementedError(f"No visit method for {type(node).__name__}")
        return visitor(node)

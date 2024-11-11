import math
import ast
import operator as op
import string


class MathParser:
    """Basic math expression parser with local variables and math functions.

    Args:
        vars (dict): Dictionary mapping variable names to their numerical values.
        math (bool, optional): If True (default), include all math functions
            from the `math` module in the parser's namespace.

    Raises:
        Exception: If the expression contains invalid characters.
        NameError: If a variable or function is not found.
    """

    _operators2method = {
        ast.Add: op.add,
        ast.Sub: op.sub,
        ast.BitXor: op.xor,
        ast.Or: op.or_,
        ast.And: op.and_,
        ast.Mod: op.mod,
        ast.Mult: op.mul,
        ast.Div: op.truediv,
        ast.Pow: op.pow,
        ast.FloorDiv: op.floordiv,
        ast.USub: op.neg,
        ast.UAdd: lambda a: a,  # Identity function for unary plus
    }

    _allowed_chars = string.ascii_letters + string.digits + ' .+-*/()'

    def __init__(self, expr, vars={}, math=True):
        """
        Initializes the parser with the expression and optional variables/functions.

        Args:
            expr (str): The mathematical expression to parse.
            vars (dict, optional): Dictionary of variables and their values. Defaults to {}.
            math (bool, optional): Whether to include math functions. Defaults to True.
        """

        self._vars = vars
        self._math = math

        for c in expr:
            if c not in self._allowed_chars:
                raise Exception(f"Invalid character in expression: '{c}'")

        self._expr = ast.parse(expr, mode='eval')

        if not math:
            self._alt_name = self._no_alt_name

    def _Name(self, name):
        """
        Looks up the value of a variable or function.

        Args:
            name (str): The name of the variable or function.

        Returns:
            float: The value associated with the name.

        Raises:
            NameError: If the name is not found in variables or math functions.
        """

        try:
            return self._vars[name]
        except KeyError:
            if self._math:
                try:
                    return getattr(math, name)
                except AttributeError:
                    pass
            raise NameError(f"Variable or function not found: '{name}'")

    @staticmethod
    def _no_alt_name(name):
        """
        Raises an error if math functions are disabled and a variable is not found.
        """

        if name.startswith('_'):
            raise NameError(f"Invalid variable name: '{name}'")
        raise NameError(f"Variable not found: '{name}'")

    def eval_(self, node):
        """
        Recursively evaluates the AST node based on its type.

        Args:
            node (ast.AST): The AST node to evaluate.

        Returns:
            float: The calculated result.

        Raises:
            TypeError: If the node type is not supported.
        """

        if isinstance(node, ast.Expression):
            return self.eval_(node.body)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Name):
            return self._Name(node.id)
        elif isinstance(node, ast.BinOp):
            method = self._operators2method[type(node.op)]
            return method(self.eval_(node.left), self.eval_(node.right))
        elif isinstance(node, ast.UnaryOp):
            method = self._operators2method[type(node.op)]
            return method(self.eval_(node.operand))
        elif isinstance(node, ast.Attribute):
            return getattr(self.eval_(node.value), node.attr)
        elif isinstance(node, ast.Call):
            func = self.eval_(node.func)import math
import ast
import operator as op
import string


class MathParser:
    """Basic math expression parser with local variables and math functions.

    Args:
        vars (dict): Dictionary mapping variable names to their numerical values.
        math (bool, optional): If True (default), include all math functions
            from the `math` module in the parser's namespace.

    Raises:
        Exception: If the expression contains invalid characters.
        NameError: If a variable or function is not found.
    """

    _operators2method = {
        ast.Add: op.add,
        ast.Sub: op.sub,
        ast.BitXor: op.xor,
        ast.Or: op.or_,
        ast.And: op.and_,
        ast.Mod: op.mod,
        ast.Mult: op.mul,
        ast.Div: op.truediv,
        ast.Pow: op.pow,
        ast.FloorDiv: op.floordiv,
        ast.USub: op.neg,
        ast.UAdd: lambda a: a,  # Identity function for unary plus
    }

    _allowed_chars = string.ascii_letters + string.digits + ' .+-*/()'

    def __init__(self, expr, vars={}, math=True):
        """
        Initializes the parser with the expression and optional variables/functions.

        Args:
            expr (str): The mathematical expression to parse.
            vars (dict, optional): Dictionary of variables and their values. Defaults to {}.
            math (bool, optional): Whether to include math functions. Defaults to True.
        """

        self._vars = vars
        self._math = math

        for c in expr:
            if c not in self._allowed_chars:
                raise Exception(f"Invalid character in expression: '{c}'")

        self._expr = ast.parse(expr, mode='eval')

        if not math:
            self._alt_name = self._no_alt_name

    def _Name(self, name):
        """
        Looks up the value of a variable or function.

        Args:
            name (str): The name of the variable or function.

        Returns:
            float: The value associated with the name.

        Raises:
            NameError: If the name is not found in variables or math functions.
        """

        try:
            return self._vars[name]
        except KeyError:
            if self._math:
                try:
                    return getattr(math, name)
                except AttributeError:
                    pass
            raise NameError(f"Variable or function not found: '{name}'")

    @staticmethod
    def _no_alt_name(name):
        """
        Raises an error if math functions are disabled and a variable is not found.
        """

        if name.startswith('_'):
            raise NameError(f"Invalid variable name: '{name}'")
        raise NameError(f"Variable not found: '{name}'")

    def eval_(self, node):
        """
        Recursively evaluates the AST node based on its type.

        Args:
            node (ast.AST): The AST node to evaluate.

        Returns:
            float: The calculated result.

        Raises:
            TypeError: If the node type is not supported.
        """

        if isinstance(node, ast.Expression):
            return self.eval_(node.body)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Name):
            return self._Name(node.id)
        elif isinstance(node, ast.BinOp):
            method = self._operators2method[type(node.op)]
            return method(self.eval_(node.left), self.eval_(node.right))
        elif isinstance(node, ast.UnaryOp):
            method = self._operators2method[type(node.op)]
            return method(self.eval_(node.operand))
        elif isinstance(node, ast.Attribute):
            return getattr(self.eval_(node.value), node.attr)
        elif isinstance(node, ast.Call):
            # Cutoff from Gemeni response
            func = self.eval_(node.func)( 
                      *(self.eval_(a) for a in node.args),
                      **{k.arg:self.eval_(k.value) for k in node.keywords}
                     )           
            return self.Call( self.eval_(node.func), tuple(self.eval_(a) for a in node.args))
        else:
            raise TypeError(node)
    
    def eval(self, **kwargs):
        self._vars = kwargs
        return  self.eval_(self._expr)
    

f = MathParser("t*32/88 + 220")
print(f.eval(t=10))
print(f.eval(t=88))
print(MathParser("881").eval(t=44))

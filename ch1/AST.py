import ast
code = "y = (4 * 5) - 3"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))

import turtle


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def parse_tree(tree):
    value = list(tree[0])[1] if list(tree[0])[1].isnumeric() else list(tree[0])[0]
    left, right = tree[1], tree[2]
    return Node(int(value), parse_tree(left) if left else None, parse_tree(right) if right else None)


def draw_tree(node, x, y, dx, dy):
    if node is not None:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write(node.value, align="center", font=("Arial", 12, "bold"))

        if node.left is not None:
            turtle.penup()
            turtle.goto(x, y - dy)
            turtle.pendown()
            turtle.goto(x - dx, y - dy - 50)
        draw_tree(node.left, x - dx, y - dy - 50, dx, dy)

        if node.right is not None:
            turtle.penup()
            turtle.goto(x, y - dy)
            turtle.pendown()
            turtle.goto(x + dx, y - dy - 50)
        draw_tree(node.right, x + dx, y - dy - 50, dx, dy)


turtle.setworldcoordinates(-1000, -1000, 1000, 100)
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# create a sample tree
null = None


tree = [{"16","a"},[{"5","a"},[{"4","a"},null,null],[{"15","a"},[{"10","a"},null,null],null]],[{"30","a"},null,[{"40","a"},null,[{"50","a"},[{"45","a"},null,[{"47","a"},null,null]],[{"60","a"},null,null]]]]]

root = parse_tree(tree)
draw_tree(root, 0, 0, 50, 20)
turtle.done()

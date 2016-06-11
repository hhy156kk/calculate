
class Buffer(object):
    def __init__(self,data):
        self.data = data
        self.offset = 0

    def peek(self):
        if self.offset >= len(self.data):
            return None
        return self.data[self.offset]

    def advance(self):
        self.offset = self.offset+1

class Token(object):
    def consume(self,buffer):
        pass

class IntToken(Token):
    def consume(self,buffer):
        accum = ""
        while True:
            ch = buffer.peek()
            if ch is None or ch not in "1234567890":
                break
            else:
                accum+=ch
                buffer.advance()

        if accum!="":
            return ("int",int(accum))
        else:
            return None

class OperatorToken(Token):
    def consume(self,buffer):
        ch = buffer.peek()
        if ch is not None and ch in "+-":
            buffer.advance()
            return ("ope",ch)
        return  None

class Node(object):
    pass


class IntNode(Node):
    def __init__(self,value):
        self.value = value

class BinaryOpNode(Node):
    def __init__(self,kind):
        self.kind = kind
        self.left = None
        self.right = None

def tokenize(string):
    buffer = Buffer(string)
    tk_int = IntToken()
    tk_op = OperatorToken()
    tokens = []

    while buffer.peek():
        token = None
        for tk in (tk_int,tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break

    return tokens

def parse(tokens):

    node = IntNode(tokens[0][1])
    nbo = None

    for token in tokens[1:]:

        if token[0] == 'ope':
            nbo = BinaryOpNode(token[1])
            nbo.left = node

        if token[0] == 'int':
            nbo.right = IntNode(token[1])
            node = nbo

    return node


def calculate(nbo):

    if isinstance(nbo.left,BinaryOpNode):
        leftVal = calculate(nbo.left)
    else:
        leftVal = nbo.left.value

    if nbo.kind == '-':
        return leftVal - nbo.right.value

    elif nbo.kind == '+':
        return  leftVal + nbo.right.value

    else:
        raise ValueError("Wrong operator")


if __name__ == '__main__':
    input = raw_input("Input:")
    tokens = tokenize(input)
    node = parse(tokens)
    print(calculate(node))


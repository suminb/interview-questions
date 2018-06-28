# NOTE: I don't think I can jot this down on a whiteboard in 40
# minutes, and that leads me to believe that there should be a
# simpler solution.


class Node(object):

    def __init__(self, parent, mode, data):
        self.mode = mode
        self.data = data
        self.parent = parent
        self.children = []


class Token(object):

    def __init__(self, mode, data):
        self.mode = mode
        self.data = data

    def __repr__(self):
        if self.mode == 'text':
            return self.data
        elif self.mode == 'tag_open':
            return '<{0}>'.format(self.data)
        elif self.mode == 'tag_close':
            return '</{0}>'.format(self.data)

    def __eq__(self, other):
        return self.mode == other.mode and self.data == other.data


def reverse(html):
    tokens = tokenize(html)
    root = Node(None, 'text', '')
    build(tokens, root)

    reversed_tokens = []
    traverse(root, reversed_tokens)

    return ''.join([str(t) for t in reversed_tokens])


def traverse(node, tokens):
    if node.mode == 'tag_open':
        tokens.append(Token('tag_open', node.data))
        for child in node.children[::-1]:
            traverse(child, tokens)
        tokens.append(Token('tag_close', node.data))
    elif node.mode == 'text':
        tokens.append(Token(node.mode, node.data[::-1]))
        for child in node.children[::-1]:
            traverse(child, tokens)


def build(tokens, prev_node):
    if tokens:
        token = tokens[0]
        node = Node(prev_node, token.mode, token.data)
        if token.mode == 'text':
            prev_node.children.append(node)
            build(tokens[1:], prev_node)
        elif token.mode == 'tag_open':
            prev_node.children.append(node)
            build(tokens[1:], node)
        elif token.mode == 'tag_close':
            # prev_node.append(node)
            build(tokens[1:], node.parent)


def tokenize(html):
    tokens = []
    text = ''
    tag = ''
    mode = 'text'
    for c1, c2 in zip(html, html[1:] + ' '):
        if c1 == '<':
            if text:
                tokens.append(Token(mode, text))
                text = ''

            if c2 == '/':
                mode = 'tag_close'
            else:
                mode = 'tag_open'
        elif c1 == '/':
            pass
        elif c1 == '>':
            tokens.append(Token(mode, tag))
            tag = ''
            mode = 'text'
        else:
            if mode == 'text':
                text += c1
            elif mode in ['tag_open', 'tag_close']:
                tag += c1

    if mode == 'text' and text:
        tokens.append(Token(mode, text))
    elif mode == 'tag_close' and tag:
        tokens.append(Token(mode, tag))

    return tokens


def test_tokenize():
    data = 'Hello <i>W<b>orld</b></i>'
    expected = [
        Token('text', 'Hello '),
        Token('tag_open', 'i'),
        Token('text', 'W'),
        Token('tag_open', 'b'),
        Token('text', 'orld'),
        Token('tag_close', 'b'),
        Token('tag_close', 'i'),
    ]
    assert tokenize(data) == expected


def test_1():
    data = 'Reverse HTML'
    expected = 'LMTH esreveR'
    assert reverse(data) == expected


def test_2():
    data = 'Hello <i>W<b>orld</b></i>'
    expected = '<i><b>dlro</b>W</i> olleH'
    assert reverse(data) == expected

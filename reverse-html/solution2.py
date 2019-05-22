# This is a second trial. This time, I wrote down the code on a piece of paper,
# trying to make it as completely as possible, and then copied it to a text
# editor. Besides a couple of typing errors and one minor mistake that can be
# easily found and corrected, everything worked as expected. That one minor
# mistake was this:
#
# I passed `tag_buf` when creating `Tag` instance where I was supposed to pass
# `''.join(tag_buf)`.
#
# This is definitely easier than building a tree and traversing it, and I was
# able to finish coding (on paper) in about 15 minutes or so.

# TODO: This violates the file naming convention mentioned in README. Need to
# come up with a suitable name.

class Tag:

    def __init__(self, tag, opening=True):
        self.tag = tag
        self.opening = opening

    def __str__(self):
        if self.opening:
            return f'<{self.tag}>'
        else:
            return f'</{self.tag}>'

    def flip_mode(self):
        self.opening = not self.opening
        return self


def tokenize(html):
    tag_buf = []
    tag_mode = None
    tokens = []

    for c in html:
        if tag_mode:
            if c == '/':
                tag_mode = 'close'
            elif c == '>':
                tokens.append(Tag(''.join(tag_buf), tag_mode == 'open'))
                tag_buf = []
                tag_mode = None
            else:
                tag_buf.append(c)
        elif c == '<':
            tag_mode = 'open'
        else:
            tokens.append(c)

    return tokens


def reverse_tokens(tokens):
    def process(token):
        if isinstance(token, Tag):
            return str(token.flip_mode())
        else:
            return token

    return ''.join([process(t) for t in tokens[::-1]])


def reverse(html):
    return reverse_tokens(tokenize(html))

def test_1():
    data = 'Reverse HTML'
    expected = 'LMTH esreveR'
    assert reverse(data) == expected


def test_2():
    data = 'Hello <i>W<b>orld</b></i>'
    expected = '<i><b>dlro</b>W</i> olleH'
    assert reverse(data) == expected

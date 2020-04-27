class Tag:

    def __init__(self, name, content):
        self.start_tag = '<{}'.format(name)
        self.end_tag = '<{}'.format(name)
        self.content = content

    def __str__(self):
        return "{0.start_tag}{0.content}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML', '')
        self.end_tag = ''


class Head(Tag):

    def __init__(self):
        super().__init__('head', '')


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self._body_content = []

    def add_tag(self, name, content):
        new_tag = Tag(name, content)
        self._body_content.append(new_tag)

    def display(self, file=None):
        for tag in self._body_content:
            self.content += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self):
        self._body = Body()
        self._head = Head()
        self._docType = DocType()

    def add_tag(self, name, content):
        self._body.add_tag(name, content)

    def display(self, file=None):
        self._docType.display(file=file)
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</html>", file=file)


if __name__ == '__main__':
    myPage = HtmlDoc()
    myPage.add_tag('h1', 'Main Heading')
    myPage.add_tag('h2', 'Sub-main Heading')
    myPage.add_tag('p', 'This is the content that is being displayed on the screen.')
    myPage.display()

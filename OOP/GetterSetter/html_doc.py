""" Composition means that an object knows another object, and explicitly delegates some tasks to it.
    While inheritance is implicit, composition is explicit: in Python, however, things are far more interesting
    than this =). The primary goal of composition is to relax the coupling between objects."""


class Tag:

    def __init__(self, name, content):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
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

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.content = str(self._title_tag)


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

    def __init__(self, doc_type, head, body):
        self._body = body
        self._head = head
        self._doc_type = doc_type

    def add_tag(self, name, content):
        self._body.add_tag(name, content)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</html>", file=file)


# if __name__ == '__main__':
#     myPage = HtmlDoc('Demo HTML Document')
#     myPage.add_tag('title', 'Learning Phase')
#     myPage.add_tag('h1', 'Main Heading')
#     myPage.add_tag('h2', 'Sub-main Heading')
#     myPage.add_tag('p', 'This is the content that is being displayed on the screen.')
#     with open('demo.html', 'w') as text_doc:
#         myPage.display(text_doc)
#
# # Here, the content of the head remains same but the content of the body gets changed as I have created new body.
# new_body = Body()
# new_body.add_tag('h1', 'Aggregation')
# new_body.add_tag('p', "<strong>Ek pal</strong> kaa jeena fir to heh jaana"
#                      " - Toofa to leke jaiye kudiyo ko dekhaana.")
# new_body.add_tag('p', "Dil leke darde dil dey gaye, tum jaan jaan khehke mere jaan le gaye.")
#
#
# myPage._body = new_body
# with open("demo2.html", 'w') as text_doc:
#     myPage.display(text_doc)

if __name__ == '__main__':
    # myPage = HtmlDoc('Demo HTML Document')
    # myPage.add_tag('title', 'Learning Phase')
    # myPage.add_tag('h1', 'Main Heading')
    # myPage.add_tag('h2', 'Sub-main Heading')
    # myPage.add_tag('p', 'This is the content that is being displayed on the screen.')
    # with open('demo.html', 'w') as text_doc:
    #     myPage.display(text_doc)

# Here, the content of the head remains same but the content of the body gets changed as I have created new body.
    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "<strong>Ek pal</strong> kaa jeena fir to heh jaana"
                          " - Toofa to leke jaiye kudiyo ko dekhaana.")
    new_body.add_tag('p', "Dil leke darde dil dey gaye, tum jaan jaan khehke mere jaan le gaye.")


    new_docType = DocType()
    new_header = Head('Aggregation Segment')
    myPage = HtmlDoc(new_docType, new_header, new_body)

    with open("demo2.html", 'w') as text_doc:
        myPage.display(text_doc)

"""Aggregation is a week form of composition. If you delete the container object contents objects can live without 
   container object."""
"""Models."""

class Comment(object):
    """docstring for ClassName"""
    def __init__(self, text, date):
        # super(ClassName, self).__init__()
        self.text = text
        self.date = date

    def __repr__(self):
        return "Comment: {}, Date: {}".format(self.text, self.date)

    def table(self):
        """Return users as HTML table."""
        table_str = "<table>"
        table_str += '<tr><th>Comment</th>><th>Date</th></tr>'

        for c in COMMENTS:
            tr = "<tr>"
            tr += "<td>{}</td>".format(c.text)
            tr += "<td>{}</td>".format(c.date)
            tr += "</tr>"
            table_str += tr

        table_str += "</table>"
        return table_str


c1 = Comment('znaci', '2017-05-01')
c2 = Comment('realno', '2016-03-07')
c3 = Comment('zaista', '2014-21-01')

COMMENTS = []
COMMENTS.append(c1)
COMMENTS.append(c2)
COMMENTS.append(c3)

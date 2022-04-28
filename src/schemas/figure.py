from marshmallow import Schema, fields, post_load


class Figure:
    def __init__(self, tight_layout=False, edgecolor='white', facecolor='white'):
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.tight_layout = tight_layout

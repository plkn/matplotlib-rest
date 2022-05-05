from marshmallow import Schema, fields


class Subplot:
    def __init__(self, plot, index=1):
        self.plot = plot
        self.index = index


class SubplotSchema(Schema):
    index = fields.Integer(description="Index of a subplot in a subplots grid", required=True, load_default=1)
    plot = fields.Nested(description="", required=True, load_default="")

from marshmallow import Schema, fields, post_load

from utils.exporter import export


class Line:
    def __init__(self, y, x=None, label=None, fmt=None, linewidth=1):
        self.x = x
        self.y = y
        self.label = label
        self.fmt = fmt
        self.linewidth = linewidth


@export
class LineSchema(Schema):
    x = fields.List(fields.Float, description="", required=False)
    y = fields.List(fields.Float, description="")
    label = fields.String(description="Line label", required=False)
    fmt = fields.String(description="Line format", required=False, load_default="r-")
    linewidth = fields.Float(description="", required=False, load_default=1)

    @post_load
    def load_line(self, data, **kwargs):
        return Line(**data)

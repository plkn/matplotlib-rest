from marshmallow import Schema, fields


class LineSchema(Schema):
    title = fields.String(description="Line title", required=False)
    format = fields.String(description="Line format", required=False)


class PlotSchema(Schema):
    lines = fields.List(fields.Nested(LineSchema))

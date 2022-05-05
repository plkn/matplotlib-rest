from marshmallow import Schema, fields


class Subplot:
    def __init__(self, plot, index=1):
        self.plot = plot
        self.index = index


class SubplotSchema(Schema):
    lie = 1

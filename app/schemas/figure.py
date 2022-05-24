from typing import List

from marshmallow import Schema, fields, post_load

from utils.exporter import export
from .subplot import SubplotSchema, SubplotParams


class FigureParams:
    def __init__(self, subplots: List[SubplotParams], tight_layout=False, edgecolor='white', facecolor='white',
                 subplot_columns=1,
                 subplot_rows=1):
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.tight_layout = tight_layout
        self.subplot_columns = subplot_columns
        self.subplot_rows = subplot_rows
        self.subplots = subplots


@export
class FigureSchema(Schema):
    edgecolor = fields.String(description="Edge color", required=False, load_default="white")
    facecolor = fields.String(description="Face color", required=False, load_default="white")
    subplot_columns = fields.Integer(description="Number of columns of suplots grid", required=False, load_default=1)
    subplot_rows = fields.Integer(description="Number of rows of suplots grid", required=False, load_default=1)
    tight_layout = fields.Bool(description="Tight layout switch", required=False, load_default=False)
    subplots = fields.List(fields.Nested(SubplotSchema), description="List of subplots", required=True)

    @post_load
    def load_figure(self, data, **kwargs):
        return FigureParams(**data)

from marshmallow_oneofschema import OneOfSchema

from src.schemas.hist import Hist, HistSchema
from src.schemas.plot import Plot, PlotSchema


class BasePlotSchema(OneOfSchema):
    type_schemas = {"plot": PlotSchema, "hist": HistSchema}

    def get_obj_type(self, obj):
        if isinstance(obj, Plot):
            return "plot"
        elif isinstance(obj, Hist):
            return "hist"
        else:
            raise Exception("Unknown object type: {}".format(obj.__class__.__name__))

import json

from flask import Blueprint, request

from schemas import FigureSchema, ResponseSchema
from schemas.response import Response

figure_bp = Blueprint(name="figure_bp", import_name=__name__)


@figure_bp.route('/', methods=['POST'])
def build_figure():
    """
    ---
    post:
      description: matplotlib.figure endpoint
      requestBody:
        required: true
        content:
            application/json:
                schema: FigureSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ResponseSchema
    """
    figure_schema = FigureSchema()
    figure = figure_schema.load(request.json)

    resp = Response(json.dumps(figure.__dict__))
    r = ResponseSchema().dump(resp)
    return r

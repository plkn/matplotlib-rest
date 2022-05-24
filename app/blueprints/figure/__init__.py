import json

from flask import Blueprint, request, send_file

from core import build_figure
from schemas import FigureSchema, ResponseSchema
from schemas.response import Response

figure_bp = Blueprint(name="figure_bp", import_name=__name__)


@figure_bp.route('/', methods=['POST'])
def build():
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

    build_figure(figure)

    resp = Response(json.dumps(figure.__dict__))
    r = ResponseSchema().dump(resp)
    return r

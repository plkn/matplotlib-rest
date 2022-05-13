# from bottle import route, request, run
from flask import Blueprint, jsonify, request

from src.schemas import FigureSchema

plot_bp = Blueprint(name="plot_bp", import_name=__name__)


@plot_bp.route('/', methods=['POST'])
def plot():
    """
    ---
    post:
      description: matplotlib.plot endpoint
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
    req = figure_schema.load(request.json)

    output = {"msg": "I'm the test endpoint from matplotlib.plot."}
    return jsonify(output)


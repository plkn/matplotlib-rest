from flask import Blueprint, jsonify, request

plot_bp = Blueprint(name="plot_bp", import_name=__name__)


@plot_bp.route('/test', methods=['GET'])
def test():
    """
    ---
    get:
      description: test endpoint
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - testing
    """
    output = {"msg": "I'm the test endpoint from blueprint_x."}
    return jsonify(output)


# add view function to the blueprint
# @plot_bp.route('/plus', methods=['POST'])
# def plus_x():
#     # retrieve body data from input JSON
#     data = request.get_json()
#     in_val = data['number']
#     # compute result and output as JSON
#     result = in_val + x
#     output = {"msg": f"Your result is: '{result}'"}
#     return jsonify(output)

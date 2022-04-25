"""Flask Application"""

# load libaries
from flask import Flask

# load modules
from src.blueprints.plot_blueprint import plot_bp

# init Flask app
app = Flask(__name__)

app.register_blueprint(plot_bp, url_prefix="/api/v1/plot")

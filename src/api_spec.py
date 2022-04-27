"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from src.schemas import *

# Create an APISpec
spec = APISpec(
    title="Matplotlib REST API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# register schemas with spec
spec.components.schema("Line", schema=LineSchema)
spec.components.schema("Plot", schema=PlotSchema)

"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

import src.schemas as schemas

# Create an APISpec
spec = APISpec(
    title="Matplotlib REST API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# register schemas with spec


for sc in map(schemas.__dict__.get, schemas.__all__):
    spec.components.schema(sc)

spec.components.schema("Figure", schema=FigureSchema)
# spec.components.schema("Plot", schema=PlotSchema)

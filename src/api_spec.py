"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec_oneofschema import MarshmallowPlugin
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
for sc in map(lambda _: (_, schemas.__dict__.get(_)), schemas.__all__):
    spec.components.schema(sc[0], schema=sc[1])

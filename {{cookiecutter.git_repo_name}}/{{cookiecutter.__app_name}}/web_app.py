"""
FastAPI WebApp
"""
{% if cookiecutter.include_webpages == "y" %}
import os
from fastapi.staticfiles import StaticFiles
{% endif %}
from fastapi import FastAPI
from {{cookiecutter.__app_name}}.version import __version__
from {{cookiecutter.__app_name}}.routers import example
{% if cookiecutter.include_webpages == "y" %}
from {{cookiecutter.__app_name}}.routers import hello_world

static_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
{% endif %}

# Used to config swagger UI
# Reference : https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
swagger_ui_parameters = {
    'docExpansion': 'none',
    'filter': 'true'
}

web_app = FastAPI(title='{{ cookiecutter.git_repo_name }}', version=__version__,
                  description='{{ cookiecutter.app_description }}', swagger_ui_parameters=swagger_ui_parameters)
web_app.include_router(example.router)
{% if cookiecutter.include_webpages == "y" %}
web_app.include_router(hello_world.router)

web_app.mount("/static", StaticFiles(directory=static_path), name="static")
{% endif %}

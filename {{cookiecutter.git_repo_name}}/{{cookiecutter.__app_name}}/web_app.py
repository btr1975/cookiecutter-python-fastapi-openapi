"""
FastAPI WebApp
"""
{% if cookiecutter.include_webpages == "y" %}
import os
from fastapi.staticfiles import StaticFiles
{% endif %}
from fastapi import FastAPI
{% if cookiecutter.package_manager == 'pip' %}
from {{cookiecutter.__app_name}}.version import __version__
{% elif cookiecutter.package_manager == 'uv' %}
from importlib.metadata import version
{% endif %}
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

{% if cookiecutter.package_manager == 'pip' %}
web_app = FastAPI(title='{{ cookiecutter.git_repo_name }}', version=__version__,
                  description='{{ cookiecutter.app_description }}', swagger_ui_parameters=swagger_ui_parameters)
{% elif cookiecutter.package_manager == 'uv' %}
web_app = FastAPI(title='{{ cookiecutter.git_repo_name }}', version=version("{{cookiecutter.git_repo_name}}"),
                  description='{{ cookiecutter.app_description }}', swagger_ui_parameters=swagger_ui_parameters)
{% endif %}

web_app.include_router(example.router)
{% if cookiecutter.include_webpages == "y" %}
web_app.include_router(hello_world.router)

web_app.mount("/static", StaticFiles(directory=static_path), name="static")
{% endif %}

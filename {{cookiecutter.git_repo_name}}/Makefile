# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.8
#

.PHONY: all info build build-container coverage format pylint pytest gh-pages build dev-run start-container \
	stop-container remove-container check-vuln check-security

info:
	@echo "make options"
	@echo "    all                 To run coverage, format, pylint, and check-vuln"
	@echo "    build               To build a distribution"
	@echo "    build-container     To build a container image"
	@echo "    check-vuln          To check for vulnerabilities in the dependencies"
	@echo "    check-security      To check for vulnerabilities in the code"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    dev-run             To run the app"
	@echo "    format              To format the code with black"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    start-container     To start the container"
	@echo "    stop-container      To stop the container"
	@echo "    remove-container    To remove the container"
{% if cookiecutter.app_documents_location == 'github-pages' %}	@echo "    gh-pages           To create the GitHub pages"{% endif %}

all: format pylint coverage check-security check-vuln

build:
	@python -m build

{% if cookiecutter.container_runtime == "podman" %}
build-container:
	@cd containers && podman build --ssh=default --build-arg=build_branch=main -t {{ cookiecutter.git_repo_name }}:latest -f Containerfile
{% endif %}

{% if cookiecutter.container_runtime == "docker" %}
build-container:
	@cd containers && docker build --ssh=default --build-arg=build_branch=main -t {{ cookiecutter.git_repo_name }}:latest -f Dockerfile
{% endif %}

coverage:
	@pytest --cov --cov-report=html -vvv

format:
	@black {{cookiecutter.__app_name}}/
	@black tests/

pylint:
	@pylint {{cookiecutter.__app_name}}/

pytest:
	@pytest --cov -vvv

dev-run:
	@python -c "from {{cookiecutter.__app_name}} import cli;cli()" start -p 8080 -r

{% if cookiecutter.app_documents_location == 'github-pages' %}
gh-pages:
	@rm -rf ./docs/source/code
	@sphinx-apidoc -o ./docs/source/code ./{{cookiecutter.__app_name}}
	@sphinx-build ./docs ./docs/gh-pages
{% endif %}

{% if cookiecutter.container_runtime == "podman" %}
start-container:
	@podman run -itd --name {{ cookiecutter.git_repo_name }} -p 8080:8080 localhost/{{ cookiecutter.git_repo_name }}:latest

stop-container:
	@podman stop {{ cookiecutter.git_repo_name }}

remove-container:
	@podman rm {{ cookiecutter.git_repo_name }}
{% endif %}

{% if cookiecutter.container_runtime == "docker" %}
start-container:
	@docker run -itd --name {{ cookiecutter.git_repo_name }} -p 8080:8080 localhost/{{ cookiecutter.git_repo_name }}:latest

stop-container:
	@docker stop {{ cookiecutter.git_repo_name }}

remove-container:
	@docker rm {{ cookiecutter.git_repo_name }}
{% endif %}

check-vuln:
	@pip-audit -r requirements.txt

check-security:
	@bandit -c pyproject.toml -r .

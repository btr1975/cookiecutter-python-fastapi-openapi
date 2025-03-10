@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.6
REM

IF "%1" == "all" (
    pytest --cov --cov-report=html -vvv
    black {{cookiecutter.__app_name}}/
    black tests/
    pylint {{cookiecutter.__app_name}}\
    pip-audit -r requirements.txt
    GOTO END
)

IF "%1" == "build" (
    python -m build
    GOTO END
)

IF "%1" == "coverage" (
    pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "pylint" (
    pylint {{cookiecutter.__app_name}}\
    GOTO END
)

IF "%1" == "pytest" (
    pytest --cov -vvv
    GOTO END
)

IF "%1" == "dev-run" (
    python -c "from {{cookiecutter.__app_name}} import cli;cli()" start -p 8080 -r
    GOTO END
)

IF "%1" == "format" (
    black {{cookiecutter.__app_name}}/
    black tests/
    GOTO END
)

IF "%1" == "check-vuln" (
    pip-audit -r requirements.txt
    GOTO END
)

{% if cookiecutter.app_documents_location == 'github-pages' %}
IF "%1" == "gh-pages" (
    rmdir /s /q docs\source\code
    sphinx-apidoc -o ./docs/source/code ./{{cookiecutter.__app_name}}
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)
{% endif %}

@ECHO make options
@ECHO     all                 To run coverage, format, pylint, and check-vuln
@ECHO     build               To build a distribution
@ECHO     check-vuln          To check for vulnerabilities
@ECHO     coverage            To run coverage and display ASCII and output to htmlcov
@ECHO     dev-run             To run the app
@ECHO     format              To format the code with black
@ECHO     pylint              To run pylint
@ECHO     pytest              To run pytest with verbose option
{% if cookiecutter.app_documents_location == 'github-pages' %}@ECHO     gh-pages  To create the GitHub pages{% endif %}

:END

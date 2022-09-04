@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.1
REM

IF "%1" == "app-run" (
    python app_run.py
    GOTO END
)

IF "%1" == "coverage" (
    coverage erase
    coverage run
    coverage report
    coverage html
    GOTO END
)

IF "%1" == "pylint" (
    pylint modules\
    GOTO END
)

IF "%1" == "pytest" (
    pytest -vvv
    GOTO END
)

IF "%1" == "pdf" (
    sphinx-build -b rinoh ./docs ./docs/_build/pdf
    GOTO END
)

IF "%1" == "word" (
    sphinx-build -b docx ./docs ./docs/_build/word
    GOTO END
)

{% if cookiecutter.app_documents_location == 'github-pages' %}
IF "%1" == "gh-pages" (
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)
{% endif %}

@ECHO make options
@ECHO     app-run   To run the app
@ECHO     coverage  To run coverage and display ASCII and output to htmlcov
@ECHO     pylint    To run pylint
@ECHO     pytest    To run pytest with verbose option
@ECHO     pdf       To create PDF Docs
@ECHO     word      To create Word Docs
{% if cookiecutter.app_documents_location == 'github-pages' %}@ECHO     gh-pages  To create the GitHub pages{% endif %}

:END

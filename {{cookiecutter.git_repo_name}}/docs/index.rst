.. pname documentation master file, created by
   sphinx-quickstart on Thu Jan 27 10:22:38 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{ cookiecutter.git_repo_name }} documentation
===============================================================================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   source/index

{% if cookiecutter.app_documents_theme == "alabaster" %}
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
{% endif %}

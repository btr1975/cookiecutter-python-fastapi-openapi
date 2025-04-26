import os
import sys
import pytest

base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


@pytest.fixture
def bake_project_api_only_podman() -> dict:
    options = {
        "git_repo_name": "api-only",
        "include_webpages": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_api_only_podman() -> dict:
    options = {
        "git_repo_name": "api-only",
        "include_webpages": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_api_only_docker() -> dict:
    options = {
        "git_repo_name": "api-only",
        "include_webpages": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_api_only_docker() -> dict:
    options = {
        "git_repo_name": "api-only",
        "include_webpages": "n",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_api_with_webpages_podman() -> dict:
    options = {
        "git_repo_name": "api-with-webpages",
        "include_webpages": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_api_with_webpages_podman() -> dict:
    options = {
        "git_repo_name": "api-with-webpages",
        "include_webpages": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_api_with_webpages_docker() -> dict:
    options = {
        "git_repo_name": "api-with-webpages",
        "include_webpages": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_uv_api_with_webpages_docker() -> dict:
    options = {
        "git_repo_name": "api-with-webpages",
        "include_webpages": "y",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "uv",
    }

    return options

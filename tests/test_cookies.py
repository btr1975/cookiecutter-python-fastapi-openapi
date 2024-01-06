def test_bake_project_api_only_podman(cookies, bake_project_api_only):
    result = cookies.bake(extra_context=bake_project_api_only)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'api-only'
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('README.md').is_file()
    assert result.project_path.joinpath('api_only').is_dir()
    assert result.project_path.joinpath('containers').is_dir()
    assert result.project_path.joinpath('containers', 'Containerfile').is_file()
    assert not result.project_path.joinpath('containers', 'Dockerfile').is_file()
    assert not result.project_path.joinpath('api_only', 'static').is_dir()
    assert not result.project_path.joinpath('api_only', 'templates').is_dir()
    assert not result.project_path.joinpath('api_only', 'routers', 'hello_world.py').is_file()


def test_bake_project_api_with_webpages_podman(cookies, bake_project_api_with_webpages):
    result = cookies.bake(extra_context=bake_project_api_with_webpages)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'api-with-webpages'
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('README.md').is_file()
    assert result.project_path.joinpath('api_with_webpages').is_dir()
    assert result.project_path.joinpath('containers').is_dir()
    assert result.project_path.joinpath('containers', 'Containerfile').is_file()
    assert not result.project_path.joinpath('containers', 'Dockerfile').is_file()
    assert result.project_path.joinpath('api_with_webpages', 'static').is_dir()
    assert result.project_path.joinpath('api_with_webpages', 'templates').is_dir()
    assert result.project_path.joinpath('api_with_webpages', 'routers', 'hello_world.py').is_file()

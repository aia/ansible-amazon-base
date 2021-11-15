def test_docker_package(host):
    docker_package = host.package("docker")
    assert docker_package.is_installed  # nosec


def test_docker_service(host):
    docker_service = host.service("docker")
    assert docker_service.is_running  # nosec
    assert docker_service.is_enabled  # nosec

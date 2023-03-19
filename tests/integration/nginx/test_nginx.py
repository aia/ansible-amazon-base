def test_nginx_package(host):
    nginx_package = host.package("nginx")
    assert nginx_package.is_installed  # nosec


def test_nginx_service(host):
    nginx_service = host.service("nginx")
    assert nginx_service.is_running  # nosec
    assert nginx_service.is_enabled  # nosec

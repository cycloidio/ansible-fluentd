import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    present = [
        "/etc/td-agent"
    ]
    if present:
        for directory in present:
            d = host.file(directory)
            assert d.is_directory
            assert d.exists


def test_files(host):
    present = [
        "/etc/td-agent/td-agent.conf",
        "/etc/td-agent/conf.d/filter.conf",
        "/etc/td-agent/conf.d/match.conf",
        "/etc/td-agent/conf.d/plugin.conf",
        "/etc/td-agent/conf.d/source.conf"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_service(host):
    present = [
        "td-agent"
    ]
    if present:
        for service in present:
            s = host.service(service)
            assert s.is_enabled
            assert s.is_running


def test_packages(host):
    present = [
        "td-agent"
    ]
    if present:
        for package in present:
            p = host.package(package)
            assert p.is_installed


# Prometheus
def test_socket(host):
    present = [
        "tcp://127.0.0.1:24231"
    ]
    for socket in present:
        s = host.socket(socket)
        assert s.is_listening

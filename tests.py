import pytest
from click.testing import CliRunner

from browserly.cli import cli


@pytest.fixture
def runner():
    """ prefix alias function """
    return CliRunner


def test_cli(runner):
    result = runner().invoke(cli)
    assert result.exit_code == 0


def test_screenshot(runner):
    result = runner().invoke(cli, ['screenshot', '--p', '/tmp', '--url', 'https://db.com'])
    assert result.exit_code == 0

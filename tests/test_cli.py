import os
from click.testing import CliRunner

from scm_source.cli import main


def test_main(monkeypatch):
    monkeypatch.setattr('scm_source.cli.generate_scm_source', lambda x, y, z, q: True)
    runner = CliRunner()
    result = runner.invoke(main, [], catch_exceptions=False)
    assert 'Generating scm-source.json.. LOCALLY MODIFIED' in result.output


def test_directory_arg(monkeypatch):
    def generate_scm_source(x, y, directory, fatal_on_modified):
        assert 'mydir' == directory
        return False
    monkeypatch.setattr('scm_source.cli.generate_scm_source', generate_scm_source)
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.makedirs('mydir')
        result = runner.invoke(main, ['mydir'], catch_exceptions=False)
    assert 'Generating scm-source.json.. OK' in result.output
    assert 0 == result.exit_code


def test_directory_does_not_exist(monkeypatch):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, ['does-not-exist'], catch_exceptions=False)
    assert 'Path "does-not-exist" does not exist' in result.output
    assert 2 == result.exit_code


def test_directory_multiple_args(monkeypatch):
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.makedirs('foo')
        os.makedirs('bar')
        result = runner.invoke(main, ['foo', 'bar'], catch_exceptions=False)
    assert 'At most one directory can be given' in result.output
    assert 2 == result.exit_code


def test_fail_on_modified_with_flag(monkeypatch):
    def mocked_generate_scm_source(x, y, z, fail_on_modified):
        raise RuntimeError
    monkeypatch.setattr('scm_source.cli.generate_scm_source', mocked_generate_scm_source)
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.makedirs('foo')
        result = runner.invoke(main, ['--fail-on-modified', 'foo'])
    assert result.exit_code != 0


def test_no_fail_on_modified_without_flag(monkeypatch):
    def mocked_generate_scm_source(x, y, z, fail_on_modified):
        return 'non empty status'
    monkeypatch.setattr('scm_source.cli.generate_scm_source', mocked_generate_scm_source)
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.makedirs('foo')
        result = runner.invoke(main, ['foo'])
    assert result.exit_code == 0
    assert 'Generating scm-source.json.. LOCALLY MODIFIED' in result.output

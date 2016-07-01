from click.testing import CliRunner

from scm_source.cli import main

def test_main(monkeypatch):
    monkeypatch.setattr('scm_source.cli.generate_scm_source', lambda x, y, z: True)
    runner = CliRunner()
    result = runner.invoke(main, [], catch_exceptions=False)
    assert 'Generating scm-source.json.. LOCALLY MODIFIED' in result.output


def test_directory_arg(monkeypatch):
    def generate_scm_source(x, y, directory):
        assert 'mydir' == directory
        return False
    monkeypatch.setattr('scm_source.cli.generate_scm_source', generate_scm_source)
    runner = CliRunner()
    result = runner.invoke(main, ['mydir'], catch_exceptions=False)
    assert 'Generating scm-source.json.. OK' in result.output


def test_directory_multiple_args(monkeypatch):
    runner = CliRunner()
    result = runner.invoke(main, ['foo', 'bar'], catch_exceptions=False)
    assert 'At most one directory can be given' in result.output
    assert 2 == result.exit_code

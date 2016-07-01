from click.testing import CliRunner

from scm_source.cli import main

def test_main(monkeypatch):
    monkeypatch.setattr('scm_source.cli.generate_scm_source', lambda x, y, z: True)
    runner = CliRunner()
    result = runner.invoke(main, [], catch_exceptions=False)
    assert 'Generating scm-source.json.. LOCALLY MODIFIED' in result.output

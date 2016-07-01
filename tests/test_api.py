import os
from scm_source import generate_scm_source

def test_generate_scm_source(monkeypatch):
    monkeypatch.setattr('subprocess.check_output', lambda x: b'test')
    generate_scm_source('test.json', 'JohnDoe')
    os.unlink('test.json')


def test_generate_scm_source_dir(monkeypatch):
    def check_output(x):
        assert '--git-dir=somedir/.git' in x
        assert '--work-tree=somedir' in x
        return b'test'
    monkeypatch.setattr('subprocess.check_output', check_output)
    generate_scm_source('test.json', 'JohnDoe', 'somedir')
    os.unlink('test.json')

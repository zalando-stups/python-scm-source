import os
from scm_source import generate_scm_source

def test_generate_scm_source(monkeypatch):
    monkeypatch.setattr('subprocess.check_output', lambda x: b'test')
    generate_scm_source('test.json', 'JohnDoe')
    os.unlink('test.json')

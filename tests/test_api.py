import os
import pytest
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
    monkeypatch.setattr('os.path.isdir', lambda x: True)
    monkeypatch.setattr('subprocess.check_output', check_output)
    generate_scm_source('test.json', 'JohnDoe', 'somedir')
    os.unlink('test.json')


def test_generate_scm_source_dir_not_exists(monkeypatch):
    monkeypatch.setattr('os.path.isdir', lambda x: False)
    with pytest.raises(FileNotFoundError):
        generate_scm_source('test.json', 'JohnDoe', 'does-not-exist')


def test_generate_scm_source_throws_on_fail_on_modified(monkeypatch):
    def mocked_check_output(x):
        return b'NONEMPTY STRING'
    monkeypatch.setattr('subprocess.check_output', mocked_check_output)
    with pytest.raises(RuntimeError):
        generate_scm_source('', '', fail_on_modified=True)

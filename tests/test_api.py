import os
import pytest
from scm_source import generate_scm_source
from scm_source.api import get_remote


def test_generate_scm_source(monkeypatch):
    monkeypatch.setattr('subprocess.check_output', lambda x: b'test')
    generate_scm_source('test.json', 'JohnDoe', remote = 'test')
    os.unlink('test.json')


def test_generate_scm_source_dir(monkeypatch):
    def check_output(x):
        return b'test'
    monkeypatch.setattr('os.path.isdir', lambda x: True)
    monkeypatch.setattr('subprocess.check_output', check_output)
    generate_scm_source('test.json', 'JohnDoe', 'somedir', remote = 'test')
    os.unlink('test.json')


def test_generate_scm_source_dir_not_exists(monkeypatch):
    monkeypatch.setattr('os.path.isdir', lambda x: False)
    with pytest.raises(FileNotFoundError):
        generate_scm_source('test.json', 'JohnDoe', 'does-not-exist')


def test_generate_scm_source_throws_on_fail_on_modified(monkeypatch):
    def check_output(x):
        return b'test'
    monkeypatch.setattr('subprocess.check_output', check_output)
    with pytest.raises(RuntimeError):
        generate_scm_source('', '', fail_on_modified=True, remote = 'test')


def test_get_remote_name(monkeypatch):
    def check_output(x):
        return b'test'
    monkeypatch.setattr('subprocess.check_output', check_output)
    url = get_remote('test')
    assert url == 'test'


def test_get_remote_url(monkeypatch):
    def check_output(x):
        if 'remote' in x:
            return b'test'
        else:
            return b'url'
    monkeypatch.setattr('subprocess.check_output', check_output)
    url = get_remote('url')
    assert url == 'url'


def test_get_remote_fail_non_existing_remote(monkeypatch):
    def check_output(x):
        return b'test'
    monkeypatch.setattr('subprocess.check_output', check_output)
    with pytest.raises(RuntimeError):
        url = get_remote('somethingelse')
    
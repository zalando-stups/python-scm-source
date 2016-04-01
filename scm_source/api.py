import json
import subprocess


def get_output(cmd: list):
    '''Get stripped command output'''
    raw = subprocess.check_output(cmd)
    return raw.decode('utf-8').strip()


def get_scm_source_data(author: str):
    '''Get SCM source data of current working directory'''
    rev = get_output(['git', 'rev-parse', 'HEAD'])
    url = get_output(['git', 'config', '--get', 'remote.origin.url'])
    status = get_output(['git', 'status', '--porcelain'])
    if status:
        rev = '{} (locally modified)'.format(rev)
    data = {'url': 'git:{}'.format(url), 'revision': rev, 'author': author or 'UNKNOWN', 'status': status}
    return data


def generate_scm_source(path: str, author: str):
    '''Generate and write scm-source.json'''
    data = get_scm_source_data(author)
    with open(path, 'w', encoding='utf-8') as fd:
        json.dump(data, fd)
    return data['status']

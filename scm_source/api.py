import json
import os
import subprocess


def get_output(cmd: list):
    '''Get stripped command output'''
    raw = subprocess.check_output(cmd)
    return raw.decode('utf-8').strip()


def get_scm_source_data(author: str, directory: str=None):
    '''Get SCM source data of current working directory'''
    base = ['git']
    if directory:
        git_dir = os.path.join(directory, '.git')
        if not os.path.isdir(git_dir):
            raise FileNotFoundError("No such directory: '{}'".format(git_dir))
        base += ['--git-dir={}'.format(git_dir), '--work-tree={}'.format(directory)]
    rev = get_output(base + ['rev-parse', 'HEAD'])
    url = get_output(base + ['config', '--get', 'remote.origin.url'])
    status = get_output(base + ['status', '--porcelain'])
    if status:
        rev = '{} (locally modified)'.format(rev)
    data = {'url': 'git:{}'.format(url), 'revision': rev, 'author': author or 'UNKNOWN', 'status': status}
    return data


def generate_scm_source(path: str, author: str, directory: str=None, fail_on_modified: bool = False):
    '''Generate and write scm-source.json'''
    data = get_scm_source_data(author, directory)
    is_locally_modified = data['status']

    if is_locally_modified and fail_on_modified:
        raise RuntimeError('Code tree has been modified')

    with open(path, 'w', encoding='utf-8') as fd:
        json.dump(data, fd)
    return is_locally_modified

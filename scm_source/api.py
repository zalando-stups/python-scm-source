import json
import os
import subprocess


def get_output(cmd: list):
    '''Get stripped command output'''
    raw = subprocess.check_output(cmd)
    return raw.decode('utf-8').strip()


def get_scm_source_data(author: str, directory: str = None, remote: str = 'origin'):
    '''Get SCM source data of current working directory'''
    base = ['git']
    if directory:
        git_dir = os.path.join(directory, '.git')
        if not os.path.isdir(git_dir):
            raise FileNotFoundError("No such directory: '{}'".format(git_dir))
        base += ['--git-dir={}'.format(git_dir), '--work-tree={}'.format(directory)]
    rev = get_output(base + ['rev-parse', 'HEAD'])
    url = get_remote(remote)
    status = get_output(base + ['status', '--porcelain'])
    if status:
        rev = '{} (locally modified)'.format(rev)
    data = {'url': 'git:{}'.format(url), 'revision': rev, 'author': author or 'UNKNOWN', 'status': status}
    return data


def get_remote(remote: str):
    '''Get the remote URL for a configured remote name or verify the given remote URL'''
    base = ['git']
    remotes = {}
    remote_names = get_output(base + ['remote']).split('\n')
    for rem in remote_names:
        url = get_output(base + ['config', '--get', 'remote.{}.url'.format(rem)])
        remotes[rem] = url
    if remote in remotes:
        return remotes[remote]
    elif remote in remotes.values():
        return remote
    else:
        raise RuntimeError('The provided remote ({}) is not configured for this repository'.format(remote))


def generate_scm_source(path: str, author: str, directory: str = None, fail_on_modified: bool = False,
                        remote: str = 'origin'):
    '''Generate and write scm-source.json'''
    data = get_scm_source_data(author, directory, remote)
    is_locally_modified = data['status']

    if is_locally_modified and fail_on_modified:
        raise RuntimeError('Code tree has been modified')

    with open(path, 'w', encoding='utf-8') as fd:
        json.dump(data, fd)
    return is_locally_modified

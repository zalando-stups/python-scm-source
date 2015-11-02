import click
import json
import subprocess


@click.command()
@click.option('-f', '--file', type=click.File('wb'), default='scm-source.json')
@click.option('--author', envvar='USER')
def main(file, author):

    rev = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    url = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
    status = subprocess.check_output(['git', 'status', '--procelain'])
    if status:
        rev += ' (locally modified)'
    data = {'url': 'git:{}'.format(url), 'revision': rev, 'author': author, 'status': status}

    json.dump(file, data)

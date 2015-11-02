import click
from clickclick import Action
from .api import generate_scm_source


@click.command()
@click.option('-f', '--file', metavar='PATH', default='scm-source.json', help='file path to write to')
@click.option('--author', metavar='USER', envvar='USER', help='author of the scm-source.json (default: current $USER)')
def main(file, author):
    with Action('Generating {}..'.format(file)) as act:
        locally_modified = generate_scm_source(file, author)
        if locally_modified:
            act.warning('LOCALLY MODIFIED')

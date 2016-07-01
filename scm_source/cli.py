import click
from clickclick import Action
from .api import generate_scm_source


@click.command()
@click.option('-f', '--file', metavar='PATH', default='scm-source.json', help='file path to write to')
@click.option('--author', metavar='USER', envvar='USER', help='author of the scm-source.json (default: current $USER)')
@click.argument('directory', nargs=-1, type=click.Path(exists=True))
def main(file, author, directory):
    if not directory:
        directory = None
    elif len(directory) == 1:
        directory = directory[0]
    else:
        raise click.UsageError('At most one directory can be given')
    with Action('Generating {}..'.format(file)) as act:
        locally_modified = generate_scm_source(file, author, directory)
        if locally_modified:
            act.warning('LOCALLY MODIFIED')

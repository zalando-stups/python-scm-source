import click
from clickclick import Action
from .api import generate_scm_source


@click.command()
@click.option('-f', '--file', metavar='PATH', default='scm-source.json', help='file path to write to')
@click.option('--author', metavar='USER', envvar='USER', help='author of the scm-source.json (default: current $USER)')
@click.argument('directory', nargs=-1, type=click.Path(exists=True))
@click.option('--fail-on-modified', help="fails on locally modified code tree", is_flag=True)
def main(file, author, directory, fail_on_modified):
    if not directory:
        directory = None
    elif len(directory) == 1:
        directory = directory[0]
    else:
        raise click.UsageError('At most one directory can be given')
    with Action('Generating {}..'.format(file)) as act:
        try:
            if generate_scm_source(file, author, directory, fail_on_modified):
                act.warning('LOCALLY MODIFIED')
        except RuntimeError as e:
            act.fatal_error(str(e))

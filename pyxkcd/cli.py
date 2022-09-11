import json
import click

from pyxkcd.constants import OUTPUT_IMAGE, OUTPUT_JSON, VALID_OUTPUTS
from pyxkcd import xkcd, image


@click.command()
@click.option(
    "--random",
    is_flag=True,
    show_default=True,
    default=False,
    help="get a random comic",
)
@click.option("--number", "-n", default=-1, help="get specific comic with that number")
@click.option(
    "--output",
    "-o",
    default=OUTPUT_IMAGE,
    type=click.Choice(VALID_OUTPUTS),
    help="output format",
)
def cli(random: bool, number: int, output: str):
    """Get a XKCD comic"""
    if random and number != -1:
        click.echo("ERROR: Can't set both --random and --number")
        return

    if random:
        comic = xkcd.fetch_random()
    elif number != -1:
        comic = xkcd.fetch_specific(number)
    else:
        comic = xkcd.fetch_latest()

    if output == OUTPUT_IMAGE:
        image.render_from_url(comic["img"])
        click.echo(comic["alt"])
    elif output == OUTPUT_JSON:
        click.echo(json.dumps(comic, indent=2))

import click

from rippling_cli.cli.commands.flux.app import app
from rippling_cli.cli.commands.flux.build import build
from rippling_cli.cli.commands.flux.check import check
from rippling_cli.cli.commands.flux.server import server
from rippling_cli.utils.login_utils import ensure_logged_in


@click.group()
@click.pass_context
def flux(ctx: click.Context):
    """
    Manage Rippling Flux apps and integrations.

    This command group is the entry point for the Flux CLI application. It
    serves as the base command group and provides access to various subcommands
    for managing and interacting with Flux apps, builds, and other related
    functionality.

    The flux command group itself does not perform any specific actions but
    acts as a container for its subcommands. It is responsible for setting up
    the initial context and ensuring that the user is logged in before
    executing any subcommands.

    """
    ensure_logged_in(ctx)


flux.add_command(app)  # type: ignore
flux.add_command(build)  # type: ignore
flux.add_command(check)  # type: ignore
flux.add_command(server)  # type: ignore

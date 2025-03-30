import click
from .project_creator import ProjectCreator


def str_to_bool(value):
    """Convert various string inputs to boolean."""
    value = value.lower()
    return value in ['yes', 'y', 'true', '1']


def print_header():
    """Print the header for the CLI."""
    title = "Django Project Generator"
    description = "Create and configure your Django projects easily! 🎉"
    border = "=" * len(title)

    click.echo(click.style(border, fg='green'))
    click.echo(click.style(title, fg='green', bold=True))
    click.echo(click.style(description, fg='green'))
    click.echo(click.style(border, fg='green'))
    click.echo()  # Empty line for spacing


@click.group()
def main():
    """Tools to create Django projects. 📦"""
    print_header()
    pass


@main.command()
def create():
    """Create a new Django project. 📦"""
    project_name = click.prompt(click.style('🌟 Project name:', fg='cyan'))
    api = click.prompt(click.style(
        '🌐 Is the project intended for an API? (yes/no):', fg='cyan'), type=str_to_bool)

    security = None
    if api:
        security = click.prompt(click.style(
            '🔒 Use authtoken for security? (yes/no):', fg='cyan'), type=str_to_bool)

    app_names = click.prompt(click.style(
        '📱 Enter app names separated by commas (e.g., app1, app2):', fg='cyan'))
    app_list = [name.strip() for name in app_names.split(',') if name.strip()]

    custom_user = click.prompt(click.style(
        '👤 Use a custom user? (yes/no):', fg='cyan'), type=str_to_bool)
    custom_user_app = None
    if custom_user:
        custom_user_app = click.prompt(click.style(
            '📁 In which app should the custom user be saved?:', fg='cyan'))

    creator = ProjectCreator(project_name, api, security,
                             app_list, custom_user, custom_user_app)
    creator.create_project()
    click.echo(click.style(
        f'🎊 Project {project_name} created successfully!', fg='green'))


if __name__ == '__main__':
    main()

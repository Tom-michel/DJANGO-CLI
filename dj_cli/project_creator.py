import os
import subprocess
import sys
import json
import click


class ProjectCreator:
    def __init__(self, project_name, api, security, app_list, custom_user, custom_user_app):
        self.project_name = project_name
        self.api = api
        self.security = security if api else None  # Only set security if API is used
        self.app_list = app_list
        self.custom_user = custom_user
        self.custom_user_app = custom_user_app

    def create_project(self):
        # Generate the configuration file
        self.create_config_file()

        # Determine dependencies
        dependencies = ['Django']
        if self.api:
            dependencies.append('djangorestframework')

        # Install dependencies
        self.install_dependencies(dependencies)

        # Create the Django project
        os.makedirs(self.project_name, exist_ok=True)
        os.chdir(self.project_name)

        # Create the Django project in the correct location
        subprocess.run([sys.executable, '-m', 'django',
                       'startproject', self.project_name, '.'])

        # Create apps
        for app_name in self.app_list:
            subprocess.run(
                [sys.executable, '-m', 'django', 'startapp', app_name])

        # Generate requirements.txt
        self.create_requirements_file()

        # Configure files
        self.configure_settings()

        if self.custom_user:
            self.create_custom_user()

        # Display next steps
        self.display_next_steps()

    def create_config_file(self):
        """Create the dj-config.json file with user choices."""
        config = {
            'project_name': self.project_name,
            'api': self.api,
            'security': self.security,
            'apps': self.app_list,
            'custom_user': self.custom_user,
            'custom_user_app': self.custom_user_app
        }

        with open('dj-config.json', 'w') as config_file:
            json.dump(config, config_file, indent=4)

    def install_dependencies(self, dependencies):
        """Install dependencies using pip."""
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install'] + dependencies)

    def create_requirements_file(self):
        """Create requirements.txt using pip freeze."""
        with open('requirements.txt', 'w') as f:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'freeze'], stdout=f)

    def configure_settings(self):
        # Logic to configure settings.py, using the dj-config.json file.
        pass

    def create_custom_user(self):
        """Logic to create a custom user model."""
        # Implement custom user creation logic based on self.custom_user_app
        pass

    def display_next_steps(self):
        """Display instructions for the next steps after project creation."""
        click.echo(click.style(
            f'🎊 Project {self.project_name} created successfully!\n', fg='green'))
        click.echo(f"\nNext steps to run your Django project:")
        click.echo(
            f"> cd {self.project_name}/")
        click.echo(
            "> python manage.py runserver\n")

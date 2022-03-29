'''2022/03/29 by PianisT
This terminal application creates text files bases on templates.'''


import os
import subprocess  # module used to execute terminal commands and catch its outputs.
from datetime import datetime

import click


# Constructing a path object that suports the "~" character to refer home directory.
path = os.path.expanduser('~/.TextFileTemplates/')


@click.group()
def template():
    # Creating required hidden directory "TextFileTemplates" in home directory if is not created yet. 
    if os.path.isdir(path):
        pass
    else:
        click.echo('Creating required directory "TextFileTemplates" in home directory...')
        os.mkdir(path)

    click.echo('')


@template.command()
@click.option('--new_template', is_flag=True, default=None, help='Create a new template')
@click.option('--new_file', is_flag=True, default=True, help='Create new file using an existing template')
@click.option('--override', is_flag=True, default=None, help='Override file with same name created with template')
@click.argument('file_to_use', required=True)
@click.argument('file_to_create', required=True)
def create(new_template, new_file, override, file_to_use, file_to_create):
    '''Creates a new template or a new file using an existing template.'''

    # If the "--new_template" flag is used, the program checks if already exist a file
    # with the name given by the argument. If not exist, creates the new template in the
    # "templates" folder of this project.
    if new_template:

        try:  # Checks if the file to use for create the new template exists.
            with open(file_to_use, 'r') as f:
                template = f.read()
        except FileNotFoundError:
            click.echo(f'ERROR: The file to use "{file_to_use}" do not exist.')
            return None

        try:  # Checks if the template file to create already exists.
            with open(f'{path}{file_to_create}') as f:
                pass 
        except FileNotFoundError:
            click.echo(f'Creating new template "{file_to_create}"...')
            with open(f'{path}{file_to_create}', 'x') as template_to_create:
                template_to_create.write(template) 
            click.echo(f'"{file_to_create}" successfully created!')
            click.echo(f'"{file_to_create}" is now available to use as a template for new text files.')
        else:
            click.echo(f'ERROR: A file with name "{file_to_create}" already exist.')
            return None
                    
    # if the "--new_file" flag is used, the program creates a new file in the path given by
    # the argument passed (default is current directory) using a template from the "templates"
    # folder as second argument.
    elif new_file is not None:
        # Checking if template file to use exists.
        # In this scenario, "file_to_use" argument refers to the template
        # file in "~/.TextFileTemplates" to create a new file.
        try:
            with open(f'{path}{file_to_use}') as f:
                template = f.read()
        except FileNotFoundError:
            click.echo('ERROR: The template file do not exist.')
            return None

        # Checking if the new file created with the template already exist.
        # In this scenario, "file_to_create" argument refers to the new
        # file created with the template and can be a path to a file too.
        # The new file is created if don't exist or if exist but the
        # "--override" option is set.
        file_exist = os.path.isfile(file_to_create)
        if file_exist and override is None:
            click.echo(f'ERROR: "{file_to_create}" already exist.')
            click.echo('\tTo override an existing file use "--override" option.')
            return None
        elif (file_exist and override) or not file_exist:
            with open(f'{file_to_create}', f'{"w" if override else "x"}') as f:
                click.echo(f'{"Overriding" if override else "Creating new file"} "{file_to_create}"...')
                f.write(template)
        
    click.echo('\nAll executed.')
    return None


@template.command()
def list():
    '''Lists the existing templates.'''

    click.echo('TEMPLATES:')
    popet_object = subprocess.Popen(['ls', path], stdout=subprocess.PIPE)  # The output as a Popet object. 
    output_tuple = popet_object.communicate()  # This returns a tuple with the output of the command itself and the errors.
    templates = str(output_tuple[0]).split('\'')
    templates = templates[1].split(r'\n')

    for template in templates:
        if template:
            click.echo(f'- {template}')

    return None


if __name__ == '__main__':
    template()

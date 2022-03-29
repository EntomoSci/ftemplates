'''2022/03/29 by PianisT
This terminal application creates text files bases on templates.'''


import os
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


@template.command()
@click.option('--new_template', is_flag=True, default=None, help='Create a new template')
@click.option('--new_file', is_flag=True, default=True, help='Create file using an existing template')
@click.argument('file_to_use', required=True)
@click.argument('file_to_create', required=True)
def create(new_template, new_file, file_to_use, file_to_create):
    '''Creates a new template or a new file using an existing template.'''

    # If the "--new_template" flag is used, the program checks if already exist a file
    # with the name given by the argument. If not exist, creates the new template in the
    # "templates" folder of this project.
    if new_template:
        # Checks if the file to use for create the new template exist.
        try:
            with open(file_to_use, 'r') as f:
                template = f.read()
        except FileNotFoundError:
            click.echo(f'The file to use "{file_to_use}" do not exist.')
            return None

        # Checks if the template file to create already exist.
        try: 
            with open(f'{path}{file_to_create}') as f:
                pass 
        except FileNotFoundError:
            click.echo(f'Creating new template "{file_to_create}"...')
            with open(f'{path}{file_to_create}', 'x') as template_to_create:
                template_to_create.write(template) 
            click.echo(f'"{file_to_create}" successfully created!')
            click.echo(f'"{file_to_create}" is now available to use as a template for new text files.')
        else:
            click.echo(f'A file with name "{file_to_create}" already exist.')
            return None
        finally:
            click.echo('All executed.')
                    
    # if the "--new_file" flag is used, the program creates a new file in the path given by
    # the argument passed (default is current directory) using a template from the "templates"
    # folder as second argument.
    elif new_file is not None:
        pass


if __name__ == '__main__':

    
    template()

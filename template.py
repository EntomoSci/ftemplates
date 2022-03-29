'''2022/03/29 by PianisT
This terminal application creates text files bases on templates.'''


from datetime import date
from email.policy import default

import click


@click.group()
def template():
    pass


@click.option('--new_template', is_flag=True, help='Create a new template')
@click.option('--new_file', is_flag=True, help='Create file using an existing template')
@click.argument('arg1', required=True)
@click.argument('arg2', required=True)
def create(new_template, new_file, arg1, arg2):
    '''Creates a new template or file using an existing template.'''

    # If the "--new_template" flag is used, the program checks if already exist a file
    # with the name given by the argument. If not exist, creates the new template in the
    # "templates" folder of this project.
    if new_template is not None:
        file_name = arg1 #input('File path to use as template: ')
        try:
            with open(file_name) as f:
                template = f.read()
        except FileNotFoundError:
            click.echo('The file do not exist.')
            return None
        else:
            while True:
                template_name = arg2 #input('Template name: ')
                try: 
                    with open(f'./templates/{template_name}') as f:
                        pass 
                except FileNotFoundError:
                    click.echo(f'Creating new template "{template_name}"...')
                    with open(f'./templates/{template_name}', 'w') as f:
                        f.write(template) 
                    click.echo(f'"{template_name}" successfully created!')
                    click.echo(f'"{template_name}" is now available to use as a template for new text files.')
                else:
                    click.echo(f'A file with name "{template_name}" already exist.')
                    return None
        finally:
            click.echo('All executed.\n')
                    
    # if the "--new_file" flag is used, the program creates a new file in the path given by
    # the argument passed (default is current directory) using a template from the "templates"
    # folder as second argument.
    if new_file is not None:
        pass


if __name__ == '__main__':
    template()

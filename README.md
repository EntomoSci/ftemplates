# templates

A CLI application to create files with templates.


## Abstract

This project is a command-line interface application that allows you to create your own templates for any kind of file
and use them to create new files easily with a few commands.

## Rationale

Many times the files we use follows some kind of pattern or predefined structure. Sometimes we end up writing that
structure ourselves to frame better some workflow. Those structures driven by conventions or personal preferences
commonly stay the same or change slowly. Writing them over and over again is tedious and inconsistent. Instead of
relying in our busy memory to rebuild the structure of some `.ipynb` or `README` files who been handy in the past,
automate the process with templates and a CLI.

## Installation

1. Create a local copy of the repository:
```console
git clone git@github.com:smv7/templates.git
```

2. Navigate to the package directory and install the package with `pip`:
```console
pip install .
```

## Usage

In the terminal run `template` or `template --help` to know what to do. From there all its functionality should be easy
to use.

## Examples

```console
// List all available templates.
$ template list  

// Create new file using a template.
$ template create --new-file python_template.py new_file.py

// Create new template using a file.
$ template create --new-template file4template.ipynb notebook_template.ipynb

// Override template with new template.
$ template create --new-template --override updated_file4template.md markdown_template.md
```

## Q&A

<details>
<summary>What was your personal motivation to create this project?</summary>

I create this project to create jupyter notebook files (`.ipynb`) with a custom structure to frame data science
workflows better. The structure of the file was already developed by me (you can find it as the
`data_science_notebook.ipynb` built-in template), but copying and pasting the file manually over and over was
suboptimal. *"I want to create notebooks with predefined structure with a simple command"* gave birth this project.
</details>

<details>
<summary>Why the names of the commands and built-in templates are too long and explicit?</summary>

The project try to be as clear as possible enforcing legibility and intuitive usage. Reading it will be beneficial
for understanding. Typing it will be a curse, so make your own 2-4 character aliases, write them once and understand
them whenever you read them with a single look. Therefore both things will be meeting their purposes: self-documented
commands giving legibility and aliases giving practicality.
</details>

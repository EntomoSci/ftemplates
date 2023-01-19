# templates

A CLI application to create files with templates.


## Abstract

This project is a command-line interface application that allows you to create your own templates for any kind of file
and use them to create new files easily with a few commands.

## Rationale

Many times the files we use follows some kind of pattern or predefined structure. Sometimes we end up writting that
structure ourselves to frame better some workflow. Those structures driven by conventions or personal preferences
commonly stay the same or change slowly. Writting them over and over again is tedious and inconsistent. Instead of
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
$ template create --new-file python_template.py myfile.py

// Create new template using a file.
$ template create --new-template my_notebook_template.ipynb new_notebook_template.ipynb

// Override template with new template.
$ template create --new-template --override updated_markdown_template.md deprecated_markdown_template.md
```

## Q&A

<details>
<summary>What was your personal motivation to create this project?</summary>

I create this project to create jupyter notebook files (`.ipynb`) with a custom structure to frame data science
workflows better. The structure of the file was already developed by me (you can find it as the `ds-ipynb` built-in
template), but copying and pasting the file manually over and over was suboptimal.
*"I want to create notebooks with predefined structure with a simple command"* gave birth this project.
</details>

import json
import os


def save_output_to_ipynb_notebook(notebook_name=None, output_code=None):
    """
    This function takes the output code and puts it as the last cell in a jupyter notebook
    :param notebook_name:
    :param output_code:
    :return:
    """
    if notebook_name is None:
        notebook_name = 'output.ipynb'
    if output_code is None:
        output_code = 'print("Hello World")'

    if os.path.exists(notebook_name):
        with open(notebook_name, 'r') as f:
            notebook = json.load(f)
    else:
        notebook = {
            "cells": [],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "codemirror_mode": {
                        "name": "ipython",
                        "version": 3
                    },
                    "file_extension": ".py",
                    "mimetype": "text/x-python",
                    "name": "python",
                    "nbconvert_exporter": "python",
                    "pygments_lexer": "ipython3",
                    "version": "3.7.3"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 2
        }

    cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            output_code
        ]
    }
    notebook['cells'].append(cell)

    with open(notebook_name, 'w') as f:
        json.dump(notebook, f)


if __name__ == '__main__':
    save_output_to_ipynb_notebook(notebook_name='output.ipyb')


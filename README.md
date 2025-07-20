# Sales Analytics

This project aims to provide insights about sales using a local dataset in "data" folder

The insights are:
-
- Profits by each category
- Profits by each subcategory

The result of those insights will then be compiled into a .pdf file.

## Tecnologies

- **Python 3**: Programming language used in this analytics.
- **Matplotlib**: Plotting library used to generate charts.
- **fpdf2**: PDF creation library used to generate the report with charts.

## Generating the Analytics

To generate the analytics, first is necessary to have python and all necessary libraries installed. You should use [pip](https://pypi.org/project/pip/) for this project. Steps to install dependencies from a requirements.txt file can be found [here](https://pip.pypa.io/en/stable/getting-started/#install-multiple-packages-using-a-requirements-file).

> Before proceeding, is necessary to have a basic understanding of how to use a terminal and do packages installation.

You can verify the existence of Python in your system with the following command:

```bash
python --version
```

It should print the installed version of Python, if it is not installed, you can install from [here](https://www.python.org/downloads/).

After the installation of Python is done, we need to ensure that Git is also installed, you can do that with the following command:

```bash
git -v
```

It should shows the installed version of Git, if not installed, you can install Git from [here](https://git-scm.com/downloads).

After Git, Python and the dependencies are installed, you can run the following command in the terminal to download this project:

```bash
git clone https://github.com/LucasTody3535/sales-analytics.git
```

Enter the project directory with the command:

```bash
cd sales-analytics
```

And generate the analytics with:

```bash
python ./main.py # Or 'python .\main.py' in Powershell
```

The analytics will be generated and a browser will be opened with the generated .pdf file located in the **out** folder. An example output can be found in the **example** folder.

## Running the tests

> More tests will be added as the analytics evolve.

Some steps from the previous section applies, only the last one is changed. The command to run the tests is:

```bash
python ./tests/main.py # Or 'python .\tests\main.py' in Powershell
```

## TODO

<ol>
    <li>
        <p>
            Implement tests for existing code.
        </p>
    </li>
    <li>
        <p>
            Add output example and usage tutorial.
        </p>
    </li>
    <li>
        <p>
            Add more analytics from dataset.
        </p>
    </li>
</ol>

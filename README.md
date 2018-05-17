RealEstate
==============================

Webcrawling for real estate analysis

Setting up
----------
This process assumes that you are using conda for creating a virtual environment. Alternatively `virtualenv` could be used.

Create a new empty project:

`conda create -n myproject`

Activate the environment:

`conda activate myproject`

Install the default dependencies (same for all projects):

`make requirements`

To install a single package:

`conda install apackage`

Export the environment so that it can be used to set up the project on another machine:

`conda env export > environment.yml`

On the new machine, create the project environment from the blueprint:

`conda env create -f environment.yml`

Setting up using the makefiles
----
```
rikard@rikard4ubuntu:~/WORK/realestate$ make create_environment 
>>> Detected conda, creating conda environment.
conda create --name realestate python=3
Solving environment: done

## Package Plan ##

  environment location: /home/rikard/anaconda3/envs/realestate

  added / updated specs: 
    - python=3


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    wheel-0.31.1               |           py36_0          62 KB

The following NEW packages will be INSTALLED:

    ca-certificates: 2018.03.07-0           
    certifi:         2018.4.16-py36_0       
    libedit:         3.1.20170329-h6b74fdf_2
    libffi:          3.2.1-hd88cf55_4       
    libgcc-ng:       7.2.0-hdf63c60_3       
    libstdcxx-ng:    7.2.0-hdf63c60_3       
    ncurses:         6.1-hf484d3e_0         
    openssl:         1.0.2o-h20670df_0      
    pip:             10.0.1-py36_0          
    python:          3.6.5-hc3d631a_2       
    readline:        7.0-ha6073c6_4         
    setuptools:      39.1.0-py36_0          
    sqlite:          3.23.1-he433501_0      
    tk:              8.6.7-hc745277_3       
    wheel:           0.31.1-py36_0          
    xz:              5.2.3-h5e939de_4       
    zlib:            1.2.11-ha838bed_2      

Proceed ([y]/n)? y


Downloading and Extracting Packages
wheel-0.31.1         |   62 KB | ##################################################################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate realestate
#
# To deactivate an active environment, use
#
#     $ conda deactivate

>>> New conda env created. Activate with:
source activate realestate
rikard@rikard4ubuntu:~/WORK/realestate$ 
```
`source activate realestate`
`make requirements`
`conda env export > environment.yml`

(https://blog.godatadriven.com/how-to-start-a-data-science-project-in-python)
pip install cookiecutter
cookiecutter https://github.com/drivendata/cookiecutter-data-science
conda install scrapy
cd src/data/
scrapy startproject realestatescraper
cd realestatescraper/realestatescraper/spiders
scrapy genspider housing www.homegate.ch
(edit housing.py, items.py)
scrapy crawl --nolog housing

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

Code style guide
----
Use the [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html).

Automatically format code to PEP8 style:

`autopep8 --in-place --aggressive foo.py`

Run a linter on the code to catch unused import etc:

`flake8 foo.py`

...then edit the code and repeat until there are no suggested improvements.

To run the linter on all code in the project, you can run

`make lint`

Main
----
In Python, pydoc as well as unit tests require modules to be importable. Your code should always check if `__name__ == '__main__'` before executing your main program so that the main program is not executed when the module is imported.
```
def main():
      ...

if __name__ == '__main__':
    main()
```
All code at the top level will be executed when the module is imported. Be careful not to call functions, create objects, or perform other operations that should not be executed when the file is being pydoced.


Code documentation
----

The code should be documented with comments.

 A function must have a docstring, unless it meets all of the following criteria:
- not externally visible
- very short
- obvious

Functions and methods should clearly document what they do,
what arguments they expect, and what they return. Example below:
```
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass
```

Project documentation
-----
The `docs` folder contains source files for making project documentation in various formats. For example, to generate documentation as `html` files, you would use:
```
cd docs
make html
```
The resulting html files are found in `_build/html`.

Changes
---
### Makefile:
#### To capture arguments for "make data"
args = $(filter-out $@,$(MAKECMDGOALS))

#### Make Dataset
data: requirements
	$(PYTHON_INTERPRETER) src/data/make_dataset.py ${args}
%:
    @:

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

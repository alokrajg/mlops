## 1. Create creating a virtual/conda environment
> conda create -n env_name python=3.9

> conda activate env_name

## 2. Install required python packages
> pip install -r requirement.txt

## 3. Configurations

```
    config/
    ├── args.json       - arguments
    └── config.py       - configuration setup
```
Inside *config.py*, we'll add the code to define key directory locations (we'll add more configurations in later lessons as they're needed)

and inside *args.json*, we'll add the parameters that are relevant to data processing and model training.

## 4. Operations

```
text_tagging/
└── main.py       - training/optimization pipelines
```
We'll define these core operations inside main.py as we move code from notebooks to the appropriate scripts below:

    elt_data: extract, load and transform data.
    optimize: tune hyperparameters to optimize for objective.
    train_model: train a model using best parameters from optimization study.
    load_artifacts: load trained artifacts from a given run.
    predict_tag: predict a tag for a given input.

## 5. Utilities
```
text_tagging/
├── main.py       - training/optimization pipelines
└── utils.py      - supplementary utilities
```

## 6. Project
When it comes to migrating our code from notebooks to scripts, it's best to organize based on utility. For example, we can create scripts for the various stages of ML development such as data processing, training, evaluation, prediction, etc.:

```
text_tagging/
├── data.py       - data processing utilities
├── evaluate.py   - evaluation components
├── main.py       - training/optimization pipelines
├── predict.py    - inference utilities
├── train.py      - training utilities
└── utils.py      - supplementary utilities

```

## 7. Documentation
1. Install required packages:
 *setup.py*
```
docs_packages = [
    "mkdocs==1.3.0",
    "mkdocstrings==0.18.1"
]

Define our package:
setup(
    ...
    install_requires=[required_packages],
    extras_require={
        "dev": docs_packages,
        "docs": docs_packages,
    },
)

```
Now we can install this package with:
> python3 -m pip install -e ".[docs]"

> python3 -m pip install -e ".[dev]"

2. Initialize mkdocs
> python3 -m mkdocs new .
```
.
├─ docs/
│  └─ index.md
└─ mkdocs.yml
```
3. Next we'll create documentation files for each script in our text_tagging directory:

```
mkdir docs/text_tagging
cd docs/text_tagging
touch main.md utils.md data.md train.md evaluate.md predict.md
cd ../../
```
4. Next we'll add text_tagging.<SCRIPT_NAME> to each file under docs/text_tagging.
```
# docs/text_tagging/data.md
::: text_tagging.data
```
5. Finally, we'll add some configurations to our mkdocs.yml file that mkdocs automatically created:

```
# mkdocs.yml
site_name: TEXT TAGGING
nav:
  - Home: index.md
  - workflows:
    - main: text_tagging/main.md
  - tagifai:
    - data: text_tagging/data.md
    - evaluate: text_tagging/evaluate.md
    - predict: text_tagging/predict.md
    - train: text_tagging/train.md
    - utils: text_tagging/utils.md
theme: readthedocs
plugins:
  - mkdocstrings
watch:
  - .  # reload docs for any file changes
```

6. Serve our documentation locally:
> python3 -m mkdocs serve

## 7. Styling and Formatting
Style and formatting conventions to keep our code looking consistent.

**1. Tools**

    Black: an in-place reformatter that (mostly) adheres to PEP8.
    isort: sorts and formats import statements inside Python scripts.
    flake8: a code linter with stylistic conventions that adhere to PEP8.

```
# setup.py
style_packages = [
    "black==22.3.0",
    "flake8==3.9.2",
    "isort==5.10.1"
]

# Define our package
setup(
    ...
    extras_require={
        "dev": docs_packages + style_packages,
        "docs": docs_packages,
    },
)
```
**2. Configuration**

> touch pyproject.toml
```
# Black formatting
[tool.black]
line-length = 100
include = '\.pyi?$'
exclude = '''
/(
      .eggs         # exclude a few common directories in the
    | .git          # root of the project
    | .hg
    | .mypy_cache
    | .tox
    | venv
    | _build
    | buck-out
    | build
    | dist
  )/
'''
```
```
# iSort
[tool.isort]
profile = "black"
line_length = 79
multi_line_output = 3
include_trailing_comma = true
virtual_env = "venv"
```
For Flake:
>touch .flake8
```
[flake8]
exclude = venv
ignore = E501, W503, E226
max-line-length = 79

# E501: Line too long
# W503: Line break occurred before binary operator
# E226: Missing white space around arithmetic operator
```
**3. Usage**
```
black .
flake8
isort .
```

## 8. Makefiles
An automation tool that organizes commands for our application's processes.
>touch Makefile

```
# Styling
.PHONY: style
style:
    black .
    flake8
    isort .
```
```
# Cleaning
.PHONY: clean
clean: style
    find . -type f -name "*.DS_Store" -ls -delete
    find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
    find . | grep -E ".pytest_cache" | xargs rm -rf
    find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
    find . | grep -E ".trash" | xargs rm -rf
    rm -f .coverage
```
```
# Environment
.ONESHELL:
venv:
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install pip setuptools wheel
    python3 -m pip install -e .
```
```
.PHONY: help
help:
    @echo "Commands:"
    @echo "venv    : creates a virtual environment."
    @echo "style   : executes style formatting."
    @echo "clean   : cleans all unnecessary files."
```
> make venv

> make style

> make clean


## 9. FastAPI
```
app/
├── api.py          - FastAPI app
├── gunicorn.py     - WSGI script
└── schemas.py      - API model schemas
```
    api.py: the main script that will include our API initialization and endpoints.
    gunicorn.py: script for defining API worker configurations.
    schemas.py: definitions for the different objects we'll use in our resource endpoints.

>uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload --reload-dir text_tagging --reload-dir app  # dev

>gunicorn -c app/gunicorn.py -k uvicorn.workers.UvicornWorker app.api:app  # prod

## 10. Testing
**1. Test Code**
```
mkdir tests
cd tests
mkdir code
touch <SCRIPTS>
cd ../
```

test directory
```
tests/
└── code/
│   ├── test_data.py
│   ├── test_evaluate.py
│   ├── test_main.py
│   ├── test_predict.py
│   └── test_utils.py
```
Add test packages in setup.py
```
# setup.py
test_packages = [
    "pytest==7.1.2",
    "pytest-cov==2.10.1"
]

# Define our package
setup(
    ...
    extras_require={
        "dev": docs_packages + style_packages + test_packages,
        "docs": docs_packages,
        "test": test_packages,
    },
)
```
Configuration
```
# Pytest
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
addopts = "--strict-markers --disable-pytest-warnings"
markers = [
    "training: tests that involve training",
]

# Pytest coverage Exclusions
[tool.coverage.run]
omit = ["app/gunicorn.py"]
```
**Execution**

all tests
>python3 -m pytest

tests under a directory
>python3 -m pytest tests/food

Coverage
> python3 -m pytest --cov text_tagging --cov-report html

**2. Test Data**

```
# setup.py
test_packages = [
    "pytest==7.1.2",
    "pytest-cov==2.10.1",
    "great-expectations==0.15.15"
]
```
1. Projects

>cd tests

>great_expectations init

This will set up a tests/great_expectations directory with the following structure:
```
tests/great_expectations/
├── checkpoints/
├── expectations/
├── plugins/
├── uncommitted/
├── .gitignore
└── great_expectations.yml
```
2. Data source

The first step is to establish our datasource which tells Great Expectations where our data lives:
>great_expectations datasource new
```
What data would you like Great Expectations to connect to?
    1. Files on a filesystem (for processing with Pandas or Spark) 👈
    2. Relational database (SQL)

What are you processing your files with?
1. Pandas 👈
2. PySpark

Enter the path of the root directory where the data files are stored: ../data
```
3. Suites

Create expectations manually, interactively or automatically and save them as suites (a set of expectations for a particular data asset).

>great_expectations suite new

```
How would you like to create your Expectation Suite?
    1. Manually, without interacting with a sample batch of data (default)
    2. Interactively, with a sample batch of data 👈
    3. Automatically, using a profiler

Which data asset (accessible by data connector "default_inferred_data_connector_name") would you like to use?
    1. labeled_projects.csv
    2. projects.csv 👈
    3. tags.csv

Name the new Expectation Suite [projects.csv.warning]: projects
```
Define expectations in jupyter notebook:
```
Table expectations:

# Presence of features
validator.expect_table_columns_to_match_ordered_list(column_list=["id", "tag"])

Column expectations:
# id
validator.expect_column_values_to_be_unique(column="id")

# tag
validator.expect_column_values_to_not_be_null(column="tag")
validator.expect_column_values_to_be_of_type(column="tag", type_="str")
```
To edit a suite, we can execute the follow CLI command:

>great_expectations suite edit <SUITE_NAME>

4. Checkpoints
```
great_expectations checkpoint new projects
great_expectations checkpoint new tags
great_expectations checkpoint new labeled_projects
```
We have to change the lines for data_asset_name (which data asset to run the checkpoint suite on) and expectation_suite_name (name of the suite to use). For example, the projects checkpoint would use the projects.csv data asset and the projects suite.

```
great_expectations checkpoint run projects
great_expectations checkpoint run tags
great_expectations checkpoint run labeled_projects
```
5. Documentation
>great_expectations docs build

**3. Test Model**

The final aspect of testing ML systems involves how to test machine learning models during training, evaluation, inference and deployment. [Behavioral testing]

### Makefile

Let's create a target in our Makefile that will allow us to execute all of our tests with one call:
```
# Test
.PHONY: test
test:
    pytest -m "not training"
    cd tests && great_expectations checkpoint run projects
    cd tests && great_expectations checkpoint run tags
    cd tests && great_expectations checkpoint run labeled_projects
```
> make test



# Workflow
```
python main.py elt-data
python main.py optimize --args-fp="config/args.json" --study-name="optimization" --num-trials=10
python main.py train-model --args-fp="config/args.json" --experiment-name="baselines" --run-name="sgd"
python main.py predict-tag --text="Transfer learning with transformers for text classification."

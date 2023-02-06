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




# Workflow

```
python main.py elt-data
python main.py optimize --args-fp="config/args.json" --study-name="optimization" --num-trials=10
python tmain.py train-model --args-fp="config/args.json" --experiment-name="baselines" --run-name="sgd"
python main.py predict-tag --text="Transfer learning with transformers for text classification."


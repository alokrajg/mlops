import json
import numpy as np
import random

def load_dict(filepath):
    """Load a dictionary from a JSON's filepath."""
    with open(filepath, "r") as fp:
        d = json.load(fp)
    return d

def save_dict(d, filepath, cls=None, sortkeys=False):
    """Save a dictionary to a specific location."""
    with open(filepath, "w") as fp:
        json.dump(d, indent=2, fp=fp, cls=cls, sort_keys=sortkeys)

def set_seeds(seed=42):
    """Set seed for reproducibility."""
    # Set seeds
    np.random.seed(seed)
    random.seed(seed)

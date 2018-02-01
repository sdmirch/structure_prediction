import numpy as np
from collections import Counter

def model_RandomClass(y):
    """
    Predicts classes randomly based on class distribution in given label vector y.

    Args:
        y (arr): array or list of classes.

    Returns:
        predictions (arr): array of random predictions
    """

    classes = []
    probabilities = []
    c = Counter(y)
    for k, v in c.iteritems():
        classes.append(k)
        probabilities.append(v*1.0/len(y))

    predictions=np.random.choice(classes,size=len(y),replace=True,p=probabilities)

    return predictions

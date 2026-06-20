from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ModelMetrics:
    name: str
    accuracy: float
    precision: float
    recall: float

def compare_models(model1: ModelMetrics, model2: ModelMetrics) -> Dict[str, str]:
    comparison = {}
    if model1.accuracy > model2.accuracy:
        comparison['accuracy'] = f"{model1.name} is better"
    elif model1.accuracy < model2.accuracy:
        comparison['accuracy'] = f"{model2.name} is better"
    else:
        comparison['accuracy'] = "Both models are equal"

    if model1.precision > model2.precision:
        comparison['precision'] = f"{model1.name} is better"
    elif model1.precision < model2.precision:
        comparison['precision'] = f"{model2.name} is better"
    else:
        comparison['precision'] = "Both models are equal"

    if model1.recall > model2.recall:
        comparison['recall'] = f"{model1.name} is better"
    elif model1.recall < model2.recall:
        comparison['recall'] = f"{model2.name} is better"
    else:
        comparison['recall'] = "Both models are equal"

    return comparison

def get_best_model(models: List[ModelMetrics]) -> ModelMetrics:
    best_model = models[0]
    for model in models[1:]:
        if model.accuracy > best_model.accuracy:
            best_model = model
    return best_model

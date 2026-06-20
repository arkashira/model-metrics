import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Metric:
    name: str
    value: float

@dataclass
class LLMProvider:
    name: str
    metrics: List[Metric]

class ModelMetrics:
    def __init__(self):
        self.providers = {}

    def add_provider(self, provider: LLMProvider):
        self.providers[provider.name] = provider.metrics

    def get_metrics(self, provider_name: str) -> List[Metric]:
        return self.providers.get(provider_name, [])

    def calculate_average(self, provider_name: str, metric_name: str) -> float:
        metrics = self.get_metrics(provider_name)
        metric_values = [metric.value for metric in metrics if metric.name == metric_name]
        if not metric_values:
            raise ValueError(f"No metrics found for {provider_name} with name {metric_name}")
        return round(sum(metric_values) / len(metric_values), 2)

    def to_json(self) -> str:
        data = {name: [metric.__dict__ for metric in metrics] for name, metrics in self.providers.items()}
        return json.dumps(data)

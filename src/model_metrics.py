import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class ProviderConfig:
    endpoint: str
    credentials: Dict[str, str]

class ModelMetrics:
    def __init__(self, providers: Dict[str, ProviderConfig]):
        self.providers = providers

    def get_provider(self, provider_name: str) -> ProviderConfig:
        if provider_name not in self.providers:
            raise ValueError(f"Provider {provider_name} not found")
        return self.providers.get(provider_name)

    def get_metrics(self, provider_name: str, model_name: str) -> Dict[str, str]:
        provider = self.get_provider(provider_name)
        # Simulate a request to the provider endpoint
        # In a real implementation, you would make an HTTP request here
        return {"metric1": "value1", "metric2": "value2"}

    def compare_providers(self, model_name: str) -> Dict[str, Dict[str, str]]:
        metrics = {}
        for provider_name, provider in self.providers.items():
            metrics[provider_name] = self.get_metrics(provider_name, model_name)
        return metrics

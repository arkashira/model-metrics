import pytest
from model_metrics import ModelMetrics, ProviderConfig

def test_get_provider():
    providers = {
        "OpenAI": ProviderConfig("https://api.openai.com", {"api_key": "key1"}),
        "Anthropic": ProviderConfig("https://api.anthropic.com", {"api_key": "key2"}),
    }
    model_metrics = ModelMetrics(providers)
    assert model_metrics.get_provider("OpenAI").endpoint == "https://api.openai.com"

def test_get_metrics():
    providers = {
        "OpenAI": ProviderConfig("https://api.openai.com", {"api_key": "key1"}),
    }
    model_metrics = ModelMetrics(providers)
    metrics = model_metrics.get_metrics("OpenAI", "model1")
    assert metrics == {"metric1": "value1", "metric2": "value2"}

def test_compare_providers():
    providers = {
        "OpenAI": ProviderConfig("https://api.openai.com", {"api_key": "key1"}),
        "Anthropic": ProviderConfig("https://api.anthropic.com", {"api_key": "key2"}),
    }
    model_metrics = ModelMetrics(providers)
    metrics = model_metrics.compare_providers("model1")
    assert metrics["OpenAI"] == {"metric1": "value1", "metric2": "value2"}
    assert metrics["Anthropic"] == {"metric1": "value1", "metric2": "value2"}

def test_get_provider_not_found():
    providers = {
        "OpenAI": ProviderConfig("https://api.openai.com", {"api_key": "key1"}),
    }
    model_metrics = ModelMetrics(providers)
    with pytest.raises(ValueError):
        model_metrics.get_provider("Azure")

def test_get_metrics_provider_not_found():
    providers = {
        "OpenAI": ProviderConfig("https://api.openai.com", {"api_key": "key1"}),
    }
    model_metrics = ModelMetrics(providers)
    with pytest.raises(ValueError):
        model_metrics.get_metrics("Azure", "model1")

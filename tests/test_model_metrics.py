from model_metrics import ModelMetrics, LLMProvider, Metric
import pytest

def test_add_provider():
    model_metrics = ModelMetrics()
    provider = LLMProvider("LLM1", [Metric("accuracy", 0.9), Metric("f1", 0.8)])
    model_metrics.add_provider(provider)
    assert model_metrics.get_metrics("LLM1") == provider.metrics

def test_get_metrics():
    model_metrics = ModelMetrics()
    provider = LLMProvider("LLM1", [Metric("accuracy", 0.9), Metric("f1", 0.8)])
    model_metrics.add_provider(provider)
    assert model_metrics.get_metrics("LLM1") == provider.metrics

def test_calculate_average():
    model_metrics = ModelMetrics()
    provider = LLMProvider("LLM1", [Metric("accuracy", 0.9), Metric("accuracy", 0.8)])
    model_metrics.add_provider(provider)
    assert model_metrics.calculate_average("LLM1", "accuracy") == 0.85

def test_calculate_average_no_metrics():
    model_metrics = ModelMetrics()
    provider = LLMProvider("LLM1", [Metric("accuracy", 0.9)])
    model_metrics.add_provider(provider)
    with pytest.raises(ValueError):
        model_metrics.calculate_average("LLM1", "f1")

def test_to_json():
    model_metrics = ModelMetrics()
    provider = LLMProvider("LLM1", [Metric("accuracy", 0.9), Metric("f1", 0.8)])
    model_metrics.add_provider(provider)
    expected_json = '{"LLM1": [{"name": "accuracy", "value": 0.9}, {"name": "f1", "value": 0.8}]}'
    assert model_metrics.to_json() == expected_json

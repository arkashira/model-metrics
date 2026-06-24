from model_metrics import ModelMetrics, BenchmarkSuite
import pytest

def test_create_suite():
    metrics = ModelMetrics()
    results = {"accuracy": 0.9}
    suite_id = metrics.create_suite(results)
    assert suite_id in metrics.suites
    assert metrics.suites[suite_id].results == results

def test_generate_share_link():
    metrics = ModelMetrics()
    results = {"accuracy": 0.9}
    suite_id = metrics.create_suite(results)
    link = metrics.generate_share_link(suite_id)
    assert link.startswith("https://example.com/")

def test_get_results():
    metrics = ModelMetrics()
    results = {"accuracy": 0.9}
    suite_id = metrics.create_suite(results)
    token = metrics.generate_share_link(suite_id).split("/")[-1]
    assert metrics.get_results(suite_id, token) == results

def test_get_results_invalid_token():
    metrics = ModelMetrics()
    results = {"accuracy": 0.9}
    suite_id = metrics.create_suite(results)
    with pytest.raises(ValueError):
        metrics.get_results(suite_id, "invalid_token")

def test_revoke_link():
    metrics = ModelMetrics()
    results = {"accuracy": 0.9}
    suite_id = metrics.create_suite(results)
    token = metrics.generate_share_link(suite_id).split("/")[-1]
    metrics.revoke_link(suite_id, token)
    with pytest.raises(ValueError):
        metrics.get_results(suite_id, token)

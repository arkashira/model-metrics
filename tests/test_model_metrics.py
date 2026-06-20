from model_metrics import ModelMetrics, compare_models, get_best_model

def test_compare_models():
    model1 = ModelMetrics("Model 1", 0.9, 0.8, 0.7)
    model2 = ModelMetrics("Model 2", 0.8, 0.9, 0.6)
    comparison = compare_models(model1, model2)
    assert comparison['accuracy'] == "Model 1 is better"
    assert comparison['precision'] == "Model 2 is better"
    assert comparison['recall'] == "Model 1 is better"

def test_compare_models_equal():
    model1 = ModelMetrics("Model 1", 0.9, 0.8, 0.7)
    model2 = ModelMetrics("Model 2", 0.9, 0.8, 0.7)
    comparison = compare_models(model1, model2)
    assert comparison['accuracy'] == "Both models are equal"
    assert comparison['precision'] == "Both models are equal"
    assert comparison['recall'] == "Both models are equal"

def test_get_best_model():
    model1 = ModelMetrics("Model 1", 0.9, 0.8, 0.7)
    model2 = ModelMetrics("Model 2", 0.8, 0.9, 0.6)
    model3 = ModelMetrics("Model 3", 0.7, 0.6, 0.5)
    models = [model1, model2, model3]
    best_model = get_best_model(models)
    assert best_model.name == "Model 1"

def test_get_best_model_single():
    model1 = ModelMetrics("Model 1", 0.9, 0.8, 0.7)
    models = [model1]
    best_model = get_best_model(models)
    assert best_model.name == "Model 1"

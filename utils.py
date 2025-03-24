# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

# ML model evaluation
def evaluate_model(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return mae, rmse

# Plot feature importance
def plot_feature_importance(model, model_name, feature_names):
    if model_name.lower() == 'xgboost':
        feature_importances = model.feature_importances_
    elif model_name.lower() == 'random forest':
        feature_importances = model.feature_importances_
    elif model_name.lower() == 'catboost':
        feature_importances = model.get_feature_importance()
    else:
        raise ValueError("Unsupported model type")

    plt.figure(figsize=(10, 6))
    plt.barh(feature_names, feature_importances)
    plt.title(f'{model_name} Feature Importance')
    plt.xlabel('Importance')
    plt.show()


# Plot learning curves
def plot_learning_curve(model, model_name, X_train, y_train, X_val, y_val):
    train_sizes = np.linspace(0.1, 1.0, 10)
    train_errors = []
    val_errors = []

    for train_size in train_sizes:
        sample_size = int(train_size * len(X_train))
        X_train_sample = X_train[:sample_size]
        y_train_sample = y_train[:sample_size]

        model.fit(X_train_sample, y_train_sample)
        train_pred = model.predict(X_train_sample)
        val_pred = model.predict(X_val)

        train_errors.append(np.sqrt(mean_squared_error(y_train_sample, train_pred)))
        val_errors.append(np.sqrt(mean_squared_error(y_val, val_pred)))

    plt.figure()
    plt.plot(train_sizes, train_errors, label='Training Error')
    plt.plot(train_sizes, val_errors, label='Validation Error')
    plt.title(f'Learning Curve Analysis ({model_name})')
    plt.xlabel('Training Size')
    plt.ylabel('RMSE')
    plt.legend()
    plt.show()
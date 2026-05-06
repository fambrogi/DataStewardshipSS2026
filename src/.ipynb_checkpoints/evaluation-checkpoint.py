
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import json
import os

def compute_metrics(y_true, y_pred):
    return {
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "mae": float(mean_absolute_error(y_true, y_pred))
    }

def save_metrics(metrics_dict, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(metrics_dict, f, indent=4)

def plot_prediction(y_true, y_pred, title, path):
    plt.figure()
    plt.scatter(y_true, y_pred)
    plt.xlabel("True")
    plt.ylabel("Predicted")
    plt.title(title)
    plt.grid(ls=':')
    plt.savefig(path)

def plot_prediction_comparison(x,seq_cd,multi_cd,true_cd, path, title='Pb Model Prediction Comparison'): 
    x = list(range(len(seq_cd)))
    plt.scatter(x,seq_cd, label="Sequential")
    plt.scatter(x,multi_cd, label="Multi")
    plt.scatter(x,true_cd, label="True")
    
    plt.grid(ls=':')
    plt.title(title)
    
    plt.legend()
    plt.savefig(path)


def plot_feature_importance(model, feature_names, path):
    import matplotlib.pyplot as plt
    import pandas as pd

    # Access model inside pipeline
    rf_model = model.named_steps["model"]

    importances = rf_model.feature_importances_
    feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=False)

    plt.figure()
    feat_imp.head(10).plot(kind="bar")
    plt.title("Feature Importance")
    plt.tight_layout()
    plt.grid(ls = ':' , color = 'lightgray')
    plt.savefig(path)

def interactive_plot(x, seq_cd, multi_cd, true_cd):
    import plotly.graph_objects as go
    import plotly.graph_objs as go


    # Create traces
    fig = go.Figure(x, seq_cd, multi_cd, true_cd)
    
    fig.add_trace(go.Scatter(x=x, y=seq_cd,
                        mode='lines',
                        name='Sequential'))
    fig.add_trace(go.Scatter(x=x, y=multi_cd,
                        mode='lines+markers',
                        name='Multi'))
    fig.add_trace(go.Scatter(x=x, y=true_cd,
                        mode='markers', name='True'))

    return fig
    
    #fig.show()

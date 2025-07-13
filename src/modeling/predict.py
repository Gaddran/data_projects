from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import os
import joblib
def predict_model(df, features, target_col, model=None):
    """
    Peedice la variable objetivo utilizando un modelo de Random Forest previamente entrenado.
    Args:
        df (pd.DataFrame): DataFrame que contiene las características.
        features (list): Lista de nombres de columnas que se utilizarán como características.
        model: modelo previamente entrenado. Si es None, se cargará el modelo por defecto.
    """
    if model is None:
        model_path = os.path.join("..", "models", "random_forest_model.joblib")
        model = joblib.load(model_path)
    
    

    X = df[features]
    predictions = model.predict_proba(X)
    preds_labels  = [p[1] for p in predictions.round()]
    f1 = f1_score(df[target_col], preds_labels)
    print(f'F1: {f1}')

    return predictions, f1

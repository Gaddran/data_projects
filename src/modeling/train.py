import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df, features, target_col,n_estimators=100, max_depth=10):
    """
    Entrena un modelo de Random Forest utilizando las características y el objetivo proporcionados.
    Args:
        df (pd.DataFrame): DataFrame que contiene las características y el objetivo.
        features (list): Lista de nombres de columnas que se utilizarán como características.
        target_col (str): Nombre de la columna objetivo.
        n_estimators (int): Número de árboles en el bosque aleatorio.
        max_depth (int): Profundidad máxima de los árboles.
    """   
    X  = df[features]
    y = df[target_col]
    
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X, y)
    joblib.dump(model, os.path.join("..", "models", "random_forest_model.joblib"))
    
    return model
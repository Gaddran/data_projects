## 🛠️ Configuración del entorno

Sigue estos pasos para preparar el entorno y ejecutar el notebook principal.

### 1. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
```
### 2. Activar el entorno virtual
- Linux/macOS:

```bash
source venv/bin/activate
```
- Windows (CMD):

```c
venv\Scripts\activate
```

- Windows (powershell):
```powershell
venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

Asegúrate de estar en el directorio raíz del proyecto (donde está requirements.txt).
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el notebook

```bash
jupyter notebook
```
Luego abre y ejecuta el archivo:

```bash
notebooks/main.ipynb
```

├── data
│   ├── processed
│   │   └── preprocessed.parquet
│   └── raw
│       └── yellow_tripdata_2020-01.parquet
├── models
│   └── random_forest_model.joblib
├── notebooks
│   └── main.ipynb
├── src
│   ├── data
│   │   ├── __pycache__
│   │   ├── dataset.py
│   │   └── __init__.py
│   ├── features
│   │   ├── __pycache__
│   │   ├── build_features.py
│   │   └── __init__.py
│   ├── modeling
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── predict.py
│   │   └── train.py
│   ├── __pycache__
│   │   ├── config.cpython-313.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   └── __init__.cpython-313.pyc
│   ├── visualization
│   │   └── plots.py
│   ├── config.py
│   └── __init__.py
├── __init__.py
├── README.md
└── requirements.txt
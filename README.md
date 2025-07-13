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

```
.
├── data
│   ├── processed
│   │   └── preprocessed.parquet
│   └── raw
│       └── yellow_tripdata_2020-01.parquet
├── __init__.py
├── models
│   └── random_forest_model.joblib
├── notebooks
│   └── main.ipynb
├── README.md
├── requirements.txt
└── src
    ├── config.py
    ├── data
    │   ├── dataset.py
    │   └── __init__.py
    ├── features
    │   ├── build_features.py
    │   └── __init__.py
    ├── __init__.py
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py
    │   └── train.py
    └── visualization
        └── plots.py
```
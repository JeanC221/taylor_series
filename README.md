# 🧮 NuCalc

> Suite de cálculo numérico de precisión para ingeniería y ciencias aplicadas

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

##  Características

**NuCalc** es una aplicación web moderna que proporciona herramientas de cálculo numérico con visualización interactiva:

-  **Series de Taylor** - Aproximación polinómica de funciones con análisis de convergencia
-  **Derivación Numérica** - Cálculo de pendientes mediante diferencias finitas
-  **Búsqueda de Raíces** - Solvers iterativos (Bisección y Newton-Raphson)

##  Demo

```bash
# Clonar el repositorio
git clone https://github.com/JeanC221/taylor_series.git
cd taylor_series

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

Abrir su navegador en `http://127.0.0.1:5000`

##  Tecnologías

- **Backend**: Flask (Python)
- **Cálculo Simbólico**: SymPy
- **Visualización**: Matplotlib
- **Computación Numérica**: NumPy
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Renderizado Matemático**: MathJax

##  Instalación

### Requisitos Previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/JeanC221/taylor_series.git
   cd taylor_series
   ```

2. **Crear un entorno virtual (recomendado)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instalar las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**

   ```bash
   python app.py
   ```

5. **Acceder a la aplicación**

   Abrir tu navegador en: `http://127.0.0.1:5000`

## Uso

### Series de Taylor

Aproximar funciones mediante polinomios de Taylor:

1. Ingresa la función: `cos(x)`, `exp(x)`, `log(x)`, etc.
2. Define el punto de expansión `a`
3. Especifica el orden `n` (número de términos)
4. Establece el punto de evaluación para análisis de error
5. Define el dominio de la gráfica

**Ejemplo:**

- Función: `sin(x)`
- Punto base: `0`
- Orden: `5`
- Evaluación: `1.5`

### Derivación Numérica

Calcular derivadas usando diferencias finitas:

1. Ingresar la función a derivar
2. Especificar el punto de evaluación `x`
3. Definir el paso `h` (típicamente `0.001` - `0.0001`)

**Ejemplo:**

- Función: `x**3`
- Punto: `2`
- Paso: `0.001`

### Búsqueda de Raíces

Encuentra ceros de funciones:

**Método de Bisección:**

- Requiere intervalo `[a, b]` donde `f(a)` y `f(b)` tienen signos opuestos

**Método de Newton-Raphson:**

- Requiere estimación inicial `xi` cercana a la raíz

##  Verificación

Ejecutar el script de verificación para validar la lógica matemática:

```bash
python verify_logic.py
```

##  Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

##  Notas Técnicas

- Las funciones deben usar sintaxis SymPy: `**` para potencias, `*` para multiplicación explícita
- Funciones disponibles: `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, etc.
- Los resultados incluyen métricas de error (absoluto y relativo)

##  Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

##  Autor

**Jean Carlo Herran**

- GitHub: [@JeanC221](https://github.com/JeanC221)

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub

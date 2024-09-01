# Proyecto de Calculadora de Ingeniería
Este proyecto es una aplicación web que ofrece herramientas para cálculos matemáticos avanzados, incluyendo series de Taylor, derivación numérica y búsqueda de raíces, utilizando Python y Flask.

## Funcionalidades
- Cálculo y visualización de series de Taylor
- Derivación numérica
- Búsqueda de raíces utilizando métodos de bisección y Newton

## Requisitos
- Python 3.12 o superior
- Flask 3.0.3
- SymPy 1.9 o superior
- Matplotlib 3.3 o superior
- NumPy 1.19 o superior

## Instalación
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/calculadora_ingenieria.git
   cd calculadora_ingenieria
   ```

2. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

## Uso

### Series de Taylor
1. Selecciona "Series de Taylor" en la página principal.
2. Ingresa la función matemática (ej. sin(x), e^x, x^2).
3. Define el punto de expansión (a).
4. Establece el orden de la serie (n).
5. Ingresa el valor de x para calcular errores.
6. Especifica el intervalo para la gráfica (x mínimo y máximo).
7. Haz clic en "Calcular" para ver los resultados y la gráfica.

### Derivación Numérica
1. Selecciona "Derivación Numérica" en la página principal.
2. Ingresa la función a derivar.
3. Especifica el punto (x) donde calcular la derivada.
4. Define el valor de h (paso para la aproximación numérica).
5. Haz clic en "Calcular" para obtener el resultado.

### Búsqueda de Raíces
1. Selecciona "Búsqueda de Raíces" en la página principal.
2. Elige el método (Bisección o Newton).
3. Ingresa la función para encontrar sus raíces.
4. Para el método de bisección, ingresa los valores iniciales a y b.
5. Para el método de Newton, ingresa el valor inicial xi.
6. Especifica la tolerancia deseada.
7. Haz clic en "Calcular" para encontrar la raíz.

## Notas importantes
- Asegúrate de ingresar las funciones en un formato que el sistema pueda interpretar (ej. usa `**` para potencias, `exp(x)` para e^x).
- Para multiplicaciones explícitas, usa el símbolo `*` (ej. `2*x` en lugar de `2x`).
- Las funciones trigonométricas deben escribirse con paréntesis (ej. `sin(x)`, no `sinx`).

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de hacer un pull request.

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)

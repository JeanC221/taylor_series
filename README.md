# Proyecto de Series de Taylor

Este proyecto es una aplicación web que resuelve y visualiza series de Taylor utilizando Python y Flask.

## Requisitos

- Python 3.12 o superior
- Flask 3.0.3
- SymPy
- Matplotlib
- NumPy

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/taylor_series.git
   
2. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt

3. **Ejecutar la aplicación:**

   ```bash
   python app.py


## Uso

1. **Ingresar Función**:
   - En la página principal, encontrarás un campo para ingresar la función matemática para la cual deseas calcular la serie de Taylor. Asegúrate de ingresar la función en una forma que pueda ser interpretada por el sistema.

2. **Seleccionar Punto**:
   - Define el punto de expansión (a) donde deseas que se calcule la serie de Taylor. Este es el punto alrededor del cual la serie será aproximada.

3. **Seleccionar Orden**:
   - Establece el orden (n) de la serie de Taylor que quieres calcular. El orden determina cuántos términos de la serie se incluirán en la aproximación.

4. **Ver Resultados**:
   - La página mostrará los siguientes resultados:
     - **Serie de Taylor**: La serie de Taylor calculada para la función, el punto de expansión y el orden seleccionados.
     - **Errores**:
       - **Error Absoluto**: La diferencia entre el valor real de la función y la aproximación de Taylor en el punto seleccionado.
       - **Error Relativo**: El error absoluto expresado como porcentaje del valor real de la función.
     - **Gráfica**: Una visualización gráfica que muestra la función original y la aproximación de Taylor para los valores en el intervalo especificado.

Asegúrate de que todos los campos estén correctamente completados antes de hacer clic en el botón para calcular los resultados. La gráfica y los errores se actualizarán automáticamente según los parámetros ingresados.

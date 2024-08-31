from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from io import BytesIO
import base64

app = Flask(__name__)

x = sp.Symbol('x')

class Taylor:
    def __init__(self, f, a, n):
        self.f = f
        self.a = a
        self.n = n

    def taylor(self):
        modelo = 0
        for i in range(self.n + 1):
            modelo += (self.f.diff(x, i).subs(x, self.a) * (x - self.a) ** i) / sp.factorial(i)
        return modelo

    def errores(self, equis):
        valor_teorico = self.f.subs(x, equis).evalf()
        valor_experimental = self.taylor().subs(x, equis).evalf()
        error_absoluto = abs(valor_teorico - valor_experimental)
        error_relativo = abs((valor_teorico - valor_experimental) / valor_teorico) * 100
        return valor_teorico, valor_experimental, error_absoluto, error_relativo

    def grafica(self, intervalo):
        valores_x = np.linspace(min(intervalo), max(intervalo), 100)
        valores_fx = [self.f.subs(x, i) for i in valores_x]
        valores_y = sp.lambdify(x, self.taylor())(valores_x)

        plt.plot(valores_x, valores_fx)
        plt.plot(valores_x, valores_y)
        plt.legend(['f(x)', 'Taylor'])
        plt.grid()
        plt.title('Taylor')
        plt.xlabel('x')
        plt.ylabel('f(x)')

        # Convert plot to PNG image and then to base64 string
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close()
        return plot_url

def derivacion_numerica(f, xi, h):
    return (f(xi + h) - f(xi)) / h

def calculate_error_absoluto(valor_teorico, valor_experimental):
    return abs(valor_teorico - valor_experimental)

def calculate_error_relativo(valor_teorico, valor_experimental):
    return abs(valor_teorico - valor_experimental) / abs(valor_teorico)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    plot_url = None

    if request.method == 'POST':
        if 'expression' in request.form:  # Handle Taylor series calculation
            expression = request.form['expression']
            a_value = float(request.form['a_value'])
            n_value = int(request.form['n_value'])
            x_value = float(request.form['x_value'])
            x_min = float(request.form['x_min'])
            x_max = float(request.form['x_max'])

            f = sp.sympify(expression)
            taylor = Taylor(f, a_value, n_value)

            # Cálculo de Taylor, errores y gráfico
            model = taylor.taylor()
            valor_teorico, valor_experimental, error_absoluto, error_relativo = taylor.errores(x_value)
            plot_url = taylor.grafica([x_min, x_max])

            result = {
                'series_latex': sp.latex(model),
                'valor_teorico': valor_teorico,
                'valor_experimental': valor_experimental,
                'error_absoluto': error_absoluto,
                'error_relativo': error_relativo
            }

        elif 'f_expr' in request.form:  # Handle numerical differentiation calculation
            f_expr_input = request.form['f_expr']
            xi = float(request.form['xi'])
            h = float(request.form['h'])

            # Procesamiento con SymPy
            f_expr = sp.sympify(f_expr_input)
            f = sp.Lambda(x, f_expr)
            f_prime_theoretical = sp.diff(f_expr, x)

            valor_teorico = f_prime_theoretical.subs(x, xi).evalf()
            valor_experimental = derivacion_numerica(f, xi, h)
            error_abs = calculate_error_absoluto(valor_teorico, valor_experimental)
            error_rel = calculate_error_relativo(valor_teorico, valor_experimental)

            result = {
                'valor_teorico': valor_teorico,
                'valor_experimental': valor_experimental,
                'error_abs': error_abs,
                'error_rel': error_rel
            }
            plot_url = None  # No hay gráfico para derivación numérica

    return render_template('index.html', result=result, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)

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

def parse_function(func_str):
    try:
        # Reemplazar ^ por ** para exponentes
        func_str = func_str.replace('^', '**')
        # Reemplazar e por exp
        func_str = func_str.replace('e', 'exp')
        return sp.sympify(func_str)
    except sp.SympifyError as e:
        raise ValueError(f"Error al analizar la función: {str(e)}")

def biseccion(f, a, b, tolerancia):
    fa = f.subs(x, a)
    fb = f.subs(x, b)
    if fa * fb > 0:
        return None, "No hay raíces en este intervalo"
    
    xr = (a + b) / 2
    fxr = f.subs(x, xr)
    iteraciones = 0
    
    while abs(fxr) > tolerancia and iteraciones < 1000:
        if fa * fxr > 0:
            a = xr
            fa = fxr
        else:
            b = xr
            fb = fxr
        
        xr = (a + b) / 2
        fxr = f.subs(x, xr)
        iteraciones += 1
    
    return xr, iteraciones

def newton(f, xi, tolerancia):
    try:
        fxi = f.subs(x, xi)
        iteraciones = 0
        while abs(fxi) > tolerancia and iteraciones < 1000:
            xi = xi - f.subs(x, xi) / f.diff(x).subs(x, xi)
            fxi = f.subs(x, xi)
            iteraciones += 1
        return xi, iteraciones
    except Exception as e:
        raise ValueError(f"Error durante el cálculo: {str(e)}")


def plot_function(f, xr, method):
    plt.figure(figsize=(10, 6))
    x_vals = np.linspace(xr - 2, xr + 2, 1000)
    y_vals = [f.subs(x, i) for i in x_vals]
    plt.plot(x_vals, y_vals)
    plt.plot(xr, 0, 'r*')
    plt.legend(['f(x)', 'Raíz'])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Método de {method}')
    plt.grid(True)
    
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url


@app.route('/', methods=['GET', 'POST'])
def index():
    section = request.args.get('section', 'home')
    result = None
    plot_url = None

    if request.method == 'POST':
        if 'expression' in request.form:
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

        elif 'f_expr' in request.form:
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
        elif 'root_function' in request.form:
            function = sp.sympify(request.form['root_function'])
            method = request.form['method']
            
            if method == 'biseccion':
                a = float(request.form['a'])
                b = float(request.form['b'])
                tolerancia = float(request.form['tolerancia'])
                root, iteraciones = biseccion(function, a, b, tolerancia)
            else:  # newton
                xi = float(request.form['xi'])
                tolerancia = float(request.form['tolerancia'])
                root, iteraciones = newton(function, xi, tolerancia)
            
            if root is not None:
                result = {
                    'root': root,
                    'iteraciones': iteraciones
                }
                plot_url = plot_function(function, root, method.capitalize())
            else:
                result = {'error': "No se pudo encontrar una raíz"}

    return render_template('index.html', section=section, result=result, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)

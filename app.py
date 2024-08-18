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

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    plot_url = None
    
    if request.method == 'POST':
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

    return render_template('index.html', result=result, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import sympy as sp
from taylor_series.calculus import Taylor, get_derivacion_results, biseccion, newton
from taylor_series.plotting import plot_taylor, plot_root_finding

app = Flask(__name__)

# Fix matplotlib main thread issue
import matplotlib
matplotlib.use('Agg')

@app.route('/', methods=['GET', 'POST'])
def index():
    section = request.args.get('section', 'home')
    result = None
    plot_url = None
    error_message = None

    if request.method == 'POST':
        try:
            if 'expression' in request.form:
                expression = request.form['expression']
                a_value = request.form['a_value']
                n_value = request.form['n_value']
                x_value = request.form['x_value']
                x_min = request.form['x_min']
                x_max = request.form['x_max']

                f = sp.sympify(expression)
                taylor = Taylor(f, a_value, n_value)

                # Taylor calc
                model = taylor.taylor()
                valor_teorico, valor_experimental, error_absoluto, error_relativo = taylor.errores(x_value)
                
                # Plot
                plot_url = plot_taylor(f, model, [x_min, x_max])

                result = {
                    'series_latex': sp.latex(model),
                    'valor_teorico': valor_teorico,
                    'valor_experimental': valor_experimental,
                    'error_absoluto': error_absoluto,
                    'error_relativo': error_relativo
                }

            elif 'f_expr' in request.form:
                f_expr_input = request.form['f_expr']
                xi = request.form['xi']
                h = request.form['h']

                result = get_derivacion_results(f_expr_input, xi, h)

            elif 'root_function' in request.form:
                function_str = request.form['root_function']
                method = request.form['method']
                function = sp.sympify(function_str)
                
                root = None
                iteraciones = 0
                msg = None

                if method == 'biseccion':
                    a = request.form['a']
                    b = request.form['b']
                    tolerancia = request.form['tolerancia']
                    root, msg = biseccion(function, a, b, tolerancia)
                else:  # newton
                    xi = request.form['xi']
                    tolerancia = request.form['tolerancia']
                    root, msg = newton(function, xi, tolerancia)
                
                if root is not None:
                    # If root comes back as complex or integer, ensure we display it nicely?
                    # For now root should be float if success
                    result = {
                        'root': root,
                        'iteraciones': msg if isinstance(msg, int) else 0 # msg returns iteraciones if success
                    }
                    plot_url = plot_root_finding(function, root, method.capitalize())
                else:
                    error_message = msg

        except Exception as e:
            error_message = f"Error procesando la solicitud: {str(e)}"

    return render_template('index.html', section=section, result=result, plot_url=plot_url, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)

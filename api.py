from flask import Flask, request, jsonify
from flask_cors import CORS
from poly_expand.core.parser import parse, latex_to_algebraic
from poly_expand.core.transformer import to_polynomial
from poly_expand.export.latex import polynomial_to_latex


app = Flask(__name__)
CORS(app)

@app.route('/expand', methods=['POST'])
def expand():
    data = request.get_json()
    expr = data.get('expression', '')
    if not expr:
        return jsonify({'error': 'No expression provided'}), 400
    try:
        expr_proc = latex_to_algebraic(expr)
        ast = parse(expr_proc)
        poly = to_polynomial(ast)
        result = str(poly)
        latex = polynomial_to_latex(poly)
        return jsonify({'result': result, 'latex': latex})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

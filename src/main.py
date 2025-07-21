from fastapi import FastAPI, Request
from pydantic import BaseModel
from back.core.parser import parse
from back.core.transformer import to_polynomial
from back.export.latex import polynomial_to_latex

app = FastAPI()

class InputExpr(BaseModel):
    expr: str

@app.get("/")
def read_root():
    return {"message": "API de expansión de polinomios"}

@app.post("/expandir")
def expandir_polynomial(data: InputExpr):
    try:
        expr_ast = parse(data.expr)
        poly = to_polynomial(expr_ast)
        latex_result = polynomial_to_latex(poly)
        return {"latex": latex_result}
    except Exception as e:
        return {"error": str(e)}